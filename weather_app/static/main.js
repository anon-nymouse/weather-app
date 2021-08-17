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

    let latt = json.latt;
    let lonn = json.lonn;
    let temp = json.temp;
    let feels_like = json.feels_like;
    let humidity = json.humidity;
    let clouds = json.clouds;
    let weather = json.w;
    let des = json.w0;


    document.getElementById('lat').innerHTML = latt;
    document.getElementById('lon').innerHTML = lonn;
    document.getElementById('tmp').innerText = temp;
    document.getElementById('fls').innerText = feels_like;
    document.getElementById('cls').innerHTML = clouds;
    document.getElementById('hum').innerHTML = humidity;
    document.getElementById('weather').innerHTML = weather;
    document.getElementById('des').innerHTML = des;
    document.getElementById('rain').innerHTML = rain;

    // console.log(json);
  }
