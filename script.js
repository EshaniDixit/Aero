document.getElementById('predict-btn').addEventListener('click', function () {
    const cityInput = document.getElementById('city').value.trim();
    const resultContainer = document.getElementById('result');

    // Clear previous results and validate input
    clearPreviousResults(resultContainer);

    if (!cityInput) {
        showError(resultContainer, 'Please enter a valid city name.');
        return;
    }

    // Show a loading spinner while fetching the data
    showLoading(resultContainer);

    // Fetch air quality prediction for the entered city
    fetch(`/predict?city=${encodeURIComponent(cityInput)}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response failed.');
            }
            return response.json();
        })
        .then(data => {
            if (!data || !data.aqi) {
                throw new Error('Invalid data received from the server.');
            }
            displayResult(data, resultContainer);
        })
        .catch(error => {
            console.error('Error fetching air quality data:', error);
            showError(resultContainer, 'Could not fetch air quality data. Please try again.');
        });
});

// Function to clear previous results from the result container
function clearPreviousResults(resultContainer) {
    resultContainer.innerHTML = '';
}

// Function to show a loading spinner
function showLoading(resultContainer) {
    resultContainer.innerHTML = `
        <div class="alert alert-info">
            <div class="spinner-border spinner-border-sm" role="status"></div>
            Fetching air quality data...
        </div>
    `;
}

// Function to display error message
function showError(resultContainer, message) {
    resultContainer.innerHTML = `
        <div class="alert alert-danger">${message}</div>
    `;
}

// Function to display air quality result
function displayResult(data, resultContainer) {
    const { aqi, city } = data;
    const airQuality = getAirQualityDescription(aqi);
    const badgeClass = getBadgeClass(aqi);

    const resultCard = `
        <div class="card text-center">
            <div class="card-header">
                Air Quality Index for ${city}
            </div>
            <div class="card-body">
                <h5 class="card-title">${aqi}</h5>
                <p class="card-text">
                    <span class="badge ${badgeClass}">${airQuality}</span>
                </p>
            </div>
        </div>
    `;

    resultContainer.innerHTML = resultCard;
}

// Function to determine the air quality description based on AQI
function getAirQualityDescription(aqi) {
    if (aqi <= 50) return "Good";
    if (aqi <= 100) return "Moderate";
    if (aqi <= 150) return "Unhealthy for Sensitive Groups";
    if (aqi <= 200) return "Unhealthy";
    if (aqi <= 300) return "Very Unhealthy";
    return "Hazardous";
}

// Function to get the corresponding badge class for AQI
function getBadgeClass(aqi) {
    if (aqi <= 50) return "badge-success";
    if (aqi <= 100) return "badge-warning";
    if (aqi <= 150) return "badge-danger";
    if (aqi <= 200) return "badge-danger";
    if (aqi <= 300) return "badge-dark";
    return "badge-dark";
}

