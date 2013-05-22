'use strict';

/* Controllers */

angular.module('sideguide.controllers', [])
    .controller('IndexControl', [function() {


    }])
    .controller('UserControl', [function() {

    }])
    .controller('FrameController', [function($scope) {
        $scope.toggleMenu = function() {
            $scope.menuopen = !$scope.menuopen;
        }
    }]);
