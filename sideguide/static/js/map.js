var style = [{
    "stylers": [{
        "visibility": "off"
    }]
}, {
    "featureType": "road",
    "stylers": [{
        "visibility": "on"
    }, {
        "color": "#ffffff"
    }]
}, {
    "featureType": "road.arterial",
    "stylers": [{
        "visibility": "on"
    }, {
        "color": "#fee379"
    }]
}, {
    "featureType": "road.highway",
    "stylers": [{
        "visibility": "on"
    }, {
        "color": "#fee379"
    }]
}, {
    "featureType": "landscape",
    "stylers": [{
        "visibility": "on"
    }, {
        "color": "#f3f4f4"
    }]
}, {
    "featureType": "water",
    "stylers": [{
        "visibility": "on"
    }, {
        "color": "#7fc8ed"
    }]
}, {}, {
    "featureType": "road",
    "elementType": "labels",
    "stylers": [{
        "visibility": "off"
    }]
}, {
    "featureType": "poi.park",
    "elementType": "geometry.fill",
    "stylers": [{
        "visibility": "on"
    }, {
        "color": "#83cead"
    }]
}, {
    "elementType": "labels",
    "stylers": [{
        "visibility": "off"
    }]
}, {
    "featureType": "landscape.man_made",
    "elementType": "geometry",
    "stylers": [{
        "weight": 0.9
    }, {
        "visibility": "off"
    }]
}]

function draw_map(container, lat, lon) {
    var map;

    var centerPosition = new google.maps.LatLng(lat, lon);
    var options = {
        zoom: 16,
        center: centerPosition,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    map = new google.maps.Map(document.getElementById(container), options);

    map.setOptions({
        styles: style
    });

    return map;
}

function draw_point(map, x, y) {
    var image = {
        url: '/static/img/icons/flat-marker.png',
        origin: new google.maps.Point(x, y),
        anchor: new google.maps.Point(x + 12, y + 59)
    };

    var shadow = {
        url: '/static/img/icons/flat-marker-shadow.png',
        origin: new google.maps.Point(x, y),
        anchor: new google.maps.Point(x -2, y + 36)
    };

    var marker = new google.maps.Marker({
        position: centerPosition,
        map: map,
        icon: image,
        shadow: shadow
    });
}