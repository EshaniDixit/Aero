from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load the air quality data from a CSV file
air_quality_data = pd.read_csv('city_day.csv')

# Function to predict air quality based on the city
def predict_air_quality(city):
    # Normalize the input city name for case-insensitive comparison
    normalized_city = city.strip().lower()

    # Search for the city in the DataFrame
    city_data = air_quality_data[air_quality_data['City'].str.lower() == normalized_city]

    if not city_data.empty:
        # Aggregate the air quality parameters (take the mean of the non-null values for each parameter)
        aggregated_data = city_data[['PM2.5', 'PM10', 'NO2', 'O3', 'AQI']].mean()
        return {
            'City': city_data.iloc[0]['City'],
            'PM2.5': aggregated_data['PM2.5'] if pd.notnull(aggregated_data['PM2.5']) else 0.0,
            'PM10': aggregated_data['PM10'] if pd.notnull(aggregated_data['PM10']) else 0.0,
            'NO2': aggregated_data['NO2'] if pd.notnull(aggregated_data['NO2']) else 0.0,
            'O3': aggregated_data['O3'] if pd.notnull(aggregated_data['O3']) else 0.0,
            'AQI': aggregated_data['AQI'] if pd.notnull(aggregated_data['AQI']) else 0.0
        }
    else:
        # If the city is not found, return a message or default values
        return {
            'City': city,
            'PM2.5': float('nan'),
            'PM10': float('nan'),
            'NO2': float('nan'),
            'O3': float('nan'),
            'AQI': float('nan')
        }
def get_health_recommendations(aqi):
    if aqi <= 50:
        return "Air quality is good. Enjoy outdoor activities!", "GOOD"
    elif aqi <= 100:
        return "Air quality is moderate. It's okay to be outdoors.","Moderate"
    elif aqi <= 150:
        return "Unhealthy for sensitive groups. Limit outdoor activities.","Unhealthy for sensitive groups"
    elif aqi <= 200:
        return "Unhealthy. Everyone should reduce outdoor activities.","Unhealthy"
    elif aqi <= 300:
        return "Very Unhealthy. Stay indoors and use air filters.","VERY Unhealthy"
    else:
        return "Hazardous. Avoid all outdoor activities!","HAZARDOUS"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    city = request.form['city']
    air_quality_data = predict_air_quality(city)

    if pd.notnull(air_quality_data['PM2.5']):  # or air_quality_data['AQI'] is not None
        latest_aqi = air_quality_data['AQI']
        recommendation, air_quality_status = get_health_recommendations(latest_aqi)
        return render_template('result.html', data=air_quality_data, aqi=latest_aqi, recommendation=recommendation, air_quality_status=air_quality_status)
    else:
        return render_template('result.html', data=None, aqi=None, recommendation="City not found.", air_quality_status=None)


if __name__ == '__main__':
    app.run(debug=True)
