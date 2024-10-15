# Aero Predict

This project is a web application that continuously monitors air quality across a city, predicts pollution levels based on historical data, and provides actionable measures to mitigate poor air quality. The app uses a machine learning model to predict the Air Quality Index (AQI) and display the current air quality status for different cities.




## Overview
This project is an AI-powered air quality monitoring and prediction system that uses various sensors to collect real-time data on air pollutants and environmental conditions. The system employs Intel optimized libraries, including oneAPI Data Analytics Library (oneDAL) and oneAPI Deep Neural Network Library (oneDNN), for efficient data analysis and AI model performance. The system is designed to predict air quality levels and provide insights for proactive decision-making to improve environmental health and sustainability.
## Features

- Predicts AQI and pollutant levels (PM2.5, PM10, NO2, O3) based on city input
- Displays real-time air quality classification (Good, Moderate, Unhealthy, etc.).
- Visualizes missing data using heatmaps for quality assurance.
- Utilizes a machine learning model trained on historical air quality data.
- Web-based interface built using Flask for easy user interaction.


## Tech Stack

**Frontend:** HTML5, CSS3, Bootstrap, JavaScript

**Backend:** Python, Flask

**Machine Learning:** Scikit-learn, Pandas and NumPy, Sklearn


## How the Model Works

   1. *Data Collection*: The historical data is preprocessed to   handle missing values, outliers, and scaling.
   2. *Feature Selection*: Important features like PM2.5, PM10, NO2, temperature, and humidity are extracted to predict AQI.
   3. *Model Training*: A Random Forest Regressor is trained on the dataset, using features as inputs and AQI as the output.
   4. *Prediction*: Once trained, the model predicts the AQI for new inputs provided by the user.
   5. *Integration*: The model is integrated with Flask, allowing real-time predictions via the web interface.
