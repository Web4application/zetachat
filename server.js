const api = new ParseServer({
  databaseURI: databaseUri || 'mongodb://localhost:27017/dev',
  cloud: process.env.PARSE_SERVER_CLOUD || __dirname + '/cloud/main.js',
  appId: process.env.PARSE_SERVER_APPLICATION_ID || 'myAppId',
  masterKey: process.env.PARSE_SERVER_MASTER_KEY || '',
  fileUpload: {
    enableForPublic: true,
    enableForAnonymousUser: true,
    enableForAuthenticatedUser: true,
  }
});
await api.start();