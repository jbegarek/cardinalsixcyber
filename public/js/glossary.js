(function () {
    var searchInput = document.getElementById('glossarySearch');
    var groups = document.querySelectorAll('.letter-group');
    var rows = document.querySelectorAll('.term-row');
    var emptyState = document.getElementById('emptyState');
    var resultsEl = document.getElementById('glossaryResults');
    var letterLinks = document.querySelectorAll('.letter-link:not(.letter-disabled)');

    /* Highlight active letter as user scrolls */
    if ('IntersectionObserver' in window) {
        var letterObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    var letter = entry.target.getAttribute('data-letter-group');
                    letterLinks.forEach(function (link) {
                        link.classList.toggle('letter-active', link.getAttribute('data-letter') === letter);
                    });
                }
            });
        }, { threshold: 0, rootMargin: '-180px 0px -70% 0px' });
        groups.forEach(function (g) { letterObserver.observe(g); });
    }

    if (searchInput) {
        var debounceTimer;
        searchInput.addEventListener('input', function () {
            clearTimeout(debounceTimer);
            debounceTimer = setTimeout(function () {
                applySearch(searchInput.value.trim().toLowerCase());
            }, 150);
        });
    }

    function applySearch(query) {
        var visibleCount = 0;
        var groupVisibleCounts = {};

        rows.forEach(function (row) {
            var searchText = row.getAttribute('data-search') || '';
            var visible = !query || searchText.indexOf(query) !== -1;
            row.hidden = !visible;
            if (visible) {
                visibleCount++;
                var group = row.closest('.letter-group');
                if (group) {
                    var letter = group.getAttribute('data-letter-group') || '';
                    groupVisibleCounts[letter] = (groupVisibleCounts[letter] || 0) + 1;
                }
            }
        });

        groups.forEach(function (group) {
            var letter = group.getAttribute('data-letter-group') || '';
            var count = groupVisibleCounts[letter] || 0;
            group.hidden = count === 0;
            var countEl = group.querySelector('[data-letter-count]');
            if (countEl) countEl.textContent = String(count);
        });

        letterLinks.forEach(function (link) {
            var letter = link.getAttribute('data-letter');
            if (groupVisibleCounts[letter] || !query) {
                link.classList.remove('letter-dimmed');
            } else {
                link.classList.add('letter-dimmed');
            }
        });

        if (emptyState) emptyState.hidden = visibleCount > 0;
        if (resultsEl) resultsEl.hidden = visibleCount === 0;
    }
})();
