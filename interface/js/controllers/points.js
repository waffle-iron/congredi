//http://lusilva.github.io/word-galaxy/
//http://anvaka.github.io/pm/#/
var angular = require('angular');
module.exports = function ($cookies) {
	$cookies.put('myFavorite', 'oatmeal');
	console.log($cookies.get('myFavorite'));
	$cookies.remove('myFavorite');
};
