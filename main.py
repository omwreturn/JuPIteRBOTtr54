import os
import discord
from discord.ext import commands
from myserver import app_commands
from myserver import server_on

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# //////////////////// Bot Event ////////////////////
# คำสั่ง bot พร้อมใช้งานแล้ว
@bot.event
async def on_ready():
    print("Bot Online!")
    synced = await bot.tree.sync()
    print(f"{len(synced)} command(s)")

# แจ้งคนเข้า-ออกเซฟเวอร์
@bot.event
async def on_member_join(member):
    chanel = bot.get_channel(1293515967837765663) # IDห้อง
    text = f"Welcome to the server, {member.mention}!"

    emmbed = discord.Embed(title = 'Welcome to the server!',
                           description = text,
                           color = 0x66FFFF)
    
    await chanel.send(text) # ส่งข้อความไปที่ห้องนี้
    await chanel.send(embed = emmbed) # ส่ง Embed ไปที่ห้องนี้
    await member.send(text) # ส่งข้อความไปที่แชทส่วนตัวของ member

@bot.event
async def on_member_remove(member):
    chanel = bot.get_channel(1293515967837765663) # IDห้อง
    text = f"{member.name} has left the server!"
    await chanel.send(text) # ส่งข้อความไปที่ห้องนี้

# คำสั่ง chatbot
@bot.event
async def on_message(message):
    mes = message.content # ดึงข้อความที่ถูกส่งมา
    if mes == 'hello':
        await message.channel.send("Hello Sir!") # ส่งกลับไปที่ห้องนั้น
    
    elif mes == 'hi bot':
        await message.channel.send("Hello, " + str(message.author.name))

    await bot.process_commands(message) # ทำคำสั่ง event แล้วไปทำคำสั่ง bot command ต่อ

# //////////////////// Commands ////////////////////
# กำหนดคำสั่งให้บอท
@bot.command()
async def Bob(ctx):
    await ctx.send(f"hello {ctx.author.name}!")

@bot.command()
async def test(ctx, arg):

# Slash Commands
 @bot.tree.command(name='hellobot', description='Replies with Hello')
 async def hellocommand(interaction):
    await interaction.response.send_message("Hello It's me BOT DISCORD")

@bot.tree.command(name='name')
@app_commands.describe(name = "What's your name?")
async def namecommand(interaction, name : str):
    await interaction.response.send_message(f"Hello {name}")

# Embeds
@bot.tree.command(name='help', description='Bot Commands')
async def helpcommand(interaction):
    emmbed = discord.Embed(title='Help Me! - Bot Commands',
                           description='Bot Commands',
                           color=0x66FFFF,
                           timestamp= discord.utils.utcnow())
    
    # ใส่ข้อมูล
    emmbed.add_field(name='/hello1', value='Hello Command', inline=True)
    emmbed.add_field(name='/hello2', value='Hello Command', inline=True)
    emmbed.add_field(name='/hello3', value='Hello Command', inline=False)

    emmbed.set_author(name='Author', url='https://www.youtube.com/watch?v=YoGK3tyQsMM', icon_url='https://i.pinimg.com/564x/d2/00/c9/d200c94dced8941aba62c06a3c83182e.jpg') # type: ignore

    # ใส่รูปเล็ก-ใหญ่
    emmbed.set_thumbnail(url='https://i.pinimg.com/564x/d2/00/c9/d200c94dced8941aba62c06a3c83182e.jpg')
    emmbed.set_image(url='https://i.insider.com/5da1f837695b58492866de50?width=700')

    # Footer เนื้อหาส่วนท้าย
    emmbed.set_footer(text='Footer',icon_url='https://i.pinimg.com/564x/d2/00/c9/d200c94dced8941aba62c06a3c83182e.jpg')

server_on()

bot.run(os.getenv('TOKEN'))