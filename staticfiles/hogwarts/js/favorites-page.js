async function loadFavorites() {
    const favorites = JSON.parse(localStorage.getItem('favorites')) || [];
    const response = await fetch("https://hp-api.onrender.com/api/characters");
    const all = await response.json();
    const filtered = all.filter(c => favorites.includes(c.name)); 
    const container = document.getElementById('favorites-list');
    container.innerHTML = '';

    if (filtered.length === 0) {
        container.innerHTML = '<p>No favorites yet.</p>';
        return;
    }

    filtered.forEach(char => {
        const html = `
            <div style="margin-bottom: 20px;">
                <h3><a href="/characters/${char.name.toLowerCase().replaceAll(' ', '-')}">${char.name}</a></h3>
                <p>House: ${char.house || 'Unknown'} | Patronus: ${char.patronus || 'None'}</p>
                ${char.image ? `<img src="${char.image}" width="120">` : ''}
                <br>
                <button onclick="removeFavorite('${char.name}')">Remove from Favorites</button>
            </div>
            <hr>
        `;
        container.innerHTML += html;
    });
}

function removeFavorite(name) {
    let favorites = JSON.parse(localStorage.getItem('favorites')) || [];
    favorites = favorites.filter(fav => fav !== name);
    localStorage.setItem('favorites', JSON.stringify(favorites));
    loadFavorites();  
}

document.addEventListener('DOMContentLoaded', loadFavorites);
