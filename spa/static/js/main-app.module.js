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
        .state('recommandations', {
            url: '/recommandations',
            templateUrl: 'static/views/recommandations.html'
        })
        .state('tvshowcard', {
            url: '/tvshowcard/:tmdb_id',
            controller: 'tvShowCardController',
            templateUrl: 'static/views/tvshowcard.html'
        })
        .state('default', {
        	url: '',
        	templateUrl: 'static/views/accueil.html'
        });

});

app.provider("friendskeywords", function() {
    this.$get = function () {
        var keywords = ["date","friend","wedding","meet","occupation","apartment","privation","baby","play",
        				"party","girl","work","gang","love","guy","visit","together","look","call","semen"];
        return {
            keywords,
            "find": function (id) {
                if (id < keywords.length) {
                    return keywords[id];
                }
            }
        };
    }
});

app.controller("keywordsCtrl", function($scope, friendskeywords) {
    $scope.keywords = chunk(friendskeywords.keywords, 2);

});

app.controller('allNames', function($scope, $http) {
    $http.get('/api/names').then(function(response) {
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
    $http.get('/tmdb/'+$stateParams.tmdb_id+'/').then(function(response) {
        $scope.tvShowData = response.data;
    });
});

app.controller('submitSearchController', function($scope) {
    $scope.tvShowCard = function () {
        console.log("ça marche");
    };
});