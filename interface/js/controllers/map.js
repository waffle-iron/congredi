/*use strict*/
var angular = require('angular');
module.exports = function ($http, $session, $crypto, $routeParams) {
	/*use strict*/
	var forms = this;
	this.forms = [];
	this.submit = function (typeOf, data) {
		this.forms.push(data);
		this.errors = null;
		var apiUrl = '/api/record/' + typeOf + '/new';
		// var session = $session.getsession();
		// var signature = $crypto.sign(session.key, data);
		// var content = {
		//     session: session,
		//     recordType: typeOf,
		//     action: 'create',
		//     content: data,
		//     signature: signature
		// };
		// $http.post(apiUrl, content).success(
		//     function (data) {
		//         forms.forms = data;
		//     }
		// ).error(function (data) {
		//     alert('Error...');
		//     //this.errors = error;
		// });
	};
};