'use strict'

###*
 # @ngdoc function
 # @name restoApp.controller:MainCtrl
 # @description
 # # MainCtrl
 # Controller of the restoApp
###
angular.module 'restoApp'
    .controller 'RestaurantsCtrl', ($scope, $http) ->
        $scope.update = (url) ->
            $http.get(url)
            .success (response) ->
                $scope.response = response
                $scope.restaurants = response.results
        $scope.next = ->
            if $scope.response and $scope.response.next
                $scope.update $scope.response.next
        $scope.previous = ->
            if $scope.response and $scope.response.previous
                $scope.update $scope.response.previous
        $scope.showDetails = (restaurant) ->
            $scope.details = restaurant
        $scope.update 'http://localhost:8000/restaurants/restaurants/'
