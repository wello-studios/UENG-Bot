import json
import random
import asyncio
import math

import discord
from discord.commands import Option

bot = discord.Bot()

bot_serverid = 984047852173033494

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

Companys= [
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

def ReadFile():
    with open(file="data/data.json", mode="r", encoding="UTF-8") as f:
        file=json.load(f)
        print(file)
        return file

def ReadCompanyValue(Index):
    file = ReadFile()
    return file["company"][CompanyNames[Index]]

def WriteCompanyValue(value, Index):
    file = ReadFile()
    file["company"][CompanyNames[Index]] = value
    with open(file="data/data.json", mode="w", encoding="UTF-8") as f:
        print(file)
        json.dump(file, f, indent=4)


def ReadUserValue(id, Index):
    file = ReadFile()
    try:
        value = file["user"][str(id)]["coins"][Index - 1]
    except:
        WriteNewUserValue(id)
        ReadUserValue(id, Index)
    else:    
        return value 

def WriteUserValue(value, id, Index):
    file = ReadFile()
    file["user"][str(id)]["coins"][Index - 1] = value
    print(file)
    with open(file="data/data.json", mode="w", encoding="UTF-8") as f:
        json.dump(file, f, indent=4)

def WriteUserMoney(value, id):
    file = ReadFile()
    file["user"][str(id)]["money"] = value
    print(file)
    with open(file="data/data.json", mode="w", encoding="UTF-8") as f:
        json.dump(file, f, indent=4)

def WriteNewUserValue(id):
    file = ReadFile()
    file["user"][str(id)] = {"coins": [0, 0, 0, 0, 0, 0, 0, 0], "money": 10000}
    print(file)
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
        ChangeAmount = random.randint(-20000, 20000)/1000
    elif ChangePercent < 40:
        ChangeAmount = random.randint(-90000, 90000)/1000
    elif ChangePercent < 70:
        ChangeAmount = random.randint(-150000, 150000)/1000
    elif ChangePercent < 90:
        ChangeAmount = random.randint(-220000, 220000)/1000
    elif ChangePercent < 97:
        ChangeAmount = random.randint(-4500000, 4500000)/1000
    else:
        ChangeAmount = random.randint(-1000000, 1000000)/1000

    if ReadCompanyValue(CompanyIndex) + ChangeAmount < 1:
        WriteCompanyValue(1.000, CompanyIndex)
    else:
        WriteCompanyValue(round((ReadCompanyValue(CompanyIndex) + ChangeAmount)*1000)/1000, CompanyIndex)

    '''print('??????   : ' + CompanyNames[CompanyIndex] + '??????')
    print('????????? : ' + str(ChangeAmount) + '???')
    print(CompanyNames[CompanyIndex] + '?????? ?????? ?????? : ' + str(ReadCompanyValue(CompanyIndex)))
    print('-' * 20)
    #'''
    return CompanyIndex - 1, ChangeAmount


def ChangeEmbed(Index, Amount):
    """ Change Value to Embed """
    if Amount != 0:
        if Amount > 0:
            embed = discord.Embed(title="?????? :chart_with_upwards_trend:", color=0xFF5D5D)
            embed.add_field(name="??????", value=CompanyNames[Index+1])
            embed.add_field(name="?????? ?????????", value=":small_red_triangle: " + str(Amount))
            embed.add_field(name="?????? ??????", value=str(ReadCompanyValue(Index+1)) + "???")
            return embed
        elif Amount < 0:
            embed = discord.Embed(title="?????? :chart_with_downwards_trend:", color=0x5D5DFF)
            embed.add_field(name="??????", value=CompanyNames[Index+1])
            embed.add_field(name="?????? ?????????", value=":small_red_triangle_down: " + str(Amount))
            embed.add_field(name="?????? ??????", value=str(ReadCompanyValue(Index+1)) + "???")
            return embed
    else:
        embed = discord.Embed(title="?????? :white_large_square:", color=0x5D5D5D)
        embed.add_field(name="??????", value=CompanyNames[Index+1])
        embed.add_field(name="?????? ?????????", value=":small_orange_diamond: " + str(Amount))
        embed.add_field(name="?????? ??????", value=str(ReadCompanyValue(Index+1)) + "???")
        return embed

async def main():
    bot_server = bot.get_channel(bot_serverid)

    await bot_server.purge(limit=500)

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

@bot.event
async def on_ready():
    print("ready!")
    await main()

@bot.event
async def on_message(message):
    bot_server = bot.get_channel(bot_serverid)
    if not message.author.bot and message.channel.id == bot_serverid:
        await message.delete()

@bot.slash_command(guild_ids = [838725916607119383],name="???" ,description="?????? ??? ??????????????? ?????? ???????????????.")
async def say(ctx, text: Option(str, "????????? ?????????, ??? ?????? ????????????.")):
    await ctx.defer()

    print("<", ctx.author.name, "> ", text)
    msg = input("?????????? : ")

    embed = discord.Embed(title=msg,description="**??????: "+text+"**", color=0xDAF7A6)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)

    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [838725916607119383],name="??????" ,description="?????? ?????? ????????? ???????????????.")
async def info(ctx):
    await ctx.defer()

    embed = discord.Embed(color=0xDAF7A6)
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar)

    embed.add_field(name="?????? ?????????", value="[????????? ??????](<https://www.ueng.xyz>)", inline=True)
    embed.add_field(name="??? ????????????", value="[????????? ??????](<https://discord.com/api/oauth2/authorize?client_id=951788089725034526&permissions=8&scope=bot>)", inline=True)
    embed.add_field(name="???????????? ??????\n", value="[????????? ??????](<https://discord.gg/KwgY6s2Y>)", inline=True)

    embed.add_field(name="??? ??????", value="0.01a", inline=True)
    embed.add_field(name="?????????", value="<:Wello:991308295103053884> WelloStudios", inline=True)

    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [838725916607119383],name="????????????" ,description="????????? ???????????????.")
async def buycoin(ctx, ??????: Option(str, "?????? ?????? ?????? ????????? ??????", choices=Companys, required=True), ??????: Option(int, "????????? ????????? ??????", required=True)):
    await ctx.defer()

    global index

    if ?????? == Companys[0]:
        index = 1
    if ?????? == Companys[1]:
        index = 2
    if ?????? == Companys[2]:
        index = 3
    if ?????? == Companys[3]:
        index = 4
    if ?????? == Companys[4]:
        index = 5
    if ?????? == Companys[5]:
        index = 6
    if ?????? == Companys[6]:
        index = 7
    if ?????? == Companys[7]:
        index = 8

    value = ReadCompanyValue(index-1)
    prize = ?????? * value

    user = ReadUserValue(ctx.author.id, index)
    
    global embed
    if user["money"] > prize:
        WriteUserMoney(user["money"] - prize, ctx.author.id)
        WriteUserValue(user["coins"][index-1] + ??????, ctx.author.id, index)

        embed = discord.Embed(title="?????? ??????! :white_check_mark:", description=?????? + "?????? " + ?????? + "?????? ??????????????? ?????????????????????.", color=0x2aef2a)

        embed.add_field(name="??????",value=??????,inline=True)
        embed.add_field(name="??????",value=??????,inline=True)

        embed.add_field(name="?????? ??????",value=prize,inline=False)
        embed.add_field(name="?????? ??? ??????",value=user["money"],inline=True)
    else:
        embed = discord.Embed(title="?????? ??????.. :x:",color=0xef2a2a)
        embed.add_field(name="????????? ???????????????.",value=user["money"])

    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [838725916607119383],name="????????????" ,description="| ????????? ?????? |  ?????? ?????? ?????? ???????????? ???????????????.")
async def loaduserdata(ctx, id: Option(str, "????????? ?????????", required=True), index: Option(str, "????????? ?????????", required=False)):
    await ctx.defer()

    global embed

    if index == None:
        embed=discord.Embed(title=id)

        coins = []
        for i in range(1, 9, 1):
            embed.add_field(name=CompanyNames[i], value=ReadUserValue(id, i), inline=True)

    else:
        embed=discord.Embed(title=str(id), description=str(index))

        embed.add_field(name=str(CompanyNames[int(index)]), value=str(ReadUserValue(int(id), int(index))), inline=True)


    await ctx.respond(embed=embed)


bot.run("TOKEN")
