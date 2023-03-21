import discord
from discord.ext import commands
import sympy

# criar um comando "hello"
@commands.command(aliases=['calcular', 'calcule', 'calculate', 'cal'])
async def calculate_expression(ctx, equation: str = None):
    # verifica se o usuário esqueceu de mandar a equação
    if equation is None:
        embed = discord.Embed(
            title='Título do Embed',
            description='Descrição do Embed',
            color=discord.Color.blue()
        )

        # adicionar um campo ao embed
        embed.add_field(name='Nome do Campo', value='Valor do Campo', inline=False)

        # enviar o embed para o canal
        await ctx.channel.send(embed=embed)

    # faz a equação que o usuário pediu
    else:
        # avaliar a equação usando a biblioteca sympy
        result = sympy.sympify(equation)

        # enviar o resultado para o chat
        await ctx.send(f'O resultado é {result}.')

# adicionar o comando à lista de objetos que devem ser importados
__all__ = ['calculate_expression']