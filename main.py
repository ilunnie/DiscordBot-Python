import discord
from discord.ext import commands
from decouple import config
import importlib
import os

# define o prefixo
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# obter a lista de arquivos da pasta "commands"
commands_folder = os.path.dirname(os.path.abspath(__file__)) + '/commands'
commands_files = os.listdir(commands_folder)

# iterar sobre cada arquivo da pasta "commands" e importá-lo
for file in commands_files:
    if file.endswith('.py'):
        # importar o arquivo como um módulo
        module = importlib.import_module(f'commands.{file[:-3]}')
        # adicionar os comandos do módulo à lista de eventos do objeto Bot
        for command in module.__all__:
            bot.add_command(getattr(module, command))

@bot.event
async def on_ready():
    print(f'Bot iniciado como {bot.user}')

bot.run(config('TOKEN'))