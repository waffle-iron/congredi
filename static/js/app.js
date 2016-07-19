//http://pineconellc.github.io/angular-foundation/



var angular = require('angular'),
	uiBootstrap = require('angular-bootstrap'),
	ngCookies = require('angular-cookies'),
	//mock = require('angular').mock,
	ngRoute = require('angular-route'),
	ngGrid = require('angular-ui-grid'),
	ngRouterUI = require('angular-ui-router'),
	ngResource = require('angular-resource');
	//openpgp = require('openpgp'), -- needs ./config module
	//webtorrent.io
	//markdown.js
// when dom is ready

var app = angular.module('todoApp', [ 'ngRoute' ]);

var routesConfig		= require('./routes'),
	authCtrl		= require('./controllers/auth'),
	createCtrl	= require('./controllers/create'),
	//cryptoCtrl	= require('./controllers/crypto'),
	editCtrl		= require('./controllers/edit'),
	//mainCtrl		= require('./controllers/main'),
	mapCtrl		= require('./controllers/map'),
	navCtrl		= require('./controllers/nav'),
	pointsCtrl	= require('./controllers/points'),
	searchCtrl	= require('./controllers/search'),

	authDirective		= require('./directives/auth'),
	mapDirective		= require('./directives/map'),
	navDirective		= require('./directives/navauth'),

	percentFilter		= require('./filters/percent'),
	
	exampleService		= require('./services/example');

angular.module('app',			['ngRoute'])
	.config(['$routeProvider', '$locationProvider', routesConfig])

	.controller('auth',			['$scope', '$location', '$cookieStore', '$localStorage', authCtrl])
	.controller('create',		['$scope', '$location', createCtrl])
	//.controller('crypto',		cryptoCtrl)
	.controller('edit',			editCtrl)
	.controller('map',			mapCtrl)
	//.controller('main',			mainCtrl)
	.controller('nav',			['$scope', '$http', '$log', navCtrl])
	.controller('points',		pointsCtrl)
	.controller('search',		['$scope', searchCtrl])

	//abc
	.directive('auth',			authDirective)
	.directive('map',			mapDirective)
	.directive('navauth',		navDirective)

	.filter('percent',			['$filter', percentFilter])
	//.pgp
	//.onion (AACSOnion? :3)
	.service('example',			exampleService);
	//abc
	//def
	//jwt
	//.api
	//.stv
	//.pgp
	//.rtc
	//.tor
	//.tf
	//.caffe





console.log('hello');
//https://github.com/btford/angular-socket-io
//https://github.com/mgechev/angular-webrtc
//http://blog.mgechev.com/2014/12/26/multi-user-video-conference-webrtc-angularjs-yeoman/
// might have to use SBC instead of STUN? or simply Tor rendesvous? *gulp*
// this rendesvous could be relatively durable (like scons....)
//https://github.com/Ayms/node-Tor
//https://github.com/digitalbazaar/forge
//https://github.com/Ayms/node-Tor/tree/master/install
//https://github.com/bitwiseshiftleft/sjcl