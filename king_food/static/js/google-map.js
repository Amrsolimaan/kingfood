function init() {
    // إحداثيات القاهرة
    var myLatlng = new google.maps.LatLng(29.292753, 31.129623); // استخدم الإحداثيات التي حصلت عليها

    var mapOptions = {
        zoom: 15, // زووم أكبر لرؤية التفاصيل بشكل أفضل
        center: myLatlng,
        scrollwheel: false,
        styles: [
            {
                "featureType": "administrative.country",
                "elementType": "geometry",
                "stylers": [
                    {
                        "visibility": "simplified"
                    },
                    {
                        "hue": "#ff0000"
                    }
                ]
            }
        ]
    };

    var mapElement = document.getElementById('map');
    var map = new google.maps.Map(mapElement, mapOptions);

    var addresses = ['29.292753, 31.129623']; // استخدم الإحداثيات مباشرة هنا

    for (var x = 0; x < addresses.length; x++) {
        $.getJSON('https://maps.googleapis.com/maps/api/geocode/json?latlng=' + encodeURIComponent(addresses[x]) + '&key=AIzaSyB1NGSyRCkAcR68MGdvsv7bXrTgaLQ4EC0', null, function (data) {
            var p = data.results[0].geometry.location;
            var latlng = new google.maps.LatLng(p.lat, p.lng);
            new google.maps.Marker({
                position: latlng,
                map: map,
                icon: 'images/loc.png'
            });
        });
    }
}
