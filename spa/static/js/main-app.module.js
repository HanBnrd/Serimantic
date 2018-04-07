var app = angular.module("mainApp", ['ui.router','ngAnimate']);

app.config(function($stateProvider, $urlRouterProvider) {
    /*
    //we have to change the symbols because both Django & AngularJS use the same characters
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    */

    $stateProvider
        .state('recommendations', {
            url: '/recommendations',
            templateUrl: 'static/views/recommendations.html'
        })
        .state('tvshowcard', {
            url: '/tvshowcard/:tv_show_name/:tmdb_id',
            controller: 'tvShowCardController',
            templateUrl: 'static/views/tvshowcard.html'
        })
        .state('default', {
        	url: '',
        	templateUrl: 'static/views/accueil.html'
        });

});

app.controller('allNames', function($scope, $http) {
    $http.get('/api/tv/all').then(function(response) {
        var tvShowNames = {};
        for(var i = 0; i < response.data.length; i++) {    
            tvShowNames[response.data[i].name] = null;
        }

        $scope.names = tvShowNames;

        $(document).ready(function(){
            $('input.autocomplete').autocomplete({
                data: $scope.names,
                limit: 8
            });
        });
    });
});

app.controller('tvShowCardController', function($scope, $http, $stateParams) {
    var chunk = function (arr, size) {
        var newArr = [];
        for (var i=0; i<arr.length; i+=size) {
            newArr.push(arr.slice(i, i+size));
        }
        return newArr;
    }

    $http.get('/tmdb/'+$stateParams.tmdb_id+'/').then(function(response) {
        $scope.tvShowData = response.data;
    });

    $http.get('api/tag/name/'+$stateParams.tv_show_name+'/').then(function(response) {
        var keywordsArray = [];
        for (var i=0; i<response.data.length; i+=1) {
            keywordsArray.push(response.data[i]["keyword"]);
        }
        $scope.keywords = chunk(keywordsArray, 2);
    });

    $http.get('api/recommendation/'+$stateParams.tv_show_name+'/').then(function(response) {
        $scope.recommendedShow = response.data;
        console.log(response.data);
    });
});


app.controller('submitSearchController', function($http, $scope, $location) {
    $scope.tvShowCard = function () {
        $http.get('/api/tv/name/'+$scope.tvShowName+'/').then(function(response) {
            $location.path('/tvshowcard/'+$scope.tvShowName+'/'+response.data["tmdb_id"]);
        });
    };
});