from discord.ext import commands
import discord
import aiohttp
from bs4 import BeautifulSoup

class revimage():
    'Reverse image search commands'

    def __init__(self, bot):
        self.bot = bot
        self.tineye_session = aiohttp.ClientSession()

    def __unload(self):
        self.tineye_session.close()

    def _tag_to_title(self, tag):
        return tag.replace(' ', ', ').replace('_', ' ').title()

    @commands.command()
    async def tineye(self, ctx, link=None):
        """
        Reverse image search using tineye
        usage:  .tineye <image-link> or
                .tineye on image upload comment
        """
        file = ctx.message.attachments
        if ((link is None) and (not file)):
            (await ctx.send("Message didn't contain Image"))
        else:
            async with ctx.channel.typing():
                if file:
                    url = file[0]['proxy_url']
                else:
                    url = link
                    (await ctx.message.delete())
            async with self.tineye_session.get('https://tineye.com/search/?url={}'.format(url)) as response:
                soup = BeautifulSoup((await response.text()), 'html.parser')
                pages = []
                image_link = None
                try:
                    hidden = soup.find(class_='match').select('.hidden-xs')[0]
                    if hidden.contents[0].startswith('Page:'):
                        pages.append('<{}>'.format(hidden.next_sibling['href']))
                    else:
                        image_link = hidden.a['href']
                except AttributeError:
                    embed = discord.Embed(title='Reverse Image Details', color=16776960)
                    embed.add_field(name='Original Link', value='<{}>'.format(url), inline=False)
                    embed.add_field(name='Matches', value='**No Matches Found**', inline=False)
                    embed.add_field(name='Full Search', value='https://tineye.com/search/?url={}'.format(url), inline=False)
                except IndexError:
                    embed = discord.Embed(title='Reverse Image Details', color=16776960)
                    embed.add_field(name='Original Link', value='<{}>'.format(url), inline=False)
                    embed.add_field(name='Matches', value='**No Matches Found**', inline=False)
                    embed.add_field(name='Full Search', value='https://tineye.com/search/?url={}'.format(url), inline=False)
            if (image_link is not None):
                embed = discord.Embed(title='Reverse Image Details', color=16776960)
                embed.add_field(name='Original Link', value='<{}>'.format(url), inline=False)
                embed.add_field(name='Matches', value='<{}>'.format(image_link), inline=False)
                embed.add_field(name='Full Search', value='https://tineye.com/search/?url={}'.format(url), inline=False)
            (await ctx.send(embed=embed))

def setup(bot):
    bot.add_cog(revimage(bot))
