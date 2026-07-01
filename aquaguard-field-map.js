/* AquaGuard Field · 共用地图导航（与指挥终端坐标系一致） */
window.AquaGuardMap = (function () {
  const PX_PER_M = 72 / 200;
  const BEACH = { center: [21.400495, 109.154491], zoom: 17 };

  function xyToLatLng(cx, cy) {
    const mx = (cx - 480) * PX_PER_M;
    const my = (cy - 156) * PX_PER_M;
    return [BEACH.center[0] - my * 0.000009, BEACH.center[1] + mx * 0.000009];
  }

  function distM(x1, y1, x2, y2) {
    return Math.round(Math.hypot(x2 - x1, y2 - y1) / PX_PER_M);
  }

  function bearing(cx1, cy1, cx2, cy2) {
    let deg = Math.atan2(cx2 - cx1, cy1 - cy2) * 180 / Math.PI;
    if (deg < 0) deg += 360;
    return Math.round(deg);
  }

  function makeIcon(cls, pulse) {
    return L.divIcon({
      className: '',
      html: `<div class="${cls}${pulse ? ' pulse' : ''}"></div>`,
      iconSize: [16, 16],
      iconAnchor: [8, 8]
    });
  }

  function init(containerId, opts) {
    opts = opts || {};
    const map = L.map(containerId, {
      zoomControl: false,
      attributionControl: false,
      dragging: opts.dragging !== false,
      scrollWheelZoom: !!opts.scrollWheelZoom,
      doubleClickZoom: false,
      touchZoom: opts.touchZoom !== false,
      boxZoom: false,
      keyboard: false
    }).setView(BEACH.center, opts.zoom || BEACH.zoom);

    L.tileLayer(
      'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
      { maxZoom: 19 }
    ).addTo(map);

    const routeLayer = L.layerGroup().addTo(map);
    const markerLayer = L.layerGroup().addTo(map);

    return {
      map,
      routeLayer,
      markerLayer,
      invalidate() {
        setTimeout(function () { map.invalidateSize(); }, 80);
      }
    };
  }

  function update(ctx, config) {
    const map = ctx.map;
    const routeLayer = ctx.routeLayer;
    const markerLayer = ctx.markerLayer;
    routeLayer.clearLayers();
    markerLayer.clearLayers();

    if (!config || !config.active) {
      map.setView(BEACH.center, config && config.idleZoom ? config.idleZoom : BEACH.zoom);
      return null;
    }

    const points = [];

    if (config.origin) {
      const oll = xyToLatLng(config.origin.cx, config.origin.cy);
      markerLayer.addLayer(L.marker(oll, {
        icon: makeIcon(config.originClass || 'nav-marker-guard'),
        zIndexOffset: 100
      }));
      points.push(oll);
    }

    (config.extras || []).forEach(function (e) {
      const ll = xyToLatLng(e.cx, e.cy);
      markerLayer.addLayer(L.marker(ll, {
        icon: makeIcon(e.className || 'nav-marker-target alert'),
        zIndexOffset: 40
      }));
      points.push(ll);
    });

    if (config.target) {
      const tll = xyToLatLng(config.target.cx, config.target.cy);
      const isAlert = config.target.risk === 'alert';
      markerLayer.addLayer(L.marker(tll, {
        icon: makeIcon(
          'nav-marker-target' + (isAlert ? ' alert' : ''),
          config.target.risk === 'emg'
        ),
        zIndexOffset: 200
      }));
      points.push(tll);

      if (config.origin) {
        const oll = xyToLatLng(config.origin.cx, config.origin.cy);
        L.polyline([oll, tll], {
          color: '#182e7d',
          weight: 3,
          opacity: 0.8,
          dashArray: config.target.risk === 'emg' ? null : '8 6'
        }).addTo(routeLayer);
      }
    }

    if (points.length === 1) {
      map.setView(points[0], config.focusZoom || 18, { animate: true });
    } else if (points.length > 1) {
      map.fitBounds(L.latLngBounds(points), {
        padding: config.padding || [40, 40],
        maxZoom: config.maxZoom || 18,
        animate: true
      });
    }

    if (config.origin && config.target) {
      return {
        dist: distM(config.origin.cx, config.origin.cy, config.target.cx, config.target.cy),
        bear: bearing(config.origin.cx, config.origin.cy, config.target.cx, config.target.cy)
      };
    }
    return null;
  }

  return { PX_PER_M, BEACH, xyToLatLng, distM, bearing, init, update };
})();
