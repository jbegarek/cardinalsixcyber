(function () {
    var laneButtons = Array.prototype.slice.call(document.querySelectorAll('[data-filter-kind="lane"]'));
    var topicButtons = Array.prototype.slice.call(document.querySelectorAll('[data-filter-kind="topic"]'));
    var featuredCard = document.querySelector('#featuredWrap .blog-post-card');
    var feedCards = Array.prototype.slice.call(document.querySelectorAll('#feedGrid .blog-post-card'));
    var featuredWrap = document.getElementById('featuredWrap');
    var feedWrap = document.getElementById('feedWrap');
    var stateEl = document.getElementById('blogIndexState');

    if (!featuredCard && !feedCards.length) {
        if (featuredWrap) featuredWrap.hidden = true;
        if (stateEl) stateEl.hidden = false;
        return;
    }

    var filters = { lane: 'all', topic: 'all' };

    function setActive(buttons, activeValue) {
        buttons.forEach(function (button) {
            var isActive = button.dataset.filterValue === activeValue;
            button.classList.toggle('is-active', isActive);
            button.setAttribute('aria-pressed', isActive ? 'true' : 'false');
        });
    }

    function matchesFilters(card) {
        var lane = (card.dataset.lane || '').toLowerCase();
        var topics = (card.dataset.topics || '').split('|').filter(Boolean);
        var laneMatches = filters.lane === 'all' || lane === filters.lane;
        var topicMatches = filters.topic === 'all' || topics.indexOf(filters.topic) !== -1;
        return laneMatches && topicMatches;
    }

    function render() {
        var featuredMatches = featuredCard ? matchesFilters(featuredCard) : false;
        var matchedFeedCards = feedCards.filter(matchesFilters);
        var matchedCount = matchedFeedCards.length + (featuredMatches ? 1 : 0);

        if (featuredCard) featuredCard.hidden = !featuredMatches;

        feedCards.forEach(function (card) {
            card.hidden = matchedFeedCards.indexOf(card) === -1;
        });

        if (featuredWrap) featuredWrap.hidden = !featuredMatches;
        if (feedWrap) feedWrap.hidden = matchedFeedCards.length === 0;
        if (stateEl) stateEl.hidden = matchedCount > 0;
    }

    laneButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            filters.lane = button.dataset.filterValue || 'all';
            setActive(laneButtons, filters.lane);
            render();
        });
    });

    topicButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            filters.topic = button.dataset.filterValue || 'all';
            setActive(topicButtons, filters.topic);
            render();
        });
    });

    render();
})();
