# My First Slack Bot
<p>A bot is a type of Slack App designed to interact with users via conversation.</p>
<p>When you build a bot for your Slack App, you're giving that app a face, a name, and a personality, and encouraging users to talk to it.</p>
<p>The bot can send DMs, it can be mentioned by users, it can post messages or upload files, and it can be invited to channels - or kicked out.</p>

## Install slackclient
```sh
$ pip3 install slackclient

$ pip3 freeze
aiohttp==3.7.4.post0
async-timeout==3.0.1
attrs==21.2.0
chardet==4.0.0
idna==3.2
multidict==5.1.0
slackclient==2.9.3
typing-extensions==3.10.0.0
yarl==1.6.3
```

## Create a Slack APP
- Create a new slack workspace.
![Alt text](ss/ss1.png?raw=true "slack workspace")
- Navigate to https://api.slack.com/apps and create an app From scratch.
![Alt text](ss/ss3.png?raw=true "slack app")
- Create a `Bot User` for the app, to use the Slack App as a bot:
  - Click on `OAuth & Permission` tab in the left sidebar.
  - In `Scopes` section, under `Bot Token Scopes`, click on `Add an OAuth Scope` and add the needed scopes.
  ![Alt text](ss/ss4.png?raw=true "slack app")
  - Click on `App Home` tab in the left sidebar to see the bot user and edit the display name.
  ![Alt text](ss/ss6.png?raw=true "bot user")


## Additional reading
- https://api.slack.com/bot-users