document.addEventListener('DOMContentLoaded', function() {
    const villeInput = document.getElementById('villeInput');
    const suggestionsBox = document.createElement('div');
    const quartierSelect = document.getElementById('quartierSelect');
    const showPriceBtn = document.getElementById('showPriceBtn');
    const priceDisplay = document.getElementById('priceDisplay');

    suggestionsBox.classList.add('border', 'p-2', 'mt-2', 'bg-white', 'absolute', 'w-full');
    villeInput.parentNode.insertBefore(suggestionsBox, villeInput.nextSibling);

    function populateQuartiers(cityName) {
        fetch(`/villes/name/${cityName}/quartiers`)
            .then(response => response.json())
            .then(data => {
                quartierSelect.innerHTML = data.map(quartier => `<option>${quartier}</option>`).join('');
            });
    }

    villeInput.addEventListener('input', function() {
        if (!villeInput.value) {
            suggestionsBox.innerHTML = '';
            return;
        }

        fetch(`/villes/name/${villeInput.value}`)
            .then(response => response.json())
            .then(data => {
                suggestionsBox.innerHTML = data.map(city => `<div class="suggestion-item cursor-pointer p-2 hover:bg-gray-200">${city}</div>`).join('');
                document.querySelectorAll('.suggestion-item').forEach(item => {
                    item.addEventListener('click', function() {
                        villeInput.value = this.textContent;
                        suggestionsBox.innerHTML = '';
                        populateQuartiers(this.textContent);
                    });
                });
            });
    });

    showPriceBtn.addEventListener('click', function() {
        const selectedQuartier = quartierSelect.value;
        if (selectedQuartier) {
            fetch(`/villes/name/${villeInput.value}/quartiers/${selectedQuartier}/price`)
                .then(response => response.json())
                .then(price => {
                    priceDisplay.textContent = `Price: ${price}`;
                });
        }
    });

    document.addEventListener('click', function(event) {
        if (event.target !== villeInput) {
            suggestionsBox.innerHTML = '';
        }
    });
});
