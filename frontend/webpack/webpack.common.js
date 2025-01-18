const Path = require('path');
const {CleanWebpackPlugin} = require('clean-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    entry: {
        app: Path.resolve(__dirname, '../src/scripts/index.js'),
    },
    output: {
        path: Path.join(__dirname, '../build'),
        filename: 'js/[name].js',
    },
    optimization: {
        splitChunks: {
            chunks: 'all',
            name: 'vendors',
        },
    },
    plugins: [
        new CleanWebpackPlugin(),
        new HtmlWebpackPlugin({
            template: Path.resolve(__dirname, '../src/index.html'),
        }),
    ],
    resolve: {
        alias: {
            '~': Path.resolve(__dirname, '../src'),
        },
    },
    module: {
        rules: [
            {
                test: /\.mjs$/,
                include: /node_modules/,
                type: 'javascript/auto',
            },
            {
                test: /\.html$/i,
                loader: 'html-loader',
            },
            {
                test: /\.(ico|jpg|jpeg|png|gif|eot|otf|webp|svg|ttf|woff|woff2)(\?.*)?$/,
                type: 'asset'
            },
        ],
    },
};