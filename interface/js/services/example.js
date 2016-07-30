/*use strict*/
var angular = require('angular');
module.exports = function($scope) {
	//.config(['$provide', function ($provide) {
	// 	$provide.factory('serviceId', function () {
	// 		var shinyNewServiceInstance;
	// 		// factory function body that constructs shinyNewServiceInstance
	// 		return shinyNewServiceInstance;
	// 	});
	// }])
	// .factory('Note', ['$http', function ($http, $q, $resource) {
	// 	return {
	// 		all: function () {
	// 			return $http({
	// 				method: 'GET',
	// 				url: '/notes'
	// 			});
	// 		},
	// 		find: function (id) {
	// 			return $http({
	// 				method: 'GET',
	// 				url: '/notes/' + id
	// 			});
	// 		},
	// 		update: function (noteObj) {
	// 			return $http({
	// 				method: 'PUT',
	// 				url: '/notes',
	// 				data: noteObj
	// 			});
	// 		},
	// 		create: function (noteObj) {
	// 			return $http({
	// 				method: 'POST',
	// 				url: '/notes',
	// 				data: noteObj
	// 			});
	// 		}
	// 	};
	// }]);
};
/*
.factory('userPersistenceService', ['$cookies', function ($cookies) {
	//your service code goes here
}])
.factory('userPersistenceService', [
	'$cookies',
	function ($cookies) {
		var userName = '';
		return {
			setCookieData: function (username) {
				userName = username;
				$cookies.put('userName', username);
			},
			getCookieData: function () {
				userName = $cookies.get('userName');
				return userName;
			},
			clearCookieData: function () {
				userName = '';
				$cookies.remove('userName');
			}
		};
	}
])
.factory('authorization', function ($http, config) {
	var url = config.analytics.url;
	return {
		login: function (credentials) {
			return $http.post(url + '/auth', credentials);
		}
	};
})
.factory('httpInterceptor', function httpInterceptor($q, $window, $location) {
	return function (promise) {
		var success = function (response) {
			return response;
		};
		var error = function (response) {
			if (response.status === 401) {
				$location.url('/login');
			}
			return $q.reject(response);
		};
		return promise.then(success, error);
	};
})
.factory('api', function ($http, $cookies) {
	return {
		init: function (token) {
			$http.defaults.headers.common['X-Access-Token'] = token || $cookies.token;
		}
	};
})*/
