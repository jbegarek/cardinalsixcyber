(function () {
    var SOURCES = ['BleepingComputer', 'Dark Reading', 'The Hacker News', 'The Record', 'SecurityWeek', 'Krebs on Security', 'CISA Alerts', 'NVD', 'CVE Feed', 'CVE Newsroom'];
    var feedEl = document.getElementById('newsFeed');
    var pillsEl = document.getElementById('filterPills');
    var updatedEl = document.getElementById('newsUpdated');
    var allArticles = [];
    var activeSource = null;

    function escapeHtml(str) {
        if (!str) return '';
        var div = document.createElement('div');
        div.appendChild(document.createTextNode(str));
        return div.innerHTML;
    }
    function relativeTime(dateStr) {
        var now = new Date(); var then = new Date(dateStr);
        var diffSec = Math.floor((now - then) / 1000);
        var diffMin = Math.floor(diffSec / 60);
        var diffHr = Math.floor(diffMin / 60);
        var diffDay = Math.floor(diffHr / 24);
        if (diffSec < 60) return 'just now';
        if (diffMin < 60) return diffMin + 'm ago';
        if (diffHr < 24) return diffHr + 'h ago';
        if (diffDay === 1) return 'yesterday';
        if (diffDay < 7) return diffDay + 'd ago';
        if (diffDay < 30) return Math.floor(diffDay / 7) + 'w ago';
        return then.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
    }
    var arrowSvg = '<svg class="article-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>';

    function renderPills(articles) {
        var counts = {}; articles.forEach(function (a) { counts[a.source] = (counts[a.source] || 0) + 1; });
        var html = '<button class="filter-pill active" data-source="" aria-pressed="true">All <span class="pill-count">' + articles.length + '</span></button>';
        SOURCES.forEach(function (src) {
            if (counts[src]) html += '<button class="filter-pill" data-source="' + escapeHtml(src) + '" aria-pressed="false">' + escapeHtml(src) + ' <span class="pill-count">' + counts[src] + '</span></button>';
        });
        pillsEl.innerHTML = html;
        pillsEl.querySelectorAll('.filter-pill').forEach(function (pill) {
            pill.addEventListener('click', function () {
                pillsEl.querySelectorAll('.filter-pill').forEach(function (p) {
                    p.classList.remove('active');
                    p.setAttribute('aria-pressed', 'false');
                });
                pill.classList.add('active');
                pill.setAttribute('aria-pressed', 'true');
                activeSource = pill.getAttribute('data-source') || null;
                renderFeed(filterArticles());
            });
        });
    }
    function filterArticles() { return activeSource ? allArticles.filter(function (a) { return a.source === activeSource; }) : allArticles; }
    function renderFeatured(article) {
        return '<article class="featured-article reveal"><div class="featured-meta"><span class="badge-latest">Latest</span><span class="badge-source">' + escapeHtml(article.source) + '</span><span class="badge-time">' + escapeHtml(relativeTime(article.published)) + '</span></div><h2 class="featured-title">' + escapeHtml(article.title) + '</h2><p class="featured-summary">' + escapeHtml(article.summary) + '</p><a href="' + escapeHtml(article.link) + '" class="featured-link" target="_blank" rel="noopener noreferrer">Read Article <span aria-hidden="true">&rarr;</span></a></article>';
    }
    function renderRow(article) {
        return '<a href="' + escapeHtml(article.link) + '" class="article-row" target="_blank" rel="noopener noreferrer"><div class="article-body"><div class="article-meta"><span class="badge-source">' + escapeHtml(article.source) + '</span><span class="badge-time">' + escapeHtml(relativeTime(article.published)) + '</span></div><h3 class="article-title">' + escapeHtml(article.title) + '</h3><p class="article-summary">' + escapeHtml(article.summary) + '</p></div>' + arrowSvg + '</a>';
    }
    function renderFeed(articles) {
        if (!articles || articles.length === 0) {
            feedEl.innerHTML = '<div class="news-empty"><svg class="news-empty-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 8v4"/><circle cx="12" cy="16" r="0.5" fill="currentColor"/></svg><h3>No Articles Found</h3><p>No articles match the selected filter. Try selecting a different source or check back later.</p></div>';
            return;
        }
        var html = renderFeatured(articles[0]);
        if (articles.length > 1) { html += '<div class="article-list">'; for (var i = 1; i < articles.length; i++) html += renderRow(articles[i]); html += '</div>'; }
        feedEl.innerHTML = html;
        feedEl.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('visible'); });
    }
    function renderError() {
        feedEl.innerHTML = '<div class="news-empty"><svg class="news-empty-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M15 9l-6 6M9 9l6 6"/></svg><h3>Feed Unavailable</h3><p>Unable to load the news feed at this time. Please try again later.</p></div>';
    }

    fetch('https://raw.githubusercontent.com/jbegarek/cardinalsixcyber/main/data/news.json')
        .then(function (res) { if (!res.ok) throw new Error('HTTP ' + res.status); return res.json(); })
        .then(function (data) {
            allArticles = data.articles || [];
            feedEl.setAttribute('aria-busy', 'false');
            renderPills(allArticles);
            renderFeed(allArticles);
            if (data.last_updated) {
                var d = new Date(data.last_updated);
                updatedEl.textContent = 'Last updated: ' + d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }) + ' at ' + d.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
            }
        })
        .catch(function (err) { console.error('News feed error:', err); feedEl.setAttribute('aria-busy', 'false'); renderError(); });
})();
