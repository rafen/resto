'use strict'

###*
 # @ngdoc function
 # @name restoApp.controller:AboutCtrl
 # @description
 # # AboutCtrl
 # Controller of the restoApp
###
angular.module 'restoApp'
  .controller 'AboutCtrl', ($scope) ->
    $scope.awesomeThings = [
      'HTML5 Boilerplate'
      'AngularJS'
      'Karma'
    ]
