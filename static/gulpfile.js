'use strict'
var args = require('yargs').argv,
	// ARGS, NOOP
	gulp = require('gulp'),
	gutil = require('gulp-util'),
	// CLEAN
	del = require('del'),
	// JS
	coffee = require('gulp-coffee'),
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
	minifyCss = require('gulp-minify-css'),
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
	gulp.src(['js/*.test.js'])
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
		.pipe(args.production ? minifyCss() : gutil.noop())
		.pipe(concat('app.min.css'))
		.pipe(gulp.dest('./dist/css/'));
});
// PAGE
gulp.task('page', ['clean'], function() {
	console.log('Rendering templates....');
	// gulp.src('./views/*.jade')
	// 	.pipe(jade())//liquid
	// 	.pipe(minify())
	// 	.pipe(gulp.dest('views'));
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
		'views/*.jade',
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
gulp.task('default', ['clean', 'js', 'tests', 'browser', 'ugly', 'css', 'page', 'tmp']);
//watcher
/*


$ gem update --system
$ gem install compass

Please refer the user guide
Installation

Install with npm

$ npm install gulp-compass --save-dev

Usage
Load config from config.rb

Please make sure to add css and sass options with the same value in config.rb since compass can't output css result directly.

    css default value is css.
    sass default value is sass.

var compass = require('gulp-compass');
 
gulp.task('compass', function() {
  gulp.src('./src/*.scss')
    .pipe(compass({
      config_file: './config.rb',
      css: 'stylesheets',
      sass: 'sass'
    }))
    .pipe(gulp.dest('app/assets/temp'));
});

Load config without config.rb

set your project path.

var compass = require('gulp-compass'),
  path = require('path');
 
gulp.task('compass', function() {
  gulp.src('./src/*.scss')
    .pipe(compass({
      project: path.join(__dirname, 'assets'),
      css: 'css',
      sass: 'sass'
    }))
    .pipe(gulp.dest('app/assets/temp'));
});

set your compass settings.

var compass = require('gulp-compass'),
  minifyCSS = require('gulp-minify-css');
 
gulp.task('compass', function() {
  gulp.src('./src/*.scss')
    .pipe(compass({
      css: 'app/assets/css',
      sass: 'app/assets/sass',
      image: 'app/assets/images'
    }))
    .pipe(minifyCSS())
    .pipe(gulp.dest('app/assets/temp'));
});

Support multiple require option

var compass = require('gulp-compass'),
  minifyCSS = require('gulp-minify-css');
 
gulp.task('compass', function() {
  gulp.src('./src/*.scss')
    .pipe(compass({
      css: 'app/assets/css',
      sass: 'app/assets/sass',
      image: 'app/assets/images',
      require: ['susy', 'modular-scale']
    }))
    .pipe(minifyCSS())
    .pipe(gulp.dest('app/assets/temp'));
});

Support return the output of the Compass as the callback

var compass = require('gulp-compass'),
  minifyCSS = require('gulp-minify-css');
 
gulp.task('compass', function() {
  gulp.src('./src/*.scss')
    .pipe(compass({
      css: 'app/assets/css',
      sass: 'app/assets/sass',
      image: 'app/assets/images'
    }))
    .on('error', function(error) {
      // Would like to catch the error here 
      console.log(error);
      this.emit('end');
    })
    .pipe(minifyCSS())
    .pipe(gulp.dest('app/assets/temp'));
});

gulp-compass with gulp-plumber

var compass = require('gulp-compass'),
  plumber = require('gulp-plumber'),
  minifyCSS = require('gulp-minify-css');
 
gulp.task('compass', function() {
  gulp.src('./src/*.scss')
    .pipe(plumber({
      errorHandler: function (error) {
        console.log(error.message);
        this.emit('end');
    }}))
    .pipe(compass({
      css: 'app/assets/css',
      sass: 'app/assets/sass',
      image: 'app/assets/images'
    }))
    .on('error', function(err) {
      // Would like to catch the error here 
    })
    .pipe(minifyCSS())
    .pipe(gulp.dest('app/assets/temp'));
});
var gulp = require('gulp');
var sass = require('gulp-sass');
var minifyCSS = require('gulp-minify-css');
var rename = require('gulp-rename');
var del = require('del');

gulp.task('clean', function(){
    del(['../typo3/fileadmin/assets/css/2014-12-30-ag-style.min.css'],{'force':true})
})

gulp.task('sass', function () {
    gulp.src('./scss/*.scss')
        .pipe(sass())
        .pipe(gulp.dest('./css'));
    gulp.src('./scss/*.scss')
        .pipe(sass())
        .pipe(gulp.dest('../typo3/fileadmin/assets/css/'));
});

gulp.task('minify-css', function() {
  gulp.src('./css/*.css')
    .pipe(minifyCSS({keepBreaks:true}))
    .pipe(rename("2014-12-30-ag-style.min.css"))
    .pipe(gulp.dest('../typo3/fileadmin/assets/css/'));
});

// Watch Files For Changes
gulp.task('watch', function() {
    gulp.watch('./scss/*.scss', ['clean','sass']);
    gulp.watch('./css/*.css', ['minify-css']);
});

// Default Task
gulp.task('default', ['clean','sass','minify-css','watch']);

*/