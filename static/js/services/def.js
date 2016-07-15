var angular = require('angular');
module.exports = function ($http, $location) {
	var sessionPromise = $http({
		method: 'GET',
		url: '/session'
	});
	return {
		sessionData: function () {
			return sessionPromise;
		},

		authenticate: function () {
			this.sessionData().then(function (sessionUser) {
				if (!sessionUser || !sessionUser.data.id) {
					$location.path('/');
				}
			});
		}
	};
};