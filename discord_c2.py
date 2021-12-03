import discord, subprocess

# create a discord bot here "https://discord.com/developers/applications"
TOKEN = ""  # Use the bot's token here
client = discord.Client()

@client.event
async def on_message(message):
    # So the bot won't respond to itself.
    if message.author == client.user:
        return
    # Control what UserIDs, servers or channels are allowed to run the ~sh command
    if message.author.id == : # your userid so the bot can only respond to you
        if message.content.startswith("~sh"): # discord listening command
            command = (message.content.lower()[3:])
            bash = subprocess.check_output(command, shell=True)
            if '\n' in bash.decode():
                try:
                    await message.channel.send(bash.decode()[:-1])
                except Exception as e:
                    await message.channel.send(e)
            else:
                try:
                    await message.channel.send(bash.decode())
                except Exception as e:
                    await message.channel.send(e)

client.run(TOKEN)
