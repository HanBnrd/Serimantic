function chunk (arr, size) {
	var newArr = [];
	for (var i=0; i<arr.length; i+=size) {
		newArr.push(arr.slice(i, i+size));
	}
	console.log(newArr)
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
        .state('ficheserie', {
            url: '/ficheserie',
            templateUrl: 'static/views/ficheserie.html'
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

$(document).ready(function(){
	$('.dropdown-button').dropdown({
			inDuration: 300,
			outDuration: 225,
			constrain_width: false, // Does not change width of dropdown to that of the activator
			hover: true, // Activate on hover
			gutter: 0, // Spacing from edge
			belowOrigin: false, // Displays dropdown below the button
			alignment: 'left' // Displays dropdown with edge aligned to the left of button
		}
	);
});