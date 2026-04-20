(function () {
    var reveals = document.querySelectorAll('.reveal');
    var vh = window.innerHeight;

    /* Immediate reveal for elements already in/near the viewport */
    reveals.forEach(function (el) {
        var rect = el.getBoundingClientRect();
        if (rect.top < vh * 0.95) el.classList.add('visible');
    });

    var deferred = Array.prototype.filter.call(reveals, function (el) {
        return !el.classList.contains('visible');
    });

    if ('IntersectionObserver' in window && deferred.length) {
        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px 100px 0px' });
        deferred.forEach(function (el) { observer.observe(el); });
    } else {
        deferred.forEach(function (el) { el.classList.add('visible'); });
    }

    /* Fallback: reveal everything after 3s regardless */
    setTimeout(function () {
        reveals.forEach(function (el) { el.classList.add('visible'); });
    }, 3000);
})();
