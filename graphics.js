/* marios_sal site graphics: day-unfolding forecast chart, energy node network, ambient hero drift.
   Canvas-based, uses the site's CSS colour tokens, respects prefers-reduced-motion. */
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function css(name) { return getComputedStyle(document.documentElement).getPropertyValue(name).trim(); }
  function hex2rgba(h, a) {
    h = h.replace('#', ''); if (h.length === 3) h = h.split('').map(function (c) { return c + c; }).join('');
    var n = parseInt(h, 16); return 'rgba(' + (n >> 16 & 255) + ',' + (n >> 8 & 255) + ',' + (n & 255) + ',' + a + ')';
  }
  function fit(canvas) {
    var dpr = Math.min(window.devicePixelRatio || 1, 2), r = canvas.getBoundingClientRect();
    canvas.width = Math.round(r.width * dpr); canvas.height = Math.round(r.height * dpr);
    var ctx = canvas.getContext('2d'); ctx.setTransform(dpr, 0, 0, dpr, 0, 0); return { ctx: ctx, w: r.width, h: r.height };
  }
  function onVisible(el, start, stop) {
    if (!('IntersectionObserver' in window)) { start(); return; }
    new IntersectionObserver(function (es) { es.forEach(function (e) { e.isIntersecting ? start() : stop(); }); }, { threshold: 0.05 }).observe(el);
  }
  function mono() { return '500 11px "IBM Plex Mono", monospace'; }

  /* ---------- 1. The day unfolding: PV forecast vs actual ---------- */
  function dayChart(canvas) {
    var N = 288, forecast = [], actual = [], t = 0, raf = null, state = fit(canvas);
    // Plausible summer profile: forecast is a smooth bell, actual follows with morning haze and afternoon clouds
    function bell(i) { var x = (i / N) * 24, s = (x - 13.1) / 3.7; return Math.max(0, Math.exp(-s * s * 0.9) - 0.03) / 0.97; }
    function seeded(i) { var x = Math.sin(i * 12.9898 + 78.233) * 43758.5453; return x - Math.floor(x); }
    for (var i = 0; i < N; i++) {
      var b = bell(i), x = (i / N) * 24;
      forecast.push(b);
      var cloud = 0;
      if (x > 14.2 && x < 15.6) cloud = 0.42 * Math.sin(((x - 14.2) / 1.4) * Math.PI);
      if (x > 16.4 && x < 17.0) cloud = 0.25 * Math.sin(((x - 16.4) / 0.6) * Math.PI);
      var haze = x > 7 && x < 9.5 ? 0.12 * Math.sin(((x - 7) / 2.5) * Math.PI) : 0;
      var noise = (seeded(i) - 0.5) * 0.035 * b;
      actual.push(Math.max(0, b * (1 - cloud - haze) + noise));
    }
    var CYCLE = 11000, HOLD = 2500;
    function draw(now) {
      var ctx = state.ctx, w = state.w, h = state.h;
      var ink = css('--ink'), ink2 = css('--ink-2'), rule = css('--rule'), teal = css('--accent'), orange = '#e9772c';
      var padL = 34, padR = 14, padT = 22, padB = 30, W = w - padL - padR, H = h - padT - padB;
      var phase = reduce ? 1 : ((now % (CYCLE + HOLD)) / CYCLE); if (phase > 1) phase = 1;
      var eased = phase < 1 ? phase : 1;
      ctx.clearRect(0, 0, w, h);
      // grid
      ctx.strokeStyle = hex2rgba(rule, 0.9); ctx.lineWidth = 1;
      for (var g = 0; g <= 4; g++) { var y = padT + H - (H * g) / 4; ctx.beginPath(); ctx.moveTo(padL, y); ctx.lineTo(w - padR, y); ctx.stroke(); }
      ctx.fillStyle = ink2; ctx.font = mono(); ctx.textAlign = 'center';
      [0, 6, 12, 18, 24].forEach(function (hr) { ctx.fillText((hr < 10 ? '0' : '') + hr + ':00', padL + (W * hr) / 24, h - 10); });
      ctx.textAlign = 'right'; ctx.fillText('kW', padL - 8, padT + H / 2); ctx.fillText('0', padL - 8, padT + H + 4);
      function X(i) { return padL + (W * i) / (N - 1); }
      function Y(v) { return padT + H - v * H * 0.92; }
      // forecast, dashed teal, whole day
      ctx.setLineDash([5, 6]); ctx.strokeStyle = teal; ctx.lineWidth = 1.6; ctx.beginPath();
      for (var i = 0; i < N; i++) { i ? ctx.lineTo(X(i), Y(forecast[i])) : ctx.moveTo(X(i), Y(forecast[i])); }
      ctx.stroke(); ctx.setLineDash([]);
      // actual, revealed up to cursor
      var upto = Math.floor(eased * (N - 1));
      // error shading between the two
      ctx.beginPath();
      for (var i = 0; i <= upto; i++) { i ? ctx.lineTo(X(i), Y(forecast[i])) : ctx.moveTo(X(i), Y(forecast[i])); }
      for (var i = upto; i >= 0; i--) ctx.lineTo(X(i), Y(actual[i]));
      ctx.closePath(); ctx.fillStyle = hex2rgba(orange, 0.16); ctx.fill();
      ctx.strokeStyle = orange; ctx.lineWidth = 2.2; ctx.lineJoin = 'round'; ctx.beginPath();
      for (var i = 0; i <= upto; i++) { i ? ctx.lineTo(X(i), Y(actual[i])) : ctx.moveTo(X(i), Y(actual[i])); }
      ctx.stroke();
      // cursor
      if (eased < 1) {
        var cx = X(upto); ctx.strokeStyle = hex2rgba(ink, 0.35); ctx.lineWidth = 1; ctx.setLineDash([2, 4]);
        ctx.beginPath(); ctx.moveTo(cx, padT); ctx.lineTo(cx, padT + H); ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = orange; ctx.beginPath(); ctx.arc(cx, Y(actual[upto]), 3.5, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = ink; ctx.font = mono(); ctx.textAlign = 'left';
        var hr = (upto / (N - 1)) * 24, hh = Math.floor(hr), mm = Math.floor((hr - hh) * 60);
        ctx.fillText((hh < 10 ? '0' : '') + hh + ':' + (mm < 10 ? '0' : '') + mm, Math.min(cx + 8, w - 60), padT + 12);
      }
      // legend
      ctx.textAlign = 'left'; ctx.font = mono();
      ctx.strokeStyle = teal; ctx.setLineDash([5, 6]); ctx.lineWidth = 1.6; ctx.beginPath(); ctx.moveTo(padL, padT - 10); ctx.lineTo(padL + 22, padT - 10); ctx.stroke(); ctx.setLineDash([]);
      ctx.fillStyle = ink2; ctx.fillText('forecast', padL + 28, padT - 6);
      ctx.strokeStyle = orange; ctx.lineWidth = 2.2; ctx.beginPath(); ctx.moveTo(padL + 100, padT - 10); ctx.lineTo(padL + 122, padT - 10); ctx.stroke();
      ctx.fillText('actual', padL + 128, padT - 6);
      if (!reduce) raf = requestAnimationFrame(draw);
    }
    function start() { if (!raf) raf = requestAnimationFrame(draw); }
    function stop() { if (raf) { cancelAnimationFrame(raf); raf = null; } }
    window.addEventListener('resize', function () { state = fit(canvas); if (reduce) draw(0); });
    if (reduce) draw(0); else onVisible(canvas, start, stop);
  }

  /* ---------- 2. Network of nodes: sun, battery, home, grid, EV ---------- */
  function network(canvas) {
    var raf = null, state = fit(canvas), pulses = [];
    var nodes = [
      { id: 'pv', label: 'PV', x: 0.5, y: 0.14 },
      { id: 'bat', label: 'BATTERY', x: 0.5, y: 0.52 },
      { id: 'home', label: 'LOAD', x: 0.16, y: 0.78 },
      { id: 'grid', label: 'GRID', x: 0.84, y: 0.78 },
      { id: 'ev', label: 'EV', x: 0.84, y: 0.26 },
      { id: 'ems', label: 'EMS', x: 0.16, y: 0.26 }
    ];
    var links = [['pv', 'bat'], ['pv', 'home'], ['bat', 'home'], ['bat', 'grid'], ['pv', 'ev'], ['bat', 'ev'], ['ems', 'pv'], ['ems', 'bat'], ['ems', 'home'], ['grid', 'home']];
    var byId = {}; nodes.forEach(function (n) { byId[n.id] = n; });
    function seeded(i) { var x = Math.sin(i * 91.7 + 3.3) * 10000; return x - Math.floor(x); }
    for (var i = 0; i < 14; i++) pulses.push({ link: i % links.length, t: seeded(i), speed: 0.10 + seeded(i + 50) * 0.12, dir: seeded(i + 99) > 0.5 ? 1 : -1 });
    var last = 0;
    function icon(ctx, id, x, y, col) {
      ctx.strokeStyle = col; ctx.fillStyle = col; ctx.lineWidth = 1.6; ctx.lineCap = 'round';
      if (id === 'pv') { ctx.beginPath(); ctx.arc(x, y, 5, 0, Math.PI * 2); ctx.stroke(); for (var a = 0; a < 8; a++) { var r = a * Math.PI / 4; ctx.beginPath(); ctx.moveTo(x + Math.cos(r) * 8, y + Math.sin(r) * 8); ctx.lineTo(x + Math.cos(r) * 11, y + Math.sin(r) * 11); ctx.stroke(); } }
      else if (id === 'bat') { ctx.strokeRect(x - 10, y - 5.5, 18, 11); ctx.fillRect(x + 9, y - 2.5, 2.5, 5); ctx.fillRect(x - 8, y - 3.5, 9, 7); }
      else if (id === 'home') { ctx.beginPath(); ctx.moveTo(x - 10, y + 1); ctx.lineTo(x, y - 8); ctx.lineTo(x + 10, y + 1); ctx.stroke(); ctx.strokeRect(x - 7, y, 14, 8); }
      else if (id === 'grid') { ctx.beginPath(); ctx.moveTo(x - 6, y + 9); ctx.lineTo(x - 2, y - 9); ctx.lineTo(x + 2, y - 9); ctx.lineTo(x + 6, y + 9); ctx.moveTo(x - 8, y - 4); ctx.lineTo(x + 8, y - 4); ctx.moveTo(x - 5, y + 2); ctx.lineTo(x + 5, y + 2); ctx.stroke(); }
      else if (id === 'ev') { ctx.beginPath(); ctx.moveTo(x - 10, y + 4); ctx.lineTo(x - 7, y - 3); ctx.lineTo(x + 6, y - 3); ctx.lineTo(x + 10, y + 4); ctx.closePath(); ctx.stroke(); ctx.beginPath(); ctx.arc(x - 5, y + 5, 2, 0, Math.PI * 2); ctx.arc(x + 5, y + 5, 2, 0, Math.PI * 2); ctx.fill(); }
      else { ctx.strokeRect(x - 9, y - 7, 18, 14); ctx.beginPath(); ctx.moveTo(x - 5, y + 2); ctx.lineTo(x - 2, y - 2); ctx.lineTo(x + 1, y + 1); ctx.lineTo(x + 5, y - 3); ctx.stroke(); }
    }
    function draw(now) {
      var ctx = state.ctx, w = state.w, h = state.h, dt = last ? Math.min((now - last) / 1000, 0.05) : 0; last = now;
      var ink = css('--ink'), ink2 = css('--ink-2'), rule = css('--rule'), teal = css('--accent'), orange = '#e9772c', paper = css('--paper');
      ctx.clearRect(0, 0, w, h);
      function P(n) { return { x: n.x * w, y: n.y * h }; }
      ctx.strokeStyle = hex2rgba(rule, 1); ctx.lineWidth = 1.2;
      links.forEach(function (l) { var a = P(byId[l[0]]), b = P(byId[l[1]]); ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke(); });
      if (!reduce) pulses.forEach(function (p) { p.t += dt * p.speed * p.dir; if (p.t > 1) p.t = 0; if (p.t < 0) p.t = 1; });
      pulses.forEach(function (p) {
        var l = links[p.link], a = P(byId[l[0]]), b = P(byId[l[1]]), x = a.x + (b.x - a.x) * p.t, y = a.y + (b.y - a.y) * p.t;
        var col = (l[0] === 'ems' || l[1] === 'ems') ? teal : orange;
        ctx.fillStyle = hex2rgba(col, 0.9); ctx.beginPath(); ctx.arc(x, y, 2.6, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = hex2rgba(col, 0.22); ctx.beginPath(); ctx.arc(x, y, 6, 0, Math.PI * 2); ctx.fill();
      });
      nodes.forEach(function (n) {
        var p = P(n), r = 22, col = n.id === 'ems' ? teal : n.id === 'pv' ? orange : ink;
        ctx.fillStyle = paper; ctx.strokeStyle = col; ctx.lineWidth = 1.6; ctx.beginPath(); ctx.arc(p.x, p.y, r, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
        icon(ctx, n.id, p.x, p.y, col);
        ctx.fillStyle = ink2; ctx.font = mono(); ctx.textAlign = 'center'; ctx.fillText(n.label, p.x, p.y + r + 14);
      });
      if (!reduce) raf = requestAnimationFrame(draw);
    }
    function start() { if (!raf) { last = 0; raf = requestAnimationFrame(draw); } }
    function stop() { if (raf) { cancelAnimationFrame(raf); raf = null; } }
    window.addEventListener('resize', function () { state = fit(canvas); if (reduce) draw(0); });
    if (reduce) draw(0); else onVisible(canvas, start, stop);
  }

  /* ---------- 3. Ambient hero background: slowly drifting, breathing curves ---------- */
  function ambient(canvas) {
    var raf = null, state = fit(canvas), t0 = performance.now();
    function draw(now) {
      var ctx = state.ctx, w = state.w, h = state.h, T = (now - t0) / 1000;
      var ink = css('--ink'), teal = css('--accent');
      ctx.clearRect(0, 0, w, h);
      ctx.strokeStyle = hex2rgba(ink, 0.06); ctx.lineWidth = 1;
      for (var g = 1; g <= 4; g++) { var y = h - (h * g) / 5; ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke(); }
      function curve(col, amp, dash, off, width, speed) {
        ctx.strokeStyle = col; ctx.lineWidth = width; ctx.setLineDash(dash); ctx.beginPath();
        for (var x = 0; x <= w; x += 6) {
          var u = x / w, b = Math.exp(-Math.pow((u - 0.5 - 0.02 * Math.sin(T * speed)) / 0.13, 2));
          var wobble = 0.03 * Math.sin(u * 14 + T * 0.7) + 0.02 * Math.sin(u * 31 - T * 0.5);
          var y = h - 12 - (b * (0.80 + 0.06 * Math.sin(T * 0.35)) + wobble * b) * (h - 40) * amp + off;
          x ? ctx.lineTo(x, y) : ctx.moveTo(x, y);
        }
        ctx.stroke(); ctx.setLineDash([]);
      }
      curve(hex2rgba(ink, 0.14), 1, [], 0, 1.2, 0.20);
      curve(hex2rgba(teal, 0.30), 0.82, [4, 6], 30, 1.2, 0.27);
      if (!reduce) raf = requestAnimationFrame(draw);
    }
    function start() { if (!raf) raf = requestAnimationFrame(draw); }
    function stop() { if (raf) { cancelAnimationFrame(raf); raf = null; } }
    window.addEventListener('resize', function () { state = fit(canvas); if (reduce) draw(performance.now()); });
    if (reduce) draw(performance.now()); else onVisible(canvas, start, stop);
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('canvas[data-graphic="day"]').forEach(dayChart);
    document.querySelectorAll('canvas[data-graphic="network"]').forEach(network);
    document.querySelectorAll('canvas[data-graphic="ambient"]').forEach(ambient);
    // redraw on theme switch so the colours follow
    new MutationObserver(function () { window.dispatchEvent(new Event('resize')); }).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });
  });
})();
