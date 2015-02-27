'use strict'

###*
 # @ngdoc function
 # @name restoApp.controller:MainCtrl
 # @description
 # # MainCtrl
 # Controller of the restoApp
###
angular.module 'restoApp'
    .controller 'RestaurantsCtrl', ($scope, $http, $location, $anchorScroll, $cookies) ->

        # Get current User
        $scope.getCurrentUser = ->
            $http.get('http://localhost:8000/restaurants/current-user/')
                .success (response) ->
                    $scope.user = response
                .error (data, status, headers, config) ->
                    $scope.user = null

        # Restaurants Pagination update
        $scope.update = (url) ->
            $http.get(url)
                .success (response) ->
                    $scope.response = response
                    $scope.restaurants = response.results
                    # by default fill the first restaurant in the detail section
                    if response.results.length > 0
                        $scope.details = response.results[0]

        # Restaurant Next page
        $scope.next = ->
            if $scope.response and $scope.response.next
                $scope.update $scope.response.next

        # Restaurant Previous page
        $scope.previous = ->
            if $scope.response and $scope.response.previous
                $scope.update $scope.response.previous

        # Show Restaurant details
        $scope.showDetails = (restaurant) ->
            $scope.details = restaurant
            $location.hash 'restaurant-details'
            $anchorScroll()

        # Show Search results
        $scope.gotoSearch = ->
            $location.hash 'restaurant-search'
            $anchorScroll()

        $scope.vote = (v) ->
            url = 'http://localhost:8000/restaurants/vote/'+$scope.details.id+'/'
            $http.put(url, {'vote': v})
                .success (response) ->
                    $scope.details.votes = response.votes

        # Thumbs up for selected restaurant
        $scope.voteUp = ->
            $scope.vote true

        # Thumbs up for selected restaurant
        $scope.voteDown = ->
            $scope.vote false

        # Store user visit
        $scope.visit = ->
            url = 'http://localhost:8000/restaurants/visits/'
            $http.post(url, {'user': $scope.user.id, 'restaurant': $scope.details.id})
                .success (response) ->
                    response['user'] = $scope.user
                    $scope.details.visitors.push(response)


        # Add csrf token in http methods
        $http.defaults.headers.put['X-CSRFToken'] = $cookies.csrftoken
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken
        $http.defaults.withCredentials = true
        # Load Initial data of the table
        $scope.update 'http://localhost:8000/restaurants/restaurants/'
        # Get current user
        $scope.getCurrentUser()
