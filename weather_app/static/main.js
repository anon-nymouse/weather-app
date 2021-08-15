function geolocate() { 
    if('geolocation' in navigator) {
        /* geolocation is available */
        console.log('Geolocation is available');
        navigator.geolocation.getCurrentPosition((position) => {
            let lat = position.coords.latitude;
            let lon = position.coords.longitude;
          console.log(lat, lon);
          get_wdata(lat, lon)
        });
      } else {
        /* geolocation IS NOT available */
        console.log('Geolocation is not available')
    }
}

async function get_wdata(lat, lon) {
    const data = { lat, lon }
    const options = {
      method: 'POST',
      mode: 'cors', // no-cors, *cors, same-origin
      cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
      credentials: 'same-origin', // include, *same-origin, omit
      headers: {
        'Content-Type': 'application/json'
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      redirect: 'follow', // manual, *follow, error
      referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
      body: JSON.stringify(data)
    }
    const response = await fetch('/get_weather?', options);
    json = await response.json()
    let latitude = json.lat;
    let longitude = json.lon;
    document.getElementById('lat').innerText = latitude;
    document.getElementById('lon').innerText = longitude;
    console.log(latitude, longitude);
  }
