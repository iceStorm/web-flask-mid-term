var fs = require("fs");
var browserify = require("browserify");

var gulp = require('gulp');
var babel = require("gulp-babel");
var rename = require('gulp-rename');
var browserify = require('gulp-browserify');
var notify = require("gulp-notify");

var webpack = require('webpack-stream');


/*
browserify({ debug: true })
	.add("./doka.js")
	.transform("babelify")
	.bundle()
	.on('error', function (err) {
		console.log(err);
	})
	.pipe(fs.createWriteStream("./doka.min.js"))
	.on('end', () => {		
		console.log('done.');
	});*/
/*
gulp.task('js', function () {
    gulp.src('./doka.js')
        .pipe(browserify({ transform: ['babelify'] }))
        .on('error', (e) => {
			console.log(e);
		})
        .pipe(rename('./doka.min.js'))
});*/

/*
gulp.task('js', function () {
    gulp.src('./doka.js')
        .pipe(browserify())
         .on('error', (e) => {
			console.log(e);
		})
        .pipe(rename('./dist/js/bundle.js'))
        .pipe(gulp.dest('./'))
        .pipe(notify({title: "Success", message: "Well Done!", sound: "Glass"}));
});*/

/*
gulp.task('default', function () {
  return gulp.src('./doka.js')
    .pipe(webpack({
      output: {
        filename: 'app.js'
      }
    }))
    .pipe(gulp.dest('./dist/app.js'))
});*/


function defaultTask(cb) {
	gulp.task('default', function () {
	  return gulp.src('./doka.js')
		.pipe(webpack({
		  output: {
			filename: 'app.js'
		  }
		}))
		.pipe(gulp.dest('./dist/app.js'))
	});

	cb();
}

exports.default = defaultTask