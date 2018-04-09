function chunk (arr, size) {
    var newArr = [];
    for (var i=0; i<arr.length; i+=size) {
        newArr.push(arr.slice(i, i+size));
    }
    return newArr;
}


var app = angular.module("mainApp", ['ui.router','ngAnimate']);

app.config(function($stateProvider, $urlRouterProvider) {
    /*
    //we have to change the symbols because both Django & AngularJS use the same characters
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    */

    $stateProvider
        .state('tvshows', {
            url: '/tvshows',
            controller: 'recommendationController',
            templateUrl: 'static/views/tvshows.html'
        })
        .state('discover', {
            url: '/discover',
            controller: 'recommendationController',
            templateUrl: 'static/views/discover.html'
        })
        .state('tvshowcard', {
            url: '/tvshowcard/:tv_show_name/:tmdb_id',
            controller: 'tvShowCardController',
            templateUrl: 'static/views/tvshowcard.html'
        })
        .state('default', {
        	url: '',
        	templateUrl: 'static/views/home.html'
        });

});

app.controller('allNames', function($scope, $http) {
    $http.get('/api/tv/all/').then(function(response) {
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

    $http.get('tmdb/'+$stateParams.tmdb_id+'/').then(function(response) {
        $scope.tvShowData = response.data;
        console.log($scope.tvShowData);
    });

    $http.get('api/keyword/name/'+$stateParams.tv_show_name+'/').then(function(response) {
        var keywordsArray = [];
        for (var i=0; i<response.data.length; i+=1) {
            keywordsArray.push(response.data[i]["keyword"]);
        }
        $scope.keywords = chunk(keywordsArray, 2);
    });

    $http.get('api/recommendation/'+$stateParams.tv_show_name+'/').then(function(response) {
        $scope.recommendedShow = response.data;
    });
});


app.controller('submitShowController', function($http, $scope, $location) {
    $scope.tvShowCard = function () {
        $http.get('/api/tv/name/'+$scope.tvShowName+'/').then(function(response) {
            $location.path('/tvshowcard/'+$scope.tvShowName+'/'+response.data["tmdb_id"]);
        });
    };
});


app.controller('recommendationController', function($http, $scope) {
    var filters = [];

    $scope.updateResults = function (keyword) {
        keys = '';
        if(keyword.checked == true) {
            filters.push(keyword.id);
        } else {
            filters.splice(filters.indexOf(keyword.keyword), 1);
        }
        if(filters.length > 0) {
            for(var i=0; i<filters.length-1; i+=1) {
                keys = keys+filters[i]+"&";
            }
            keys=keys+filters[filters.length-1];
            $http.get('/api/tv/keywordids/'+keys+'/').then(function(response) {
                $scope.tvShowsResults = chunk(response.data, 2);
            });
        } else {
            $scope.tvShowsResults = null;
        }
    };

    $scope.refreshKeywords = function () {
        $http.get('api/keyword/discover/10/').then(function(response) {
            $scope.randomKeywords = chunk(response.data, 2);
        });
    };

    $http.get('api/keyword/freq/10/').then(function(response) {
        $scope.frequentKeywords = chunk(response.data, 2);
    });

    $scope.refreshKeywords();
});