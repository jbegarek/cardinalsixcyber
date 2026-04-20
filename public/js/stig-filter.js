(function () {
    var filterBtns = document.querySelectorAll('.filter-btn');
    var searchInput = document.getElementById('stig-search');
    var rows = document.querySelectorAll('.rule-row');
    var noResults = document.getElementById('no-results');
    var activeSeverity = 'all';

    function applyFilters() {
        var q = (searchInput && searchInput.value || '').toLowerCase().trim();
        var visible = 0;
        rows.forEach(function (row) {
            var sev = row.dataset.severity || '';
            var searchText = row.dataset.search || '';
            var sevMatch = activeSeverity === 'all' || sev === activeSeverity;
            var textMatch = !q || searchText.indexOf(q) !== -1;
            var show = sevMatch && textMatch;
            row.hidden = !show;
            if (show) visible++;
        });
        if (noResults) noResults.hidden = visible > 0;
    }

    filterBtns.forEach(function (btn) {
        btn.addEventListener('click', function () {
            filterBtns.forEach(function (b) { b.classList.remove('active'); });
            btn.classList.add('active');
            activeSeverity = btn.dataset.filter || 'all';
            applyFilters();
        });
    });

    if (searchInput) searchInput.addEventListener('input', applyFilters);
})();
