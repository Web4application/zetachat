const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: './src/index.js',  // Entry point for your app
  output: {
    path: path.resolve(__dirname, 'dist'),  // Output folder for bundled files
    filename: 'bundle.js',  // Output bundled file name
  },
  module: {
    rules: [
      {
        test: /\.js$/,  // Apply Babel loader for JS files
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env', '@babel/preset-react'],  // Use Babel for ES6 and React JSX
          },
        },
      },
      {
        test: /\.css$/,  // Load CSS files
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
  devServer: {
    contentBase: path.join(__dirname, 'public'),
    port: 3000,  // Port for the development server
    hot: true,   // Enable Hot Module Replacement
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './public/index.html',  // HTML template to inject the bundled scripts
    }),
  ],
  resolve: {
    alias: {
      '@components': path.resolve(__dirname, 'src/components/'),  // Optional alias for easier imports
    },
  },
};
