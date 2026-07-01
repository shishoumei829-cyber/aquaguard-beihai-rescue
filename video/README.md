# AquaGuard 项目介绍短片

自动生成符合答辩/展板要求的 1 分钟产品发布会风格介绍视频。

## 输出规格

| 项目 | 要求 | 实际输出 |
|------|------|----------|
| 格式 | MP4 | MP4 |
| 视频编码 | H.264 | H.264 |
| 音频编码 | AAC | AAC |
| 分辨率 | ≥ 800×600 | 1280×720 |
| 时长 | ≤ 1 分钟 | ~55 秒 |
| 大小 | ≤ 20 MB | ~5 MB |

## 成品位置

```
video/output/AquaGuard_介绍片.mp4
```

## 视频结构（按答辩要求）

| 时段 | 内容 |
|------|------|
| 前 9 秒 | 痛点与使用场景（儿童走失、越界溺水、多警报调度难） |
| 中间 32 秒 | 产品功能与四端协同（指挥终端、任务闭环、救生员双端、游客监护端） |
| 后 10 秒 | 创新点与应用价值（多源融合、真实海岸、三端协同、完整闭环） |

## 重新生成

```bash
# 安装依赖（首次）
pip3 install playwright pillow edge-tts
python3 -m playwright install chromium

# 一键生成
python3 video/generate_video.py
```

脚本会自动：
1. 启动本地预览服务（`serve.py`）
2. 截取各端界面截图
3. 录制发布会风格演示页（`aquaguard_launch.html`）
4. 用 Edge TTS 生成中文旁白
5. FFmpeg 合成最终 MP4

## 自定义

- **旁白文案**：编辑 `generate_video.py` 中的 `NARRATION` 列表
- **画面节奏**：编辑 `aquaguard_launch.html` 中各场景的 `data-duration`
- **配音音色**：修改 `generate_video.py` 中的 `voice` 变量（如 `zh-CN-XiaoxiaoNeural`）
