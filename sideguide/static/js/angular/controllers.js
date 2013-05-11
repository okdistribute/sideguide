function CurateCtrl($scope) {

    angular.extend($scope, {
        center: {
            lat: 0, // initial map center latitude
            lng: 0 // initial map center longitude
        },
        markers: [], // an array of markers,
        zoom: 2
    });
}