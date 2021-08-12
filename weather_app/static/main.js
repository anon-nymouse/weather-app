function geolocate() { 
    if('geolocation' in navigator) {
        /* geolocation is available */
        console.log('Geolocation is available');
        navigator.geolocation.getCurrentPosition((position) => {
            let lat = position.coords.latitude;
            let lon = position.coords.longitude;
          console.log(lat, lon);
          get_wdata(lat, lon);
        });
      } else {
        /* geolocation IS NOT available */
        console.log('Geolocation is not available')
    }
}

async function get_wdata(lat, lon) {
    const data = await fetch(`127.0.0.1/get_weather?lat=${lat}&lon=${lon}`);
    console.log(data.body);
  }
