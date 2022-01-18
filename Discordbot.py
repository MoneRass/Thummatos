import discord
import random
import time
TOKEN = 'OTEyNjE5MDMwMzI4Nzk1MTk2.YZyktA.31jePEEEPYWhFFQQ8uej2SqUuc4'
import webbrowser as wb
#Made by Mr.Thummatos Sribunna
client = discord.Client()

@client.event
async def on_ready():
  print('Let do some monkey business do we {0.user}'.format(client))

  @client.event
  async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})') 

    if message.author == client.user:
      return

    if message.channel.name == 'general':
      if user_message.lower() == 'oi oi' or 'Im here':
        await message.channel.send(f'Let do some monkey business {username}!')
        return
      elif user_message.lower() == "bye boss":
        await message.channel.send(f'Have a nice day {username}!')
        return

    if message.content.startswith('hello'):
     await message.channel.send("What's up")

    if message.content.startswith('Let play'):
     await message.channel.send('Sound great!!')

    if message.content.startswith('Who is the best?'):
     await message.channel.send('DUCKOO')

    if message.content.startswith('See Ya'):
     await message.channel.send('See ya boss')

    if message.content.startswith('RPS'):
      rpss = ['ROCK', 'PAPER', 'SCISSOR']
      tell = random.choice(rpss)
      await message.channel.send(f'{username} is {tell}!')
      return 
    
#Made by Mr.Thummatos Sribunna    
    if message.content.startswith("lets play" ):
      await message.channel.send('Type "RPS" for Rock Paper Scissor')
      await message.channel.send('Type "Spin" for Russian roulette')
#Made by Mr.Thummatos Sribunna
    if message.content.startswith("Roll" ):
      dice1 = [1, 6]
      o = random.randint(1, 6)
      c = random.randint(1, 6)
      await message.channel.send(f'dice1 = {o}')
      time.sleep(3)
      await message.channel.send(f'dice2 = {c}')
#Made by Mr.Thummatos Sribunna
      time.sleep(2)
      num = o+c
      await message.channel.send(f'Total=>{num}')
#Made by Mr.Thummatos Sribunna
    if message.content.startswith("Present yourself" ):
      await message.channel.send('Hi, My name is DUCKOO Assistant.')
      time.sleep(1)
      await message.channel.send('I was made with Python by my boss.')
      time.sleep(1)
      await message.channel.send('Made by Mr.Thummatos Sribunna')
      time.sleep(1)
      await message.channel.send('He is my boss by the way.')
    if message.content.startswith("Present myself in th" ):
      await message.channel.send('สวัสดีครับ ผมนายธรรมทศ ศรีบุญณะ')
      time.sleep(1)
      await message.channel.send('ผู้เข้าสอบสัมภาษณ์ในโครงการเรียนดีช้างเผือก')
      time.sleep(1)
      await message.channel.send('คณะที่อยากเข้า คือ คณะวิศวกรรมคอมพิวเตอร์')
      time.sleep(1)
      await message.channel.send('Skills:')
      time.sleep(1)
      await message.channel.send('Python:9/10')
      time.sleep(1)
      await message.channel.send('HTML:6/10')
      time.sleep(1)
      await message.channel.send('CSS:7/10')
      time.sleep(1)
      await message.channel.send('Photoshop:8/10')
      time.sleep(1)
      await message.channel.send('Arduino:Basic')
#Made by Mr.Thummatos Sribunna   
client.run(TOKEN)
