(function () {
  const aliases = {
    '3d_rotation': 'box',
    account_circle: 'circle-user-round',
    add_alert: 'bell-ring',
    air: 'wind',
    analytics: 'chart-no-axes-combined',
    arrow_back: 'arrow-left',
    arrow_forward_ios: 'chevron-right',
    battery_full: 'battery-full',
    call: 'phone',
    chat: 'message-circle',
    check_circle: 'circle-check',
    close: 'x',
    directions_boat: 'ship',
    emergency_home: 'house-heart',
    emergency_share: 'siren',
    expand_less: 'chevron-up',
    groups: 'users-round',
    headset_mic: 'headset',
    info: 'info',
    location_on: 'map-pin',
    map: 'map',
    menu: 'menu',
    mic: 'mic',
    my_location: 'locate-fixed',
    near_me: 'navigation',
    notifications: 'bell',
    person: 'user-round',
    psychology: 'brain-circuit',
    query_stats: 'chart-spline',
    radar: 'radar',
    report: 'triangle-alert',
    satellite: 'satellite',
    search: 'search',
    settings: 'settings',
    signal_cellular_alt: 'chart-no-axes-column-increasing',
    smart_toy: 'bot',
    spatial_audio_off: 'audio-lines',
    support_agent: 'headset',
    sync: 'refresh-cw',
    tsunami: 'waves',
    trending_up: 'trending-up',
    visibility: 'eye',
    volume_up: 'volume-2',
    warning: 'triangle-alert',
    water: 'waves',
    water_drop: 'droplets',
    waves: 'waves',
    wb_sunny: 'sun',
    wifi: 'wifi'
  };

  function iconName(value) {
    const key = String(value || '').trim().toLowerCase().replace(/\s+/g, '_');
    return aliases[key] || key.replace(/_/g, '-') || 'circle-dot';
  }

  function prepare(root) {
    root.querySelectorAll('span.material-symbols-outlined').forEach((node) => {
      if (node.dataset.aqIcon) return;
      node.dataset.aqIcon = iconName(node.dataset.icon || node.textContent);
      node.dataset.lucide = node.dataset.aqIcon;
      node.setAttribute('aria-hidden', 'true');
      node.textContent = '';
    });

    root.querySelectorAll('i[class*="ti-"]').forEach((node) => {
      if (node.dataset.aqIcon) return;
      const token = Array.from(node.classList).find((name) => name.startsWith('ti-'));
      node.dataset.aqIcon = iconName(token ? token.slice(3) : 'circle-dot');
      node.dataset.lucide = node.dataset.aqIcon;
      node.setAttribute('aria-hidden', 'true');
    });
  }

  let rendering = false;
  function render() {
    if (rendering || !window.lucide) return;
    rendering = true;
    prepare(document);
    window.lucide.createIcons({
      attrs: { 'stroke-width': 1.9 },
      nameAttr: 'data-lucide'
    });
    rendering = false;
  }

  const observer = new MutationObserver(() => requestAnimationFrame(render));
  window.addEventListener('DOMContentLoaded', () => {
    render();
    observer.observe(document.body, { childList: true, subtree: true });
  });
})();
