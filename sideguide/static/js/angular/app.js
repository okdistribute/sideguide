var app = angular.module("Sideguide", ["google-maps"], function ($interpolateProvider) {
    $interpolateProvider.startSymbol('((');
    $interpolateProvider.endSymbol('))');
});
