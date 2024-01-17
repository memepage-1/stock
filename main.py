import re, os, asyncio, random, string, keep_alive
from discord.ext import commands, tasks

version = 'v2.7'

user_token = os.environ['user_token']
spam_id = os.environ['spam_id']
report_id = os.environ['report_id']

with open('data/pokemon','r', encoding='utf8') as file:
    pokemon_list = file.read()
with open('data/legendary','r') as file:
    legendary_list = file.read()
with open('data/mythical','r') as file:
    mythical_list = file.read()
with open('data/level','r') as file:
    to_level = file.readline()

num_pokemon = 0
shiny = 0
legendary = 0
mythical = 0

poketwo = 716390085896962058
client = commands.Bot(command_prefix= '&' )
intervals = [3.0, 2.2, 2.4, 2.6, 2.8]

def solve(message, file_name):
    hint = []
    for i in range(15,len(message) - 1):
        if message[i] != '\\':
            hint.append(message[i])
    hint_string = ''
    for i in hint:
        hint_string += i
    hint_replaced = hint_string.replace('_', '.')
    with open(f"data/{file_name}", "r") as f:
        solutions = f.read()
    solution = re.findall('^'+hint_replaced+'$', solutions, re.MULTILINE)
    if len(solution) == 0:
        return None
    return solution

@tasks.loop(seconds=random.choice(intervals))
async def spam():
    channel = client.get_channel(int(spam_id))
    await channel.send(''.join(random.sample(['1','2','3','4','5','6','7','8','9','0'],7)*5))

async def on_ready():
    print(f'Logged into account: {client.user.name}')
    guild = client.guilds[0]

@spam.before_loop
async def before_spam():
    await client.wait_until_ready()

spam.start()
@client.event
async def on_ready():
    print(f'Logged into account: {client.user.name}')


@client.event
async def on_message(message):
    channel = client.get_channel(message.channel.id)
    
    # Check if message is from Poketwo
    if message.author.id == poketwo:
        # Check if message contains Pokemon embed
        if message.embeds:
            embed_title = message.embeds[0].title
            if 'wild pokémon has appeared!' in embed_title:
                await asyncio.sleep(1)
                await channel.send('<@716390085896962058> h')
        else:
            content = message.content
            solution = None
            
            # Try to solve the Pokemon name from the message content
            if 'The pokémon is ' in content:
                    solution = solve(content, 'collection')
                    if solution:
                      await channel.clone()
             # If solution found, move to new category and sync.
                      category_name = 'Stock'
                      guild = message.guild
                      old_category = channel.category
                      new_category = [c for c in guild.categories if c.name == category_name][0]
                      num_channels = len(new_category.channels)
                      print(f"There are {num_channels} channels in the {category_name} category.")
                      if len(new_category.channels) <= 48:
                       await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                      if len(new_category.channels) >= 48:
                       category_name = 'Stock 2'
                       guild = message.guild
                       old_category = channel.category
                       new_category = [c for c in guild.categories if c.name == category_name][0]
                       num_channels = len(new_category.channels)
                       print(f"There are {num_channels} channels in the {category_name} category.")
                       if len(new_category.channels) <= 48:
                        await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                       if len(new_category.channels) >= 48:
                        category_name = 'Stock 3'
                        guild = message.guild
                        old_category = channel.category
                        new_category = [c for c in guild.categories if c.name == category_name][0]
                        num_channels = len(new_category.channels)
                        print(f"There are {num_channels} channels in the {category_name} category.")
                        if len(new_category.channels) <= 48:
                         await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                        if len(new_category.channels) >= 48:
                          category_name = 'Stock 4'
                          guild = message.guild
                          old_category = channel.category
                          new_category = [c for c in guild.categories if c.name == category_name][0]
                          num_channels = len(new_category.channels)
                          print(f"There are {num_channels} channels in the {category_name} category.")
                          if len(new_category.channels) <= 48:
                           await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                          if len(new_category.channels) >= 48:
                            category_name = 'Stock 5'
                            guild = message.guild
                            old_category = channel.category
                            new_category = [c for c in guild.categories if c.name == category_name][0]
                            num_channels = len(new_category.channels)
                            print(f"There are {num_channels} channels in the {category_name} category.")
                            if len(new_category.channels) <= 48:
                             await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                            if len(new_category.channels) >= 48:
                              category_name = 'Stock 6'
                              guild = message.guild
                              old_category = channel.category
                              new_category = [c for c in guild.categories if c.name == category_name][0]
                              num_channels = len(new_category.channels)
                              print(f"There are {num_channels} channels in the {category_name} category.")
                              if len(new_category.channels) <= 48:
                               await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                              if len(new_category.channels) >= 48:
                                category_name = 'Stock 7'
                                guild = message.guild
                                old_category = channel.category
                                new_category = [c for c in guild.categories if c.name == category_name][0]
                                num_channels = len(new_category.channels)
                                print(f"There are {num_channels} channels in the {category_name} category.")
                                if len(new_category.channels) <= 48:
                                 await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                                if len(new_category.channels) >= 48:
                                  category_name = 'Stock 8'
                                  guild = message.guild
                                  old_category = channel.category
                                  new_category = [c for c in guild.categories if c.name == category_name][0]
                                  num_channels = len(new_category.channels)
                                  print(f"There are {num_channels} channels in the {category_name} category.")
                                  if len(new_category.channels) <= 48: 
                                   await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                                  if len(new_category.channels) >= 48:
                                    category_name = 'Stock 9'
                                    guild = message.guild
                                    old_category = channel.category
                                    new_category = [c for c in guild.categories if c.name == category_name][0]
                                    num_channels = len(new_category.channels)
                                    print(f"There are {num_channels} channels in the {category_name} category.")
                                    if len(new_category.channels) <= 48: 
                                     await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                                    if len(new_category.channels) >= 48:
                                      category_name = 'Stock 10'
                                      guild = message.guild
                                      old_category = channel.category
                                      new_category = [c for c in guild.categories if c.name == category_name][0]
                                      num_channels = len(new_category.channels)
                                      print(f"There are {num_channels} channels in the {category_name} category.")
                                      if len(new_category.channels) <= 48: 
                                       await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                      await channel.send(f'<@716390085896962058> redirect 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40')
                      await asyncio.sleep(2)
                      await channel.edit(sync_permissions=True)
                    if not solution:
                      solution = solve(content, 'mythical')
                      if solution:
                       await channel.clone()
             # If solution found, move to new category and sync.
                       category_name = 'RareStock 1'
                       guild = message.guild
                       old_category = channel.category
                       new_category = [c for c in guild.categories if c.name == category_name][0]
                       num_channels = len(new_category.channels)
                       print(f"There are {num_channels} channels in the {category_name} category.")
                       if len(new_category.channels) <= 48:
                         await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                       if len(new_category.channels) >= 48:
                        category_name = 'RareStock 2'
                        guild = message.guild
                        old_category = channel.category
                        new_category = [c for c in guild.categories if c.name == category_name][0]
                        num_channels = len(new_category.channels)
                        print(f"There are {num_channels} channels in the {category_name} category.")
                        if len(new_category.channels) <= 48:
                         await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                        if len(new_category.channels) >= 48:
                         category_name = 'RareStock 3'
                         guild = message.guild
                         old_category = channel.category
                         new_category = [c for c in guild.categories if c.name == category_name][0]
                         num_channels = len(new_category.channels)
                         print(f"There are {num_channels} channels in the {category_name} category.")
                         if len(new_category.channels) <= 48:
                          await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                         if len(new_category.channels) >= 48:
                          category_name = 'RareStock 4'
                          guild = message.guild
                          old_category = channel.category
                          new_category = [c for c in guild.categories if c.name == category_name][0]
                          num_channels = len(new_category.channels)
                          print(f"There are {num_channels} channels in the {category_name} category.")
                          if len(new_category.channels) <= 48:
                           await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                          if len(new_category.channels) >= 48:
                            category_name = 'RareStock 5'
                            guild = message.guild
                            old_category = channel.category
                            new_category = [c for c in guild.categories if c.name == category_name][0]
                            num_channels = len(new_category.channels)
                            print(f"There are {num_channels} channels in the {category_name} category.")
                            if len(new_category.channels) <= 48:
                             await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                       await channel.send(f'<@716390085896962058> redirect 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40')
                      if not solution:
                       solution = solve(content, 'pokemon')
                       if solution:
                        await asyncio.sleep(2)
            else:
               await asyncio.sleep(3)
            if 'human' in content:
                    spam.cancel()
                    channel = client.get_channel({spam_id})
                    await channel.send(f'<@{report_id}> Needs Reset')
                    print('Captcha detected; autocatcher paused. Resume Manually, after solving captcha manually.')
    if not message.author.bot:
         await client.process_commands(message)
            

@client.command()
async def reboot(ctx):
  spam.start()

@client.command()
async def pause(ctx):
  spam.cancel()


keep_alive.keep_alive()
client.run(f"{user_token}")