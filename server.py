from datetime import datetime, timedelta
import json
import requests
from flask import Flask, request, Response
from flask_cors import CORS,  cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
@cross_origin(origin='*')
def myMainFunction():
    try:
        
        client_json_data = request.json
        weatherList = getWeather(client_json_data)
        # Returns the weather information that was requested
        return Response(json.dumps(weatherList), mimetype='application/json')
    except Exception as e:
        print(e)

def getWeather(client_json_data):

    # Gets latitude and longetude from the map.js
    lat = client_json_data['lat']
    lng = client_json_data['lng']
    location = str(lat) + "," + str(lng)

    #contact the weather service

    url = "https://api.tomorrow.io/v4/timelines"

    # Specifies the data that is to be displayed
    querystring = {
    "location":location,
    "fields":["temperature", "cloudCover", "windSpeed", "windDirection"],
    "units":"metric",
    "timesteps":"1h",
    "apikey":"2epJw1hAMurvBgSAj4gtVE3rFBbDvGM5",
    "timezone":"Africa/Johannesburg"
    }

    headers = {"Accept": "application/json"}

    response = requests.request("GET", url, params=querystring)

    results = response.json()['data']['timelines'][0]['intervals']
    counter = 0
    weatherList = []

    # Goes trough all the data recieved from Tomorrow.io
    for hourly_results in results:
        date = hourly_results['startTime'][0:10]
        time = hourly_results['startTime'][11:19]
        temp = round(hourly_results['values']['temperature'])
        cloud = round(hourly_results['values']['cloudCover'])
        spd = hourly_results['values']['windSpeed']
        direction = round(hourly_results['values']['windDirection'])
        
        # Formats the Cloud Cover data
        if cloud <= 12.5:
            cloud_cover = "Clear"
        elif cloud <= 37.5:
            cloud_cover = "Mostly clear"
        elif cloud <= 62.5:
            cloud_cover = "Partly cloudy"
        elif cloud <= 87.5:
            cloud_cover = "Mostly cloudy"
        else:
            cloud_cover = "Cloudy"

        # Formats the Wind Direction data
        if direction <= 22.5 or direction >= 337.5:
            wind_direction = "North"
        elif direction <= 67.5:
            wind_direction = "North-East"
        elif direction <= 112.5:
            wind_direction = "East"
        elif direction <= 157.5:
            wind_direction = "South-East"
        elif direction <= 202.5:
            wind_direction = "South"
        elif direction <= 247.5:
            wind_direction = "South-West"
        elif direction <= 292.5:
            wind_direction = "West"
        else:
            wind_direction = "North-West"

        # Changes the Wind Speed data from meters per second to miles per hour
        mph = spd * 2.23694
        mph = "{:.2f}".format(mph)

        # Appends data into a list to be sent back to the ajax function
        weatherList.append({
                            "date":date,
                            "time":time,
                            "temprature":temp,
                            "cloudCover":cloud_cover,
                            "windSpeed":mph,
                            "windDirection":wind_direction
                            })

        # Makes sure that there are just 12 sets of data
        if counter == 11:
            break
        else:
            counter += 1

    # Sends the weather list back to the main function
    return weatherList

if __name__ == "__main__":
    app.run()