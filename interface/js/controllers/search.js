var angular = require('angular');
module.exports = function($scope) {
	console.log('starting');
	this.ask = function (asking) {
		console.log(asking);
		alert(asking);
	};
};