var config = require('./webpack.base.js'),
    port = 3001;

config.devtool = 'cheap-module-eval-source-map';

config.output.publicPath = 'http://localhost:' + port + '/dist/';

config.module = {
    noParse: /node_modules\/quill\/dist\/quill\.js/,
    rules: [
        {
            test: /\.css$/,
            loader: 'style-loader!css-loader',
        },
    ],
};

module.exports = config;
