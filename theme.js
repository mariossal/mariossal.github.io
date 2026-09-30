(function () {
  var root = document.documentElement, key = 'theme';
  function saved() { try { return localStorage.getItem(key); } catch (e) { return null; } }
  function apply(t) { if (t === 'dark' || t === 'light') root.setAttribute('data-theme', t); else root.removeAttribute('data-theme'); }
  function current() { return saved() || 'light'; }
  apply(current());
  document.addEventListener('DOMContentLoaded', function () {
    var b = document.getElementById('theme-toggle'); if (!b) return;
    function label() { b.setAttribute('aria-label', current() === 'dark' ? 'Switch to light theme' : 'Switch to dark theme'); b.setAttribute('title', b.getAttribute('aria-label')); }
    label();
    b.addEventListener('click', function () {
      var next = current() === 'dark' ? 'light' : 'dark';
      apply(next); try { localStorage.setItem(key, next); } catch (e) {} label();
    });
  });
})();
