var angular = require('angular');
module.exports = function($scope,$http,$log) {
	this.ask = function (asking) {
		alert(asking);
		// $http.get(apiUrl).success(
		//     function (data) {
		//         ses = data.session;
		//         name = data.name;
		//     });
	};
};