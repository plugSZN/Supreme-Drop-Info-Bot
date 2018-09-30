import discord
import json
import logging
import requests

logger = logging.getLogger('discord')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

with open('config.json') as json_file:
    json_data = json.load(json_file)

user_agent = json_data['user_agent']

@client.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(client.user.name)
    print('------')
    print('Made by @plugSZN')
    print('Discord - plugSZN#2405')
    print('Twitter - https://twitter.com/piugSZN')
    print('------')

#Supreme Drops			
@client.event
async def on_message(message):

    if message.content.startswith('!ping'):
        await client.send_message(message.channel, "Im alive dont worry :)")
		
    if message.content.startswith('!supreme'):
        await client.send_message(message.channel, "Which category? reply with ! + jackets, shirts, tops, sweatshirts, pants, shorts, hats, bags, accessories, or skate.")
		
    if message.content.startswith('!jackets'):
        embed=discord.Embed(title="Item", description="Supreme®/Nike® Crewneck", color=0xce0005)
        embed.set_image(url='https://www.supremecommunity.com/u/season/add/20180925/976a446b862648c1a29bae7fbf255cc2_sqr.jpg')
        embed.add_field(name="Retail Price", value="$128/£118", inline=False)
        embed.set_footer(text="Made by @piugSZN", icon_url="https://pbs.twimg.com/profile_images/1025605978375573504/K7tygQju_400x400.jpg")
        await client.send_message(message.channel, embed=embed)

        embed=discord.Embed(title="Item", description="Supreme®/Nike® Double Zip Quilted Work Jacket", color=0xce0005)
        embed.set_image(url='https://www.supremecommunity.com/u/season/add/20180925/d51f2707eeb94549b69846efeb1c5c47_sqr.jpg')
        embed.add_field(name="Retail Price", value="$260/£240", inline=False)
        embed.set_footer(text="Made by @piugSZN", icon_url="https://pbs.twimg.com/profile_images/1025605978375573504/K7tygQju_400x400.jpg")
        await client.send_message(message.channel, embed=embed)

        embed=discord.Embed(title="Item", description="Supreme®/Nike® Reversible Nylon Sherpa Vest", color=0xce0005)
        embed.set_image(url='https://www.supremecommunity.com/u/season/add/20180925/40ef0ed1b3b24cfebf091da42f026b08_sqr.jpg')
        embed.add_field(name="Retail Price", value="$168/£154", inline=False)
        embed.set_footer(text="Made by @piugSZN", icon_url="https://pbs.twimg.com/profile_images/1025605978375573504/K7tygQju_400x400.jpg")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!shirts'):
        embed=discord.Embed(title="Item", description="Stripe Heavyweight Flannel Shirt", color=0xce0005)
        embed.set_image(url='https://www.supremecommunity.com/u/season/fall-winter2018/shirts/a9e0ddcf8f46453b964b3c157793dea0_sqr.jpg')
        embed.add_field(name="Retail Price", value="$118/£99", inline=False)
        embed.set_footer(text="Made by @piugSZN", icon_url="https://pbs.twimg.com/profile_images/1025605978375573504/K7tygQju_400x400.jpg")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!tops'):
        embed=discord.Embed(title="Item", description="Panel Stripe Waffle Thermal", color=0xce0005)
        embed.set_image(url='https://www.supremecommunity.com/u/season/fall-winter2018/tops-sweaters/15ad3197b9a2437d8522c7952c3c61ed_sqr.jpg')
        embed.add_field(name="Retail Price", value="$98/£86", inline=False)
        embed.set_footer(text="Made by @piugSZN", icon_url="https://pbs.twimg.com/profile_images/1025605978375573504/K7tygQju_400x400.jpg")
        await client.send_message(message.channel, embed=embed)

        embed=discord.Embed(title="Item", description="Supreme®/Nike® Jacquard Polo", color=0xce0005)
        embed.set_image(url='https://www.supremecommunity.com/u/season/add/20180925/c888f56765464c3e8c3f9ca2c477dfcd_sqr.jpg')
        embed.add_field(name="Retail Price", value="$124/£114", inline=False)
        embed.set_footer(text="Made by @piugSZN", icon_url="https://pbs.twimg.com/profile_images/1025605978375573504/K7tygQju_400x400.jpg")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!sweatshirts'):
        embed=discord.Embed(title="Item", description="Supreme®/Nike® Crewneck", color=0xce0005)
        embed.set_image(url='https://www.supremecommunity.com/u/season/add/20180925/976a446b862648c1a29bae7fbf255cc2_sqr.jpg')
        embed.add_field(name="Retail Price", value="$128/£118", inline=False)
        embed.set_footer(text="Made by @piugSZN", icon_url="https://pbs.twimg.com/profile_images/1025605978375573504/K7tygQju_400x400.jpg")
        await client.send_message(message.channel, embed=embed)

        embed=discord.Embed(title="Item", description="Supreme®/Nike® Plaid Hooded Sweatshirt", color=0xce0005)
        embed.set_image(url='https://www.supremecommunity.com/u/season/add/20180925/c1181482e5274dac948b7c93fa4e70c9_sqr.jpg')
        embed.add_field(name="Retail Price", value="$158/£144", inline=False)
        embed.set_footer(text="Made by @piugSZN", icon_url="https://pbs.twimg.com/profile_images/1025605978375573504/K7tygQju_400x400.jpg")
        await client.send_message(message.channel, embed=embed)
	
        embed=discord.Embed(title="Item", description="Love or Hate Hooded Sweatshirt", color=0xce0005)
        embed.set_image(url='https://www.supremecommunity.com/u/season/fall-winter2018/sweatshirts/aabbee34c50f40dfacf612d04863b688_sqr.jpg')
        embed.add_field(name="Retail Price", value="$168/£148", inline=False)
        embed.set_footer(text="Made by @piugSZN", icon_url="https://pbs.twimg.com/profile_images/1025605978375573504/K7tygQju_400x400.jpg")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!pants'):
        embed=discord.Embed(title="Item", description="Supreme®/Nike® Sweatpant", color=0xce0005)
        embed.set_image(url='https://www.supremecommunity.com/u/season/add/20180925/01236740edf44d598cc3e06af1cb8e12_sqr.jpg')
        embed.add_field(name="Retail Price", value="$128/£118", inline=False)
        embed.set_footer(text="Made by @piugSZN", icon_url="https://pbs.twimg.com/profile_images/1025605978375573504/K7tygQju_400x400.jpg")
        await client.send_message(message.channel, embed=embed)

        embed=discord.Embed(title="Item", description="Supreme®/Nike® Cotton Twill Overalls", color=0xce0005)
        embed.set_image(url='https://www.supremecommunity.com/u/season/add/20180925/b05e234a74754cd5bc90df71d0121654_sqr.jpg')
        embed.add_field(name="Retail Price", value="$198/£178", inline=False)
        embed.set_footer(text="Made by @piugSZN", icon_url="https://pbs.twimg.com/profile_images/1025605978375573504/K7tygQju_400x400.jpg")
        await client.send_message(message.channel, embed=embed)
	
        embed=discord.Embed(title="Item", description="Supreme®/Nike® Plaid Sweatshort", color=0xce0005)
        embed.set_image(url='https://www.supremecommunity.com/u/season/add/20180925/9a01d96072ce422f87b36f93187732b7_sqr.jpg')
        embed.add_field(name="Retail Price", value="$108/£98", inline=False)
        embed.set_footer(text="Made by @piugSZN", icon_url="https://pbs.twimg.com/profile_images/1025605978375573504/K7tygQju_400x400.jpg")
        await client.send_message(message.channel, embed=embed)
		
    if message.content.startswith('!hats'):
        embed=discord.Embed(title="Item", description="Napped Canvas Classic Logo 6-Panel", color=0xce0005)
        embed.set_image(url='https://www.supremecommunity.com/u/season/fall-winter2018/hats/0791f3ca668d4bb2814a28a344f62345_sqr.jpg')
        embed.add_field(name="Retail Price", value="$48/£46", inline=False)
        embed.set_footer(text="Made by @piugSZN", icon_url="https://pbs.twimg.com/profile_images/1025605978375573504/K7tygQju_400x400.jpg")
        await client.send_message(message.channel, embed=embed)

        embed=discord.Embed(title="Item", description="Piping Camp Cap", color=0xce0005)
        embed.set_image(url='https://www.supremecommunity.com/u/season/fall-winter2018/hats/e561b3a9d83744c092f55ce45f29e823_sqr.jpg')
        embed.add_field(name="Retail Price", value="$48/£46", inline=False)
        embed.set_footer(text="Made by @piugSZN", icon_url="https://pbs.twimg.com/profile_images/1025605978375573504/K7tygQju_400x400.jpg")
        await client.send_message(message.channel, embed=embed)
	
        embed=discord.Embed(title="Item", description="Small Stripe Beanie", color=0xce0005)
        embed.set_image(url='https://www.supremecommunity.com/u/season/fall-winter2018/hats/aecbdc54c6044748b2b7cd1e6c4b6e91_sqr.jpg')
        embed.add_field(name="Retail Price", value="$32/£28", inline=False)
        embed.set_footer(text="Made by @piugSZN", icon_url="https://pbs.twimg.com/profile_images/1025605978375573504/K7tygQju_400x400.jpg")
        await client.send_message(message.channel, embed=embed)
		
    if message.content.startswith('!accessories'):
        embed=discord.Embed(title="Item", description="Virgin Mary Blanket", color=0xce0005)
        embed.set_image(url='https://www.supremecommunity.com/u/season/fall-winter2018/accessories/e70592ee77e146548f961ed1fc83dcb5_sqr.jpg')
        embed.add_field(name="Retail Price", value="$118/£128", inline=False)
        embed.set_footer(text="Made by @piugSZN", icon_url="https://pbs.twimg.com/profile_images/1025605978375573504/K7tygQju_400x400.jpg")		
        await client.send_message(message.channel, embed=embed)

        embed=discord.Embed(title="Item", description="Supreme®/Nike® 14K Gold Earring", color=0xce0005)
        embed.set_image(url='https://www.supremecommunity.com/u/season/add/20180925/77217ef323034853b100990fcead2184_sqr.jpg')
        embed.add_field(name="Retail Price", value="$98/£88", inline=False)
        embed.set_footer(text="Made by @piugSZN", icon_url="https://pbs.twimg.com/profile_images/1025605978375573504/K7tygQju_400x400.jpg")
        await client.send_message(message.channel, embed=embed)
	

client.run(json_data['discord_token'])