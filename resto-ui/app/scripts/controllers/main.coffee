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

        restaurantsUrl = 'http://localhost:8000/restaurants/restaurants/'
        $scope.orderingParam = ''
        $scope.searchParam = ''

        # Get current User
        $scope.getCurrentUser = ->
            $http.get('http://localhost:8000/restaurants/current-user/')
                .success (response) ->
                    $scope.user = response
                .error (data, status, headers, config) ->
                    $scope.user =
                        id: 0

        # Search
        $scope.doSearch = ->
            $scope.searchParam = $scope.searchText
            $scope.updateUrl()

        # Ordering
        $scope.doOrdering = (param) ->
            if param != $scope.orderingParam
                $scope.orderingParam = param
            else
                $scope.orderingParam = ''
            $scope.updateUrl()

        # Update Url
        $scope.updateUrl = ->
            $scope.update(restaurantsUrl+'?search='+$scope.searchParam+'&ordering='+$scope.orderingParam)

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
            # Save old Anchor to restore it later
            old = $location.hash()
            $location.hash 'restaurant-details'
            $anchorScroll()
            # After scroll set original anchor
            $location.hash(old)

        # Show Search results
        $scope.gotoSearch = ->
            # Save old Anchor to restore it later
            old = $location.hash()
            $location.hash 'restaurant-search'
            $anchorScroll()
            # After scroll set original anchor
            $location.hash(old)

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
                    $scope.details.visitors.unshift(response)

        # Add comment
        $scope.addComment = (newComment) ->
            url = 'http://localhost:8000/restaurants/comments/'
            $http.post(url,
                'user': $scope.user.id
                'restaurant': $scope.details.id
                'comment': newComment
            ).success (response) ->
                response['user'] = $scope.user
                $scope.details.comments.unshift(response)

        # Set class to comments depending the owner
        $scope.getCommentClass = (comment) ->
            if comment.user.id == $scope.user.id
                return 'panel-info'
            else
                return 'panel-default'

        # Set class to visitors depending the owner
        $scope.getVisitorClass = (visitor) ->
            if visitor.user.id == $scope.user.id
                return 'label-info'
            else
                return 'label-default'


        # Add csrf token in http methods
        $http.defaults.headers.put['X-CSRFToken'] = $cookies.csrftoken
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken
        $http.defaults.withCredentials = true
        # Load Initial data of the table
        $scope.update restaurantsUrl
        # Get current user
        $scope.getCurrentUser()
