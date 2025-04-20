import {DiscordSDK} from '@discord/embedded-app-sdk';
const discordSdk = new DiscordSDK(1208380409814188042);

async function setup() {
  // Wait for READY payload from the discord client
  await discordSdk.ready();

  // Pop open the OAuth permission modal and request for access to scopes listed in scope array below
  const {code} = await discordSdk.commands.authorize({
    client_id: 1208380409814188042,
    response_type: 'code',
    state: '',
    prompt: 'none',
    scope: ['identify', 'applications.commands'],
  });

  // Retrieve an access_token from your application's server
  const response = await fetch('/.proxy/api/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      code,
    }),
  });
  const {access_token} = await response.json();

  // Authenticate with Discord client (using the access_token)
  auth = await discordSdk.commands.authenticate({
    access_token,
  });
}
