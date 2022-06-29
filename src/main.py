import json
import random
import asyncio
from unicodedata import name
import discord
from discord.commands import Option

bot = discord.Bot()
token = "PRIVACY"

bot_serverid = "Privacy"

CompanyNames = [
    None,
    'Ueng',
    'NEWE',
    'Itare',
    'LimDJ',
    'Dorong',
    'JssSWE',
    'WonKo.',
    'S. W.'
]

def init():
    uengembed = ChangeEmbed(0, 0)
    neweembed = ChangeEmbed(1, 0)
    muaembed = ChangeEmbed(2, 0)
    wonembed = ChangeEmbed(3, 0)
    jsweembed = ChangeEmbed(4, 0)
    limdembed = ChangeEmbed(5, 0)
    drembed = ChangeEmbed(6, 0)
    swmbed = ChangeEmbed(7, 0)

    return uengembed, neweembed, muaembed, wonembed, jsweembed, limdembed, drembed, swmbed

def ReadCompanyValue(Index):
    file = ReadAllCompanyValue()
    return file["company"][CompanyNames[Index]]

def ReadAllCompanyValue():
    with open(file="data/data.json", mode="r", encoding="UTF-8") as f:
        file=json.load(f)
        return file

def WriteCompanyValue(value, Index):
    file = ReadAllCompanyValue()
    file["company"][CompanyNames[Index]] = value
    with open(file="data/data.json", mode="w", encoding="UTF-8") as f:
        json.dump(file, f, indent=4)


def CreateCompanyEmbed():
    i, a = ChangeValue()
    return ChangeEmbed(i, a)

def ChangeValue():
    """ Changes Value """

    CompanyIndex = random.randint(1, 8)
    ChangePercent = random.randint(0, 100)
    global ChangeAmount

    if ChangePercent == 1:
        ChangeAmount = 0
    elif ChangePercent < 5:
        ChangeAmount = random.randint(-10000, 10000)/1000
    elif ChangePercent < 40:
        ChangeAmount = random.randint(-45000, 45000)/1000
    elif ChangePercent < 70:
        ChangeAmount = random.randint(-75000, 75000)/1000
    elif ChangePercent < 90:
        ChangeAmount = random.randint(-110000, 110000)/1000
    elif ChangePercent < 97:
        ChangeAmount = random.randint(-250000, 250000)/1000
    else:
        ChangeAmount = random.randint(-500000, 500000)/1000

    if ReadCompanyValue(CompanyIndex) + ChangeAmount < 1:
        WriteCompanyValue(1.000, CompanyIndex)
    else:
        WriteCompanyValue(round((ReadCompanyValue(CompanyIndex) + ChangeAmount)*1000)/1000, CompanyIndex)

    return CompanyIndex - 1, ChangeAmount


def ChangeEmbed(Index, Amount):
    """ Change Value to Embed """
    if Amount != 0:
        if Amount > 0:
            embed = discord.Embed(title="코인 :chart_with_upwards_trend:", color=0xFF5D5D)
            embed.add_field(name="코인", value=CompanyNames[Index+1])
            embed.add_field(name="가격 변화량", value=":small_red_triangle: " + str(Amount))
            embed.add_field(name="코인 가격", value=str(ReadCompanyValue(Index+1)) + "원")
            return embed
        elif Amount < 0:
            embed = discord.Embed(title="코인 :chart_with_downwards_trend:", color=0x5D5DFF)
            embed.add_field(name="코인", value=CompanyNames[Index+1])
            embed.add_field(name="가격 변화량", value=":small_red_triangle_down: " + str(Amount))
            embed.add_field(name="코인 가격", value=str(ReadCompanyValue(Index+1)) + "원")
            return embed
    else:
        embed = discord.Embed(title="코인 :white_large_square:", color=0x5D5D5D)
        embed.add_field(name="코인", value=CompanyNames[Index+1])
        embed.add_field(name="가격 변화량", value=":small_orange_diamond: " + str(Amount))
        embed.add_field(name="코인 가격", value=str(ReadCompanyValue(Index+1)) + "원")
        return embed

@bot.event
async def on_ready():
    print("ready!")
    await main()

@bot.event
async def on_message(message):
    bot_server = bot.get_channel(bot_serverid)
    if not message.author.bot and message.channel.id == bot_serverid:
        await message.delete()

@bot.slash_command(guild_ids = [838725916607119383],name="정보" ,description="코인 봇의 정보를 나타냅니다.")
async def info(ctx):
    embed = discord.Embed(color=0xDAF7A6)
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar)

    embed.add_field(name="공식 사이트", value="[클릭해 이동](<https://www.ueng.xyz>)", inline=True)
    embed.add_field(name="봇 초대하기", value="[클릭해 이동](<https://discord.com/api/oauth2/authorize?client_id=951788089725034526&permissions=8&scope=bot>)", inline=True)
    embed.add_field(name="봇 버전", value="0.01r", inline=True)

    embed.add_field(name="제작자들", value="<:amu1:964479349959061564> ItareWorks")

    embed.set_footer(text="Made by. WelloStudio", icon_url="https://cdn.discordapp.com/attachments/905771094370295900/991310034623545434/wello-Logo.png")

    await ctx.respond(embed=embed)

async def main():
    bot_server = bot.get_channel(bot_serverid)

    await bot_server.purge(limit=int(50))

    e, m, b, w, j, l, d, s = init()
    embed1 = await bot_server.send(embed=e)
    embed2 = await bot_server.send(embed=m)
    embed3 = await bot_server.send(embed=b)
    embed4 = await bot_server.send(embed=w)
    embed5 = await bot_server.send(embed=j)
    embed6 = await bot_server.send(embed=l)
    embed7 = await bot_server.send(embed=d)
    embed8 = await bot_server.send(embed=s)

    while True:

        await asyncio.sleep(random.randint(1, 10) / 10)

        Index, Amount = ChangeValue()
        toembed = ChangeEmbed(Index=Index, Amount=Amount)

        if Index == 0:
            await embed1.edit(embed=toembed)

        elif Index == 1:
            await embed2.edit(embed=toembed)

        elif Index == 2:
            await embed3.edit(embed=toembed)

        elif Index == 3:
            await embed4.edit(embed=toembed)

        elif Index == 4:
            await embed5.edit(embed=toembed)

        elif Index == 5:
            await embed6.edit(embed=toembed)

        elif Index == 6:
            await embed7.edit(embed=toembed)

        elif Index == 7:
            await embed8.edit(embed=toembed)

bot.run(token)
