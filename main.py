import discord , tokens

# prefix: str = "!"
# intents = discord.Intents.default()

cogs = [
  "hello"
  ]

bot: discord.Bot = discord.Bot()

@bot.event
async def on_ready():
  print("Log in as " + str(bot.user))

for cog in cogs:
  bot.load_extension(cog)

bot.run(tokens.bot)
