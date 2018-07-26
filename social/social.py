import os
from random import randint

import discord
from discord.ext import commands


class Social:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(invoke_without_command=True)
    async def kiss(self, ctx, *, user: discord.Member):
        """Kiss people!"""
        sender = ctx.message.author
        folder = 'kiss'
        if ctx.message.author == user:
            (await ctx.send((sender.mention + ' You pervert! You cannot do that to yourself!')))
        else:
            (await self.upload_random_gif(ctx, (((user.mention + ' was KISSED by ') + sender.mention) + '! :kiss:'),
                                          folder))

    @commands.command(invoke_without_command=True)
    async def bite(self, ctx, *, user: discord.Member):
        """Bite people!"""
        sender = ctx.message.author
        folder = 'bite'
        if ctx.message.author == user:
            (await ctx.send((sender.mention + " As kinky as that is, I can't let you do that to yourself!")))
        else:
            (await self.upload_random_gif(ctx, (((user.mention + ' was BITTEN by ') + sender.mention) + '! '), folder))

    @commands.command(invoke_without_command=True)
    async def slap(self, ctx, *, user: discord.Member):
        """Slap people!"""
        sender = ctx.message.author
        folder = 'slap'
        if ctx.message.author == user:
            (await ctx.send((sender.mention + ' You Masochist! You cannot do that to yourself!')))
        else:
            (await self.upload_random_gif(ctx,
                (((user.mention + ' was SLAPPED by ') + sender.mention) + ' and i think they liked it! '), folder))

    @commands.command(invoke_without_command=True)
    async def taunt(self, ctx, *, user: discord.Member):
        """Taunt people!"""
        sender = ctx.message.author
        folder = 'taunt'
        if ctx.message.author == user:
            (await ctx.send((sender.mention + ' You must be really lonely? Do you need a friend? ')))
        else:
            (await self.upload_random_gif(ctx, (((user.mention + ' was TAUNTED by ') + sender.mention) + '! '), folder))

    @commands.command(invoke_without_command=True)
    async def cuddle(self, ctx, *, user: discord.Member):
        """Cuddle people!"""
        sender = ctx.message.author
        folder = 'cuddle'
        if ctx.message.author == user:
            (await ctx.send((
                sender.mention + ' I am sorry that you are so lonely, but you cannot Cuddle with yourself, That is masturbation! ')))
        else:
            (await self.upload_random_gif(ctx,
                (((user.mention + ' CUDDLES HARD with ') + sender.mention) + ' , and they like it! '), folder))

    @commands.command(invoke_without_command=True)
    async def hugs(self, ctx, *, user: discord.Member):
        """Hug people!"""
        sender = ctx.message.author
        folder = 'hug'
        if ctx.message.author == user:
            (await ctx.send((sender.mention + ' Sorry, you are not that flexible. You cannot Hug yourself!')))
        else:
            (await self.upload_random_gif(ctx, (((user.mention + ' was given a BIG hug from ') + sender.mention) + '! '),
                                          folder))

    @commands.command(invoke_without_command=True)
    async def feed(self, ctx, *, user: discord.Member):
        """Feed people!"""
        sender = ctx.message.author
        folder = 'feeds'
        if ctx.message.author == user:
            (await ctx.send((sender.mention + " I'm so glad you know how to feed yourself! ")))
        else:
            (await self.upload_random_gif(ctx, (((user.mention + ' was FED by ') + sender.mention) + '! '), folder))

    @commands.command(invoke_without_command=True)
    async def spank(self, ctx, *, user: discord.Member):
        """Spank people!"""
        sender = ctx.message.author
        folder = 'spank'
        if ctx.message.author == user:
            (await ctx.send(
                (sender.mention + ' I NEED AN ADULT!!! You cannot use me to spank yourself. That is Nasty! ')))
        else:
            (await self.upload_random_gif(ctx,
                (((user.mention + ' was SPANKED HARD by ') + sender.mention) + ' , and they LOVED it! '), folder))

    @commands.command(invoke_without_command=True)
    async def tease(self, ctx, *, user: discord.Member):
        """Tease people!"""
        sender = ctx.message.author
        folder = 'tease'
        if ctx.message.author == user:
            (await ctx.send((sender.mention + " You're a special person aren't you? You cannot tease yourself! ")))
        else:
            (await self.upload_random_gif(ctx, (((user.mention + ' was TEASED by ') + sender.mention) + '! '), folder))

    @commands.command(invoke_without_command=True)
    async def hi5(self, ctx, *, user: discord.Member):
        """HighFive people!"""
        sender = ctx.message.author
        folder = 'hi5'
        if ctx.message.author == user:
            (await ctx.send((sender.mention + ' Nice try, You have to get out more! ')))
        else:
            (await self.upload_random_gif(ctx, (((user.mention + ' was HIGHFIVED by ') + sender.mention) + '! '), folder))

    @commands.command(invoke_without_command=True)
    async def shoot(self, ctx, *, user: discord.Member):
        """Shoot people!"""
        sender = ctx.message.author
        folder = 'shoot'
        if ctx.message.author == user:
            (await ctx.send((sender.mention + " Calm down! I am sure we can solve whatever problem you're having. ")))
        else:
            (await self.upload_random_gif(ctx, (((user.mention + ' was SHOT by ') + sender.mention) + '! They survived! '),
                                          folder))

    @commands.command(invoke_without_command=True)
    async def lick(self, ctx, *, user: discord.Member):
        """Lick people!"""
        sender = ctx.message.author
        folder = 'lick'
        if ctx.message.author == user:
            (await ctx.send((sender.mention + " Well aren't you a kinky little thing? And very flexible! ")))
        else:
            (await self.upload_random_gif(ctx, (((user.mention + ' was LICKED by ') + sender.mention) + '! '), folder))

    @commands.command(invoke_without_command=True)
    async def shake(self, ctx, *, user: discord.Member):
        """Handshake!"""
        sender = ctx.message.author
        folder = 'handshake'
        if ctx.message.author == user:
            (await ctx.send((sender.mention + ' No, Just No! Get a life! ')))
        else:
            (await self.upload_random_gif(ctx, (((user.mention + ' Shook ') + sender.mention) + "'s Hand! "), folder))

    @commands.command(invoke_without_command=True)
    async def twerk(self, ctx, *, user: discord.Member):
        """TWERK!"""
        sender = ctx.message.author
        folder = 'twerk'
        if ctx.message.author == user:
            (await ctx.send(
                (sender.mention + " Did you just try to twerk on yourself? We'll pretend that never happened! ")))
        else:
            (await self.upload_random_gif(ctx,
                (((user.mention + ' TWERKED FOR ') + sender.mention) + '! and they LIKED it! '), folder))

    @commands.command(invoke_without_command=True)
    async def strip(self, ctx, *, user: discord.Member):
        """STRIP!"""
        sender = ctx.message.author
        folder = 'strip'
        if ctx.message.author == user:
            (await ctx.send((sender.mention + ' No, Just No! Get a life! ')))
        else:
            (await self.upload_random_gif(ctx, (((sender.mention + ' strips for ') + user.mention) + ' and they LIKE it! '),
                                          folder))

    @commands.command(invoke_without_command=True)
    async def thirsty(self, ctx, *, user: discord.Member):
        """The Thirst is Real!"""
        sender = ctx.message.author
        folder = 'thirsty'
        if ctx.message.author == user:
            (await ctx.send((sender.mention + ' Really? Just really?? You need help! ')))
        else:
            (await self.upload_random_gif(ctx,
                (((sender.mention + ' tells ') + user.mention) + ' To calm your thirsty ass down! '), folder))

    @commands.command(invoke_without_command=True)
    async def moist(self, ctx, *, user: discord.Member):
        """Moist lol!"""
        sender = ctx.message.author
        folder = 'moist'
        if ctx.message.author == user:
            (await ctx.send((sender.mention + ' You are way to easy! ')))
        else:
            (await self.upload_random_gif(ctx, (((user.mention + ' has made ') + sender.mention) + ' moist. OH LORD! '),
                                          folder))

    @commands.command(invoke_without_command=True)
    async def whip(self, ctx, *, user: discord.Member):
        """Whip someone!"""
        sender = ctx.message.author
        folder = 'whip'
        if ctx.message.author == user:
            (await ctx.send((sender.mention + " Well aren't you just a kinky thing! ")))
        else:
            (await self.upload_random_gif(ctx,
                (((sender.mention + ' has whipped ') + user.mention) + ' and i think they LIKED it! '), folder))

    @commands.command(invoke_without_command=True)
    async def facepalm(self, ctx, *, user: discord.Member):
        """Facepalm images!"""
        sender = ctx.message.author
        folder = 'facepalm'
        if ctx.message.author == user:
            (await ctx.send((sender.mention + ' You cannot do that to yourself! ')))
        else:
            (await self.upload_random_gif(ctx, (((user.mention + ' has made ') + sender.mention) + ' FACEPALM! '), folder))

    @commands.command(invoke_without_command=True)
    async def ohno(self, ctx, *, user: discord.Member):
        """Oh no they didn't images!"""
        sender = ctx.message.author
        folder = 'ono'
        if ctx.message.author == user:
            (await ctx.send((sender.mention + ' You cannot do that to yourself! ')))
        else:
            (await self.upload_random_gif(ctx, (((sender.mention + ' yells at ') + user.mention) + " Oh no they didn't! "),
                                          folder))

    @commands.command(invoke_without_command=True)
    async def hungry(self, ctx, *, user: discord.Member):
        """Hungry images!"""
        sender = ctx.message.author
        folder = 'hungry'
        if ctx.message.author == user:
            (await ctx.send((sender.mention + ' THEN GO GET SOMETHING TO EAT! ')))
        else:
            (await self.upload_random_gif(ctx, (((user.mention + ' has made ') + sender.mention) + ' HUNGRY! '), folder))

    @commands.command(invoke_without_command=True)
    async def nuts(self, ctx, *, user: discord.Member):
        """NutCracker images!"""
        sender = ctx.message.author
        folder = 'nuts'
        if ctx.message.author == user:
            (await ctx.send((sender.mention + ' No, Just no! Get a life! ')))
        else:
            (await self.upload_random_gif(ctx,
                (((sender.mention + ' wants to kick ') + user.mention) + ' in the NUTS! OUCH!! '), folder))

    async def upload_random_gif(self, ctx, msg, folder):
        if msg:
            (await ctx.send(msg))
        folderpath = ('data/social/' + folder)
        filelist = os.listdir(folderpath)
        gifpath = ((folderpath + '/') + filelist[randint(0, (len(filelist) - 1))])
        await ctx.send(file=discord.File(gifpath))


def setup(bot):
    bot.add_cog(Social(bot))
