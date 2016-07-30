var angular = require('angular');
module.exports = function($routeProvider, $locationProvider) {
	// /objects/[/new, :id, :id/edit]
	// [/, /about, /contact, /profile/edit]
	$locationProvider.html5Mode(false); //true if matching
	$routeProvider
		.when('/', {
			templateUrl: 'static/views/home.html',
			controller: 'mainCtrl',
			controllerAs: 'main'
		})
		.when('/auth', {
			templateUrl: 'static/views/auth.html',
			controller: 'authCtrl',
			controllerAs: 'auth'
		})
		.when('/settings', {
			templateUrl: 'static/views/settings.html',
			controller: 'settingsCtrl as settings'
		})
		.when('/search', {
			templateUrl: 'static/views/search.html',
			controller: 'searchCtrl as search'
		})
		.when('/create', {
			templateUrl: 'static/views/create.html',
			controller: 'createCtrl'
		})
		.when('/edit', {
			templateUrl: 'static/views/edit.html',
			controller: 'createCtrl'
		})
		.when('/points:id', {
			templateUrl: 'static/views/points.html',
			controller: 'createCtrl',
			controllerAs: 'creatC'
		})
		.otherwise({
			redirectTo: '/'
		});
};