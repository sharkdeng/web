var HtmlWebpackPlugin = require('html-webpack-plugin');
const path = require('path');

module.exports = {
  entry: './src/main.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'resume.bundle.js'
  },
  mode: 'development',
  devtool: 'inline-source-map',
  module: {
    rules: [
      {
        test: "/\.[js|jsx]$/",
        exclude: "/node_modules/",
        use: {
          loader: "babel-loader"
        }
      }
    ]
  },
  plugins: [new HtmlWebpackPlugin({
      template: './src/index.html'
  })]
};