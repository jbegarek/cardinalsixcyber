(function () {
    var toggle = document.querySelector('.nav-toggle');
    var overlay = document.getElementById('navOverlay');
    if (!toggle || !overlay) return;
    var links = overlay.querySelectorAll('a');

    function closeMenu() {
        overlay.classList.remove('open');
        toggle.classList.remove('active');
        toggle.setAttribute('aria-expanded', 'false');
        document.body.classList.remove('nav-locked');
        toggle.focus();
    }

    toggle.addEventListener('click', function () {
        var isOpen = overlay.classList.toggle('open');
        toggle.classList.toggle('active');
        toggle.setAttribute('aria-expanded', String(isOpen));
        document.body.classList.toggle('nav-locked', isOpen);
        if (isOpen && links.length) links[0].focus();
    });

    links.forEach(function (link) { link.addEventListener('click', closeMenu); });

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && overlay.classList.contains('open')) closeMenu();
    });

    overlay.addEventListener('keydown', function (e) {
        if (e.key !== 'Tab' || !overlay.classList.contains('open')) return;
        var focusable = overlay.querySelectorAll('a[href]');
        var first = focusable[0], last = focusable[focusable.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });
})();
