function toggleFavorite(name) {
    let favorites = JSON.parse(localStorage.getItem('favorites')) || [];
    if (favorites.includes(name)) {
        favorites = favorites.filter(item => item !== name);
    } else {
        favorites.push(name);
    }
    localStorage.setItem('favorites', JSON.stringify(favorites));  // Сохраняем изменения
    updateStar(name);
}

function updateStar(name) {
    const btn = document.getElementById('fav-' + name);
    if (!btn) return;
    const favorites = JSON.parse(localStorage.getItem('favorites')) || [];
    btn.innerText = favorites.includes(name) ? '★ Remove' : '☆ Add to Favorites';
}

function initFavorites() {
    const allButtons = document.querySelectorAll('[id^="fav-"]');
    allButtons.forEach(btn => {
        const name = btn.getAttribute('data-name');
        updateStar(name);
    });
}

document.addEventListener('DOMContentLoaded', initFavorites);