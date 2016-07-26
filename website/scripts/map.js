// Initializes the Google Map and retrieves the latitude and longitude enter by the user.
// Then positions the map based on the respective latitude and longitude, thereby placing a marker.
function initMap() {
  var mapDiv = document.getElementById('map');
  var center = new google.maps.LatLng(0, 0);
  var map = new google.maps.Map(mapDiv, {
    center: center, 
    zoom: 2 
  });

  google.maps.event.addDomListener(document.getElementById("latLngForm"), 'submit',
function(e){
    e.preventDefault();

    var lat = document.getElementById('lat').value;
    var lng = document.getElementById('lng').value;
    var mapCenter = new google.maps.LatLng(lat, lng);

    var marker = new google.maps.Marker ({
      position: mapCenter,
      map: map
    });
    map.setCenter(mapCenter);
    map.setZoom(3);
  });  
}
