import discord, os, keep_alive, asyncio, datetime, pytz


from discord.ext import tasks, commands

client = commands.Bot(
 // this is prefix but its do nothing lol 😂
  command_prefix=':',
  self_bot=True
)




@client.event
async def on_connect():
 // it's streaming ❄️
  await client.change_presence(activity = discord.Streaming(name = "I'm lookin' right at the other half of me 👀✨😍" , url = "https://top.gg/bot/813709481430089739"))

// 24/7 online the project 
keep_alive.keep_alive()
// token acc go there >



//if u use repilit on this 
// client.run(os.getenv("TOKEN"), bot=False)


//if u use github use this 
// client.run('acc token', bot=False)
