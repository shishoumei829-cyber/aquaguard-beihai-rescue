#!/usr/bin/env python3
"""
AquaGuard 项目介绍短片生成器
输出规格：MP4 / H.264 / AAC / 1280x720 / ≤60s / ≤20MB
"""
from __future__ import annotations

import asyncio
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VIDEO_DIR = ROOT / "video"
ASSETS_DIR = VIDEO_DIR / "assets"
OUTPUT_DIR = VIDEO_DIR / "output"
LAUNCH_HTML = VIDEO_DIR / "aquaguard_launch.html"
FINAL_VIDEO = OUTPUT_DIR / "AquaGuard_介绍片.mp4"

VIEWPORT = {"width": 1280, "height": 720}
SERVER_PORT = 8766
SERVER_URL = f"http://127.0.0.1:{SERVER_PORT}"

# 旁白脚本（与 HTML 场景时长对齐，总计 60 秒）
NARRATION = [
    {
        "id": "pain",
        "text": "北海银滩，每天涌入上千名游客。孩子走失说不清位置，有人游进深水区，救生员肉眼顾不过来。多警报同时响起——谁先救？往哪派？",
        "duration": 9.0,
    },
    {
        "id": "reveal",
        "text": "AquaGuard，北海银滩智能救援指挥系统。",
        "duration": 4.0,
    },
    {
        "id": "command",
        "text": "所有信号汇入指挥终端。事件流实时滚动，态势图精准标注风险，任务面板自动排序优先级。",
        "duration": 9.0,
    },
    {
        "id": "workflow",
        "text": "系统预警、家长报案、手环 SOS 统一进入任务流。从发现、确认、派遣到完成，全程可追踪。",
        "duration": 8.0,
    },
    {
        "id": "lifeguard",
        "text": "儿童走失？系统秒级匹配手环候选目标。哨塔平板持续播报，出动手机导航直达现场。",
        "duration": 8.0,
    },
    {
        "id": "tourist",
        "text": "家长通过监护端关联亲友，一键报案，信息秒级同步至指挥终端。",
        "duration": 7.0,
    },
    {
        "id": "close",
        "text": "AquaGuard，把海滩安全从被动观察升级为主动应急调度。让每一次求救，都有回应、有路径、有结果。",
        "duration": 10.0,
    },
]

SCREENSHOTS = [
    ("screenshot_command.png", "/aquaguard_v3_full.html", VIEWPORT),
    ("screenshot_allmaps.png", "/beihai_rescue_all_maps_glass_fixed.html", VIEWPORT),
    ("screenshot_tablet.png", "/aquaguard_lifeguard_tablet.html", {"width": 1024, "height": 768}),
    ("screenshot_phone.png", "/aquaguard_lifeguard_phone.html", {"width": 390, "height": 844}),
    ("screenshot_tourist.png", "/aquaguard_tourist.html", {"width": 390, "height": 844}),
]


def log(msg: str) -> None:
    print(f"[generate] {msg}", flush=True)


def start_server() -> subprocess.Popen:
    log("启动本地预览服务…")
    proc = subprocess.Popen(
        [sys.executable, str(ROOT / "serve.py")],
        cwd=str(ROOT),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    for _ in range(30):
        try:
            import urllib.request
            urllib.request.urlopen(f"{SERVER_URL}/", timeout=1)
            log(f"服务就绪: {SERVER_URL}")
            return proc
        except Exception:
            time.sleep(0.5)
    proc.kill()
    raise RuntimeError("本地服务启动失败")


async def capture_screenshots() -> None:
    from playwright.async_api import async_playwright

    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    log("截取产品界面截图…")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        for filename, path, vp in SCREENSHOTS:
            page = await browser.new_page(viewport=vp)
            url = f"{SERVER_URL}{path}"
            await page.goto(url, wait_until="networkidle", timeout=60000)
            await page.wait_for_timeout(2500)

            if "phone" in filename or "tourist" in filename:
                # 手机端截图：居中裁切到合理比例
                await page.screenshot(path=str(ASSETS_DIR / filename), full_page=False)
            elif "tablet" in filename:
                await page.screenshot(path=str(ASSETS_DIR / filename), full_page=False)
            else:
                await page.screenshot(path=str(ASSETS_DIR / filename), full_page=False)
            await page.close()
            log(f"  ✓ {filename}")
        await browser.close()


async def record_launch_video() -> Path:
    from playwright.async_api import async_playwright

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    raw_video_dir = OUTPUT_DIR / "raw"
    if raw_video_dir.exists():
        shutil.rmtree(raw_video_dir)
    raw_video_dir.mkdir(parents=True)

    launch_url = LAUNCH_HTML.as_uri()
    log(f"录制发布会演示页: {launch_url}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport=VIEWPORT,
            record_video_dir=str(raw_video_dir),
            record_video_size=VIEWPORT,
        )
        page = await context.new_page()
        await page.goto(launch_url, wait_until="networkidle", timeout=30000)
        # 等待全部场景播放完毕（60s + 缓冲）
        await page.wait_for_function("document.body.dataset.done === 'true'", timeout=75000)
        await page.wait_for_timeout(1500)
        await context.close()
        await browser.close()

    webm_files = list(raw_video_dir.glob("*.webm"))
    if not webm_files:
        raise RuntimeError("录屏失败：未生成 webm 文件")
    raw_webm = OUTPUT_DIR / "raw_silent.webm"
    shutil.move(str(webm_files[0]), str(raw_webm))
    shutil.rmtree(raw_video_dir, ignore_errors=True)
    log(f"  ✓ 无声视频: {raw_webm.name}")
    return raw_webm


async def generate_narration() -> Path:
    import edge_tts

    voice = "zh-CN-YunxiNeural"
    log(f"生成中文旁白 (voice={voice})…")

    segments_dir = OUTPUT_DIR / "audio_segments"
    if segments_dir.exists():
        shutil.rmtree(segments_dir)
    segments_dir.mkdir(parents=True)

    segment_files: list[Path] = []
    for i, seg in enumerate(NARRATION):
        out = segments_dir / f"{i:02d}_{seg['id']}.mp3"
        communicate = edge_tts.Communicate(seg["text"], voice, rate="+18%")
        await communicate.save(str(out))
        segment_files.append(out)
        log(f"  ✓ 旁白片段 {seg['id']}")

    # 合并旁白片段
    concat_list = segments_dir / "concat.txt"
    with open(concat_list, "w") as f:
        for fp in segment_files:
            f.write(f"file '{fp}'\n")

    narration_mp3 = OUTPUT_DIR / "narration.mp3"
    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list),
         "-c", "copy", str(narration_mp3)],
        check=True, capture_output=True,
    )
    log(f"  ✓ 旁白合并: {narration_mp3.name}")
    return narration_mp3


def merge_video_audio(video_path: Path, audio_path: Path) -> Path:
    log("合成最终视频…")
    temp_merged = OUTPUT_DIR / "merged_temp.mp4"
    adjusted_audio = OUTPUT_DIR / "narration_adjusted.mp3"

    def probe_duration(path: Path) -> float:
        result = subprocess.run(
            ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", str(path)],
            capture_output=True, text=True, check=True,
        )
        return float(json.loads(result.stdout)["format"]["duration"])

    vid_dur = probe_duration(video_path)
    aud_dur = probe_duration(audio_path)
    log(f"  视频时长 {vid_dur:.1f}s, 旁白时长 {aud_dur:.1f}s")

    target_dur = min(max(vid_dur, aud_dur), 60.0)

    # 若旁白略长，加速适配（不截断）
    audio_input = audio_path
    if aud_dur > target_dur:
        tempo = min(aud_dur / target_dur, 1.35)
        log(f"  旁白加速 {tempo:.2f}x 以适配时长")
        subprocess.run(
            ["ffmpeg", "-y", "-i", str(audio_path),
             "-filter:a", f"atempo={tempo:.4f}", str(adjusted_audio)],
            check=True, capture_output=True,
        )
        audio_input = adjusted_audio
        aud_dur = probe_duration(audio_input)

    final_dur = min(vid_dur, aud_dur, 60.0)

    subprocess.run(
        [
            "ffmpeg", "-y",
            "-i", str(video_path),
            "-i", str(audio_input),
            "-t", str(final_dur),
            "-c:v", "libx264", "-preset", "medium", "-crf", "23",
            "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
            "-pix_fmt", "yuv420p",
            "-movflags", "+faststart",
            "-shortest",
            str(temp_merged),
        ],
        check=True, capture_output=True,
    )

    # 检查文件大小，必要时压缩
    size_mb = temp_merged.stat().st_size / (1024 * 1024)
    log(f"  初次合成大小: {size_mb:.1f} MB")

    if size_mb > 19.5:
        log("  文件偏大，二次压缩…")
        subprocess.run(
            [
                "ffmpeg", "-y", "-i", str(temp_merged),
                "-c:v", "libx264", "-preset", "slow", "-crf", "28",
                "-c:a", "aac", "-b:a", "96k",
                "-movflags", "+faststart",
                str(FINAL_VIDEO),
            ],
            check=True, capture_output=True,
        )
    else:
        shutil.move(str(temp_merged), str(FINAL_VIDEO))

    if temp_merged.exists():
        temp_merged.unlink()

    return FINAL_VIDEO


def verify_output(path: Path) -> dict:
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-print_format", "json",
         "-show_format", "-show_streams", str(path)],
        capture_output=True, text=True, check=True,
    )
    info = json.loads(result.stdout)
    fmt = info["format"]
    duration = float(fmt["duration"])
    size_mb = int(fmt["size"]) / (1024 * 1024)

    video_stream = next(s for s in info["streams"] if s["codec_type"] == "video")
    audio_stream = next((s for s in info["streams"] if s["codec_type"] == "audio"), None)

    report = {
        "duration": round(duration, 1),
        "size_mb": round(size_mb, 2),
        "width": video_stream["width"],
        "height": video_stream["height"],
        "video_codec": video_stream["codec_name"],
        "audio_codec": audio_stream["codec_name"] if audio_stream else "none",
    }
    return report


async def main() -> None:
    os.environ["PATH"] = os.environ.get("PATH", "") + ":/home/ubuntu/.local/bin"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    server = start_server()
    try:
        await capture_screenshots()
        raw_video = await record_launch_video()
        narration = await generate_narration()
        final = merge_video_audio(raw_video, narration)
        report = verify_output(final)

        log("=" * 50)
        log(f"✅ 视频生成完成: {final}")
        log(f"   时长: {report['duration']}s (要求 ≤60s)")
        log(f"   大小: {report['size_mb']} MB (要求 ≤20MB)")
        log(f"   分辨率: {report['width']}x{report['height']} (要求 ≥800x600)")
        log(f"   视频编码: {report['video_codec']} (要求 H.264)")
        log(f"   音频编码: {report['audio_codec']} (要求 AAC)")

        ok = (
            report["duration"] <= 60
            and report["size_mb"] <= 20
            and report["width"] >= 800
            and report["height"] >= 600
            and report["video_codec"] == "h264"
            and report["audio_codec"] == "aac"
        )
        if not ok:
            log("⚠️  部分规格未达标，请检查")
            sys.exit(1)
    finally:
        server.terminate()
        server.wait(timeout=5)


if __name__ == "__main__":
    asyncio.run(main())
