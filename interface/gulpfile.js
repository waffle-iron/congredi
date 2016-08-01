'use strict';
/*
bower openpgp
graceful-fs (npm ls graceful-fs
minimatch, to-iso-string, lodash, fsevents
docker run -ti --rm -u $UID -v `pwd`:/srv/ marmelab/bower bash -c "npm install && bower --allow-root --config.interactive install"
docker run -ti --rm -u $UID -v `pwd`:/srv/ marmelab/bower bash -c "npm install -g gulp && gulp"
docker run -ti --rm -u $UID -v `pwd`:/srv/ marmelab/bower bash -c "npm install --save-dev browser-sync browserify conventional-github-releaser del gulp-clean-css pub fs gulp gulp-autoprefixer gulp-browserify gulp-bump gulp-coffee gulp-concat gulp-conventional-changelog gulp-cssimport gulp-eslint gulp-git gulp-jasmine gulp-jshint gulp-less gulp-mocha gulp-rename gulp-uglify gulp-util jshint jshint-stylish vinyl-buffer vinyl-source-stream yargs && npm install --save angular angular-bootstrap angular-cookies angular-mock angular-resource angular-route angular-ui-grid angular-ui-router openpgp"
*/
var args = require('yargs').argv,
	// ARGS, NOOP
	gulp = require('gulp'),
	gutil = require('gulp-util'),
	// CLEAN
	del = require('del'),
	// JS
	eslint = require('gulp-eslint'),
	// TESTS
	jasmine = require('gulp-jasmine'),
	// MODULES
	browserify = require('browserify'),
	source = require('vinyl-source-stream'),
	buffer = require('vinyl-buffer'),
	// UGLIFY
	uglify = require('gulp-uglify'),
	concat = require('gulp-concat'),
	// CSS
	less = require('gulp-less'),
	cssimport = require('gulp-cssimport'),
	cleanCss = require('gulp-clean-css'),
	//RELEASE
	bump = require('gulp-bump'),
	fs = require('fs'),
	git = require('gulp-git'),
	conventionalChangelog = require('gulp-conventional-changelog'),
	conventionalGithubReleaser = require('conventional-github-releaser'),
	//WATCH
	browserSync = require('browser-sync');
var options = {
	globals: [
		'require'
	],
	envs: [
		'browser'
	],
	format: 'stylish',
	'extends': 'eslint:recommended',
	rules: {
		// enable additional rules
		'indent': [1, 'tab'],
		'linebreak-style': ['error', 'unix'],
		'quotes': ['error', 'single'],
		'semi': ['error', 'always'],
		'no-floating-decimal': ['error'],
		'no-useless-escape': 'error',
		'brace-style': ['error', '1tbs', {
			'allowSingleLine': true
		}],
		//'stroustrup', 'allman'
		'camelcase': 'error',
		//comma style
		'comma-dangle': ['error', 'never'],
		'comma-spacing': ['error', {
			'before': false,
			'after': true
		}],
		'comma-style': ['error', 'last', {
			'exceptions': {
				'ArrayExpression': true,
				'ObjectExpression': true
			}
		}],
		//length
		'max-len': [
			1, {
				'code': 120,
				'comments': 100,
				'ignoreTrailingComments': true,
				'ignoreUrls': true
			}
		],
		'max-lines': [1, {
			'max': 550,
			'skipBlankLines': true,
			'skipComments': true
		}],
		'max-statements': [1, 10, {
			'ignoreTopLevelFunctions': true
		}],
		'max-statements-per-line': [1, {
			'max': 3
		}],
		//spacing, padding
		'keyword-spacing': 'error',
		'key-spacing': 'error',
		'no-mixed-spaces-and-tabs': ['error', 'smart-tabs'],
		'no-trailing-spaces': ['error', {
			'skipBlankLines': true
		}],
		'padded-blocks': ['error', {
			'classes': 'never',
			'switches': 'never',
			'blocks': 'never'
		}],
		//function styles
		'func-style': [1, 'declaration'],
		'func-names': [1, 'never']
	}
};
// CLEAN
gulp.task('clean', function() {
	return del(['dist']);
});
// JS
gulp.task('js', ['clean'], function() {
	gulp.src(['js/*.js', '!gulpfile.js', '!dist/*', '!.test.js'])
		//.pipe(coffee())
		.pipe(eslint(options))
		.pipe(eslint.format())
		.pipe(eslint.failAfterError());
});
// TESTS
gulp.task('tests', function() {
	gulp.src(['js/tests/*.js'])
		.pipe(jasmine());
});
// MODULES
gulp.task('browser', ['clean'], function() {
	var b = browserify({
		entries: ['js/app.js'],
		debug: true,
		insertGlobals: true,
		ignore: ['jquery', 'underscore', 'bootstrap']
	});
	return b.bundle()
		.pipe(source('app.js'))
		.pipe(buffer())
		.pipe(gulp.dest('./build/js'));
});
// UGLIFY
gulp.task('ugly', ['js', 'browser'], function() {
	gulp.src(['./build/js/*'])
		.pipe(args.production ? uglify() : gutil.noop())
		.pipe(concat('app.min.js'))
		.pipe(gulp.dest('./dist/js/'));
});
// CSS
gulp.task('css', ['clean'], function() {
	gulp.src(['./css/*.css', '!dist/*']) //.less
		.pipe(less())
		.pipe(cssimport())
		.pipe(args.production ? cleanCss() : gutil.noop())
		.pipe(concat('app.min.css'))
		.pipe(gulp.dest('./dist/css/'));
});
// TMP
gulp.task('tmp', ['browser'], function() {
	return del(['build']);
});
gulp.task('watch', function() {
	var wjs = gulp.watch('js/*.js', ['js']);
	wjs.on('change', function(event) {
		gutil.log('Gulp is running!');
		console.log('Event type: ' + event.type); // added, changed, or deleted
		console.log('Event path: ' + event.path); // The path of the modified file
		if (event.type === 'deleted') { // if a file is deleted, forget about it
			delete cached.caches.scripts[event.path]; // gulp-cached remove api
			remember.forget('scripts', event.path); // gulp-remember remove api
		}
	});
	var wcss = gulp.watch('js/*.js', ['js']);
	wcss.on('change', function(event) {
		gutil.log('Gulp is running!');
		console.log('Event type: ' + event.type); // added, changed, or deleted
		console.log('Event path: ' + event.path); // The path of the modified file
		if (event.type === 'deleted') { // if a file is deleted, forget about it
			delete cached.caches.scripts[event.path]; // gulp-cached remove api
			remember.forget('scripts', event.path); // gulp-remember remove api
		}
	});
	var files = [
		'views/*.html',
		'css/*.css',
		'js*.js'
	];
	browserSync.init(files, {
		server: {
			baseDir: './app'
		}
	});
});
// RELEASE
gulp.task('bump-version', function() {
	// use minimist (https://www.npmjs.com/package/minimist) to determine with a
	return gulp.src(['./bower.json', './package.json'])
		.pipe(bump({
			type: 'patch'
		}).on('error', gutil.log))
		.pipe(gulp.dest('./'));
});
gulp.task('changelog', function() {
	return gulp.src('CHANGELOG.md', {
			buffer: false
		})
		.pipe(conventionalChangelog({
			preset: 'angular' // Or to any other commit message convention you use.
		}))
		.pipe(gulp.dest('./'));
});
gulp.task('commit-changes', function() {
	return gulp.src('.')
		.pipe(git.add())
		.pipe(git.commit('[Prerelease] Bumped version number'));
});
gulp.task('push-changes', function(cb) {
	git.push('origin', 'master', cb);
});
gulp.task('create-new-tag', function(cb) {
	var version = getPackageJsonVersion();
	git.tag(version, 'Created Tag for version: ' + version, function(error) {
		if (error) {
			return cb(error);
		}
		git.push('origin', 'master', {
			args: '--tags'
		}, cb);
	});

	function getPackageJsonVersion() {
		return JSON.parse(fs.readFileSync('./package.json', 'utf8')).version;
	};
});
gulp.task('github-release', function(done) {
	conventionalGithubReleaser({
		type: 'oauth',
		token: '0126af95c0e2d9b0a7c78738c4c00a860b04acc8' // change this to your own GitHub token or use an environment variable
	}, {
		preset: 'angular' // Or to any other commit message convention you use.
	}, done);
});
//New gulp version 4.0.0 will allow sequential operation...
gulp.task('release', function(callback) {
	runSequence(
		'bump-version',
		'changelog',
		'commit-changes',
		'push-changes',
		'create-new-tag',
		'github-release',
		function(error) {
			if (error) {
				console.log(error.message);
			}
			else {
				console.log('RELEASE FINISHED SUCCESSFULLY');
			}
			callback(error);
		});
});

//run order
gulp.task('default', ['clean', 'js', 'tests', 'browser', 'ugly', 'css', 'tmp']);
//watcher
