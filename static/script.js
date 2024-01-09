const villeInput = document.getElementById('villeInput');
const suggestionsBox = document.getElementById('suggestionsBox');
const quartierSelect = document.getElementById('quartierSelect');
const showPriceBtn = document.getElementById('showPriceBtn');
const priceDisplay = document.getElementById('priceDisplay');
const token = await getToken('admin', 'password');


villeInput.addEventListener('input', function() {
    if (!villeInput.value) {
        suggestionsBox.innerHTML = '';
        suggestionsBox.classList.add('hidden');
        return;
    }

    fetch(`/api/v1/villes/${villeInput.value}`, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`
        }})
        .then(response => response.json())
        .then(data => {
            suggestionsBox.innerHTML = data.map(city => `<div class="suggestion-item cursor-pointer p-2 hover:bg-gray-200">${city}</div>`).join('');
            suggestionsBox.classList.remove('hidden');
            document.querySelectorAll('.suggestion-item').forEach(item => {
                item.addEventListener('click', function() {
                    villeInput.value = this.textContent;
                    suggestionsBox.classList.add('hidden');
                    populateQuartiers(this.textContent);
                });
            });
        });
});

function populateQuartiers(cityName) {
    fetch(`/api/v1/quartiers/villes/${cityName}`,{
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`
        }})
        .then(response => response.json())
        .then(data => {
            quartierSelect.innerHTML = data.map(quartier => `<option>${quartier}</option>`).join('');
        });
}

showPriceBtn.addEventListener('click', function() {
    const selectedQuartier = quartierSelect.value;
    if (selectedQuartier) {
        fetch(`/api/v1/prices/ville/${villeInput.value}/quartier/${selectedQuartier}`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`
            }})
            .then(response => response.json())
            .then(price => {
                priceDisplay.textContent = `Price: ${price}`;
            });
    }
});

document.addEventListener('click', function(event) {
    if (event.target !== villeInput) {
        suggestionsBox.classList.add('hidden');
    }
});

async function getToken(username, password) {
    
    const response = await fetch('/api/v1/token', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    });
    
    if (!response.ok) {
        throw new Error('Authentication failed');
    }

    const data = await response.json();
    return data.access_token;
}