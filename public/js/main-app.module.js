var app = angular.module("mainApp", ['ui.router']);

app.config(function($stateProvider, $urlRouterProvider) {

    $stateProvider
        .state('recommandations', {
            url: '/recommandations',
            templateUrl: 'views/recommandations.html'
        })
        .state('default', {
        	url: '',
        	templateUrl: 'views/accueil.html'
        });

});