//https://gist.github.com/jeffjohnson9046/9470800
var angular = require('angular');
module.exports = function($filter) {
	return function (input, decimals) {
		return $filter('number')(input * 100, decimals) + '%';
	};
};
// scope.body = $sce.trustAsHtml(markdown.toHTML(scope.body.toString()));
