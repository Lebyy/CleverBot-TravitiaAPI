# A CleverBot made with the TravitiaApi which is coded in python.
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

 ## Feel free to add a star⭐ to the repository to promote the project!

> ## Bot Setup

### Create a Bot

1. Go to Discord's [Developer Portal](https://discordapp.com/developers/applications/).
2. Create a new application.
3. Add a bot user to your app.
4. Find your bot token, you will need this in the next section.

> Keep this token and any file containing it **private**! If your token ever leaks or you suspect it may have leaked, simply `regenerate` a new token to invalidate your compromised token.

5. Invite your bot to a server using: [https://discordapp.com/oauth2/authorize?scope=bot&client_id=COPY_PASTE_YOUR_DISCORD_BOT_CLIENT_ID_HERE](https://discordapp.com/oauth2/authorize?scope=bot&client_id=COPY_PASTE_YOUR_DISCORD_BOT_CLIENT_ID_HERE)

> A Discord bot's client ID is not the same as its token!

> ## Getting the bot files

1. Run `git clone lebon1377/CleverBot-TravitiaAPI` in your console to download the project.
2. Run `cd CleverBot-TravitiaAPI` in your console to navigate into the project.
3. Run `pip install -r requirements.txt` in your console to install project dependencies.

> ## Getting the TravitiaApi key.
Join the [Travitia API Discord server](https://discord.gg/C98nsXt) and use the `> api` command to request an API key.
![Getting a key](https://i.imgur.com/cUJsM3i.png "Getting a key")

> ## Configuring and Running the bot.

1. Open the bot.py file and on line 60 enter your bot token where it says 'Your Token' which you got from step 1. 
```python
bot.run('Your Token', bot=True, reconnect=True)
```
2. Open the cogs/cleverbot.py file and on line 11 enter your TravitiaApi where it says "Your TravitiaAPI Key" whcih you got from the step above.
```python
self.cleverbot = ac.Cleverbot("Your TravitiaAPI Key")
```
3. Run `python bot.py` to start your bot

4. Go to a discord server with the bot in and type `.cb [Your Message]` and enjoy chatting ☺️

5. If you would like to to change the bot prefix you need edit the bot.py and on line 29 where it says `prefixes = ['.']` you can change it to whatever you like, if you would like to change the command or the command alias edit the file in cogs/cleverbot.py on line 14 where it says `@commands.command(name="cleverbot", aliases=["cb"])` you can change it to whatever you like 

🎉 You're ready! 🎉

Visit Travitia Api Github repo for more information [Travitia API Github repo](https://github.com/crrapi/async-cleverbot)

## Note: The Api is not made by me neither I own Travitia this is just an example on how to setup the bot
