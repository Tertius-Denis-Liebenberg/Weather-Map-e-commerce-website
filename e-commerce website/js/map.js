let map;

//creates map
function initMap() {
    const myLatlng = { lat: -25.983038605054464, lng: 28.39041753322593 };
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 4,
        center: myLatlng,
    });

    // Configure the click listener.
    map.addListener("click", (mapsMouseEvent) => {
        let coordinates = JSON.stringify(mapsMouseEvent.latLng.toJSON(), null, 2);

        // Sends coordinate information to server
        $.ajax({
          url: "http://127.0.0.1:5000",
          type: "post",
          data: coordinates,
          dataType: "json",
          contentType: "application/json",
          crossOrigin: true,
          success: function (data) {
              console.log("server", data);
              displayData(data)
          },
          error: function () {
              alert("Something went wrong")
          },
        });
    });
}

// Display weather information in browser
function displayData(data) {
    const dataContainer = $("#displayWeatherInfo");
    let tableHTML = ""
    $.each(data, function (index, item) {

        if (index === 0 || index === 6) {
            tableHTML += "<tr>";
        }

        let icon = "";

        switch(item.windDirection){
            case "North":
                icon = "svg/north.svg"
                break;
            case "North-East":
                icon = "svg/north-east.svg"
                break;
            case "East":
                icon = "svg/east.svg"
                break;
            case "South-East":
                icon = "svg/south-east.svg"
                break;
            case "South":
                icon = "svg/south.svg"
                break;
            case "South-West":
                icon = "svg/south-west.svg"
                break;
            case "West":
                icon = "svg/west.svg"
                break;
            case "North-West":
                icon = "svg/north-west.svg"
                break;
        }

        // Format on how data needs to be displayed
        tableHTML += `
            <td>
                <p>${item.date}  ${item.time}</p>
                <p>Temprature: ${item.temprature} C</p>
                <p>Cloud Cover: ${item.cloudCover}</p>
                <p>Wind Speed: ${item.windSpeed} mph</p>
                <p id="svg">Wind Direction: <img src="${icon}"></p>
            </td>
        `;

        if (index === 5 || index === 11) {
            tableHTML += "</tr>";
        }
    });

    dataContainer.html(tableHTML);

}