# WeatherMap Project

This project is a weather application that displays weather information for any location clicked on a Google map. The application consists of a Python backend and an HTML/CSS/JavaScript frontend. The frontend sends location coordinates to the backend, which then fetches and returns weather data from the Tomorrow.io API.

## Table of Contents
- [File Structure](#file-structure)
- [App Overview](#app-overview)
- [Backend](#backend)
- [Frontend](#frontend)
- [Setup](#setup)
- [Usage](#usage)
- [Author](#author)

## File Structure

Create a folder called `WeatherMap` in which to keep your project files.

- `WeatherMap/`
  - `server.py` (Backend file)
  - `client.html` (Frontend HTML file)
  - `styles.css` (Optional: Separate CSS file)
  - `scripts.js` (Optional: Separate JavaScript file)

## App Overview

The application workflow is as follows:
1. The user clicks on a location on the Google map displayed in the browser.
2. A listener function extracts the latitude and longitude coordinates of the clicked location.
3. The coordinates are sent to the Python backend using a jQuery Ajax function.
4. The backend fetches the latest weather information for the specified coordinates from the Tomorrow.io API.
5. The backend sends the weather information for the next 12 hours back to the frontend.
6. The frontend displays the weather information under the map.

## Backend

The backend is a Python script (`server.py`) that handles requests from the frontend and interacts with the Tomorrow.io API to fetch weather data.

### Steps:
1. **API Key**: Register on Tomorrow.io to get an API key.
2. **Server Request Handling**: Receive coordinates from the frontend.
3. **API Request**: Use the coordinates to request weather data from Tomorrow.io.
4. **Data Extraction**: Extract relevant weather data (date, time, temperature, cloud cover, wind speed, wind direction) for the next 12 hours.
5. **Time Adjustment**: Convert times from UTC to GMT+2 (South African time).
6. **Response**: Send the weather data back to the frontend as a JSON object.

### Example API Code:
Refer to [this guide](https://www.tomorrow.io/blog/creating-daily-forecasts-with-a-python-weather-api/) for generating Python code to access the weather API.

## Frontend

The frontend consists of HTML, CSS, and JavaScript. The main file is `client.html`, which can optionally link to separate `styles.css` and `scripts.js` files.

### Steps:
1. **Display Map**: Use the Google Maps API to display a map in the browser.
2. **Map Click Listener**: Add a listener to capture click events on the map and extract coordinates.
3. **Ajax Request**: Send coordinates to the backend using a jQuery Ajax function.
4. **Display Weather Data**: Receive weather data from the backend and update the page with the information.

### Google Maps Setup:
- Visit [Google Maps JavaScript API](https://developers.google.com/maps/documentation/javascript/examples/map-simple) for map display code.
- Add a `div` with `id="map"` in the `client.html` file for displaying the map.
- Add a `div` with `id="weather"` to display weather information.

### Map Click Listener:
- Use the example from [Google Maps Event Click](https://developers.google.com/maps/documentation/javascript/examples/event-click-latlng#maps_event_click_latlng-javascript) to add a click listener.
- Extract coordinates and send them to the backend using jQuery Ajax.

### Weather Display:
- Update the `#weather` div with the weather data using jQuery.

## Setup

1. **Clone the repository**:
```bash
   git clone https://github.com/Tertius-Denis-Liebenberg/Weather-Map-e-commerce-website.git
```

2. Navigate to the project directory:
```bash
    cd WeatherMap
```


3. Install dependencies (if any, such as Flask for Python):
```bash
    pip install Flask
```

4. Run the backend server:
```bash
    python server.py
```

5. Open 'client.html' in your web browser.

## Usage

1. Open `client.html` in a web browser to view the Google map.
2. Click on any location on the map to get weather information for that location.
3. The weather information for the next 12 hours will be displayed below the map.

## Author

**Tertius Denis Liebenberg**  

For any questions or feedback, please contact [tertiusliebenberg7@gmail.com].