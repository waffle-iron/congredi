var angular = require('angular');
module.exports = function ($timeout) {
	return function (scope, element) {
		$timeout(function () {
			$(element).tooltip({
				container: 'body'
			});
			$(element).tooltip();
		});
		scope.$on('$destroy', function () {
			$(element).tooltip('destroy');
		});
	};
};
