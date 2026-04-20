(function () {
    var activeDomain = '';
    var activeLevel = '';
    var searchQuery = '';

    var domainPills = document.getElementById('domainPills');
    var levelBtns = document.querySelectorAll('.level-btn');
    var searchInput = document.getElementById('searchInput');
    var groups = document.querySelectorAll('.domain-group');
    var rows = document.querySelectorAll('.practice-row');
    var emptyState = document.getElementById('emptyState');
    var resultsEl = document.getElementById('practiceResults');

    if (domainPills) {
        domainPills.addEventListener('click', function (e) {
            var pill = e.target.closest('.filter-pill');
            if (!pill) return;
            domainPills.querySelectorAll('.filter-pill').forEach(function (p) {
                p.classList.remove('active');
                p.setAttribute('aria-pressed', 'false');
            });
            pill.classList.add('active');
            pill.setAttribute('aria-pressed', 'true');
            activeDomain = pill.getAttribute('data-domain') || '';
            applyFilters();
        });
    }

    levelBtns.forEach(function (btn) {
        btn.addEventListener('click', function () {
            levelBtns.forEach(function (b) {
                b.classList.remove('active');
                b.setAttribute('aria-pressed', 'false');
            });
            btn.classList.add('active');
            btn.setAttribute('aria-pressed', 'true');
            activeLevel = btn.getAttribute('data-level') || '';
            applyFilters();
        });
    });

    if (searchInput) {
        var debounceTimer;
        searchInput.addEventListener('input', function () {
            clearTimeout(debounceTimer);
            debounceTimer = setTimeout(function () {
                searchQuery = searchInput.value.trim().toLowerCase();
                applyFilters();
            }, 150);
        });
    }

    function applyFilters() {
        var visibleCount = 0;
        var groupVisibleCounts = {};

        rows.forEach(function (row) {
            var rowDomain = row.getAttribute('data-domain') || '';
            var rowLevel = row.getAttribute('data-level') || '';
            var rowSearch = row.getAttribute('data-search') || '';

            var domainMatch = !activeDomain || rowDomain === activeDomain;
            var levelMatch = !activeLevel || rowLevel === activeLevel;
            var searchMatch = !searchQuery || rowSearch.indexOf(searchQuery) !== -1;

            var visible = domainMatch && levelMatch && searchMatch;
            row.hidden = !visible;

            if (visible) {
                visibleCount++;
                groupVisibleCounts[rowDomain] = (groupVisibleCounts[rowDomain] || 0) + 1;
            }
        });

        groups.forEach(function (group) {
            var code = group.getAttribute('data-domain-group') || '';
            var groupCount = groupVisibleCounts[code] || 0;
            group.hidden = groupCount === 0;
            var countEl = group.querySelector('[data-domain-count]');
            if (countEl) countEl.textContent = String(groupCount);
        });

        var allPill = domainPills ? domainPills.querySelector('[data-domain=""]') : null;
        if (allPill) {
            var allCount = allPill.querySelector('.pill-count');
            if (allCount) allCount.textContent = String(visibleCount);
        }

        if (domainPills) {
            domainPills.querySelectorAll('.filter-pill[data-domain]').forEach(function (pill) {
                var dc = pill.getAttribute('data-domain');
                if (!dc) return;
                var cnt = pill.querySelector('.pill-count');
                if (cnt) cnt.textContent = String(groupVisibleCounts[dc] || 0);
            });
        }

        if (emptyState) emptyState.hidden = visibleCount > 0;
        if (resultsEl) resultsEl.hidden = visibleCount === 0;
    }
})();
