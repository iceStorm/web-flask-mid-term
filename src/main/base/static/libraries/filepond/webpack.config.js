const path = require('path');


module.exports = {
    entry: {
        b: "./doka.js",
    },
    output: {
        path: path.join(__dirname, "dist"),
        filename: "[name].js",
    }
}
