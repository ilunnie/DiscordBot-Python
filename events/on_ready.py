import discord

event_name = 'on_ready'

async def execute(bot):
    print(f'Bot iniciado como {bot.user}')