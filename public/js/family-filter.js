/* Shared filter script for NIST 800-171 and NIST 800-53 pages.
   Expects: #familyPills, #searchInput, .family-group[data-family-group],
   .row[data-family]/[data-search], #emptyState, #requirementResults or #controlResults. */
(function () {
    var activeFamily = '';
    var searchQuery = '';

    var familyPills = document.getElementById('familyPills');
    var searchInput = document.getElementById('searchInput');
    var groups = document.querySelectorAll('.family-group');
    var rows = document.querySelectorAll('.requirement-row, .control-row');
    var emptyState = document.getElementById('emptyState');
    var resultsEl = document.getElementById('requirementResults') || document.getElementById('controlResults');

    if (familyPills) {
        familyPills.addEventListener('click', function (e) {
            var pill = e.target.closest('.filter-pill');
            if (!pill) return;
            familyPills.querySelectorAll('.filter-pill').forEach(function (p) {
                p.classList.remove('active');
                p.setAttribute('aria-pressed', 'false');
            });
            pill.classList.add('active');
            pill.setAttribute('aria-pressed', 'true');
            activeFamily = pill.getAttribute('data-family') || '';
            applyFilters();
        });
    }

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
            var rowFamily = row.getAttribute('data-family') || '';
            var rowSearch = row.getAttribute('data-search') || '';
            var familyMatch = !activeFamily || rowFamily === activeFamily;
            var searchMatch = !searchQuery || rowSearch.indexOf(searchQuery) !== -1;
            var visible = familyMatch && searchMatch;
            row.hidden = !visible;
            if (visible) {
                visibleCount++;
                groupVisibleCounts[rowFamily] = (groupVisibleCounts[rowFamily] || 0) + 1;
            }
        });

        groups.forEach(function (group) {
            var code = group.getAttribute('data-family-group') || '';
            var groupCount = groupVisibleCounts[code] || 0;
            group.hidden = groupCount === 0;
            var countEl = group.querySelector('[data-family-count]');
            if (countEl) countEl.textContent = String(groupCount);
        });

        var allPill = familyPills ? familyPills.querySelector('[data-family=""]') : null;
        if (allPill) {
            var allCount = allPill.querySelector('.pill-count');
            if (allCount) allCount.textContent = String(visibleCount);
        }

        if (familyPills) {
            familyPills.querySelectorAll('.filter-pill[data-family]').forEach(function (pill) {
                var fc = pill.getAttribute('data-family');
                if (!fc) return;
                var cnt = pill.querySelector('.pill-count');
                if (cnt) cnt.textContent = String(groupVisibleCounts[fc] || 0);
            });
        }

        if (emptyState) emptyState.hidden = visibleCount > 0;
        if (resultsEl) resultsEl.hidden = visibleCount === 0;
    }
})();
