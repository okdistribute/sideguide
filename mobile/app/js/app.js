'use strict';


// Declare app level module which depends on filters, and services
var app = angular.module('sideguide',
       ['ajoslin.mobile-navigate',
        'sideguide.filters',
        'sideguide.services',
        'sideguide.directives',
        'sideguide.controllers']
);

app.config(function($routeProvider) {
  $routeProvider
      .when("/", {
        templateUrl: "index.html",
        controller: 'IndexControl'
      })
      .when("/m/:user", {
        templateUrl: "partials/user.html",
        controller: 'OrganizationControl'
      })
      .when("/m/:user/:coll", {
        templateUrl: "partials/collection.html",
        controller: 'CollectionControl'
      })
      .when("/m/:user/:coll/:item", {
        templateUrl: "partials/item.html",
        controller: 'ItemControl'
      })
      .otherwise({
        redirectTo: "/"
      });
});

app.run(function($route, $http, $templateCache) {
  angular.forEach($route.routes, function(r) {
    if (r.templateUrl) {
      $http.get(r.templateUrl, {cache: $templateCache});
    }
  });
})


app.directive('ngTap', function() {
    var isTouchDevice = !!("ontouchstart" in window);
    return function(scope, elm, attrs) {
        if (isTouchDevice) {
            var tapping = false;
            elm.bind('touchstart', function() { tapping = true; });
            elm.bind('touchmove', function() { tapping = false; });
            elm.bind('touchend', function() {
                tapping && scope.$apply(attrs.ngTap);
            });
        } else {
            elm.bind('click', function() {
                scope.$apply(attrs.ngTap);
            });
        }
    };
});