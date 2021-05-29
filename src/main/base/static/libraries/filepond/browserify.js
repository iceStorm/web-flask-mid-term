var fs = require("fs");
var browserify = require("browserify");

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
	});

