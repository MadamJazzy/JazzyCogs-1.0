import os
import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from cogs.utils import checks
from __main__ import send_cmd_help
import rethinkdb as r

class partnerapp():
    'Custom Cog for applications'
    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json('data/partner/settings.json')
        for s in self.settings:
            self.settings[s]['usercache'] = []

    def save_json(self):
        dataIO.save_json('data/partner/settings.json', self.settings)

    @commands.group(name='pset', no_pm=True)
    async def pset(self, ctx):
        'configuration settings'
        if (ctx.invoked_subcommand is None):
            (await send_cmd_help(ctx))

    def initial_config(self, guild_id):
        'makes an entry for the server, defaults to turned off'
        if (guild_id not in self.settings):
            self.settings[guild_id] = {'inactive': True, 'output': 0, 'cleanup': False, 'usercache': (), 'usermin': 0, 'multiout': False}
            self.save_json()

    @checks.admin_or_permissions(Manage_server=True)
    @pset.command(name='roles', no_pm=True)
    async def rolecreation(self, ctx):
        author = ctx.author
        guild = ctx.guild
        aprole = discord.utils.get(guild.roles, name='Partner Applicant')
        partnerrole = discord.utils.get(guild.roles, name='Partners')
        if (partnerrole not in guild.roles):
            (await guild.create_role(name='Partners'))
        if (aprole not in guild.roles):
            (await guild.create_role(name='Partner Applicant'))
        (await ctx.send('All done!'))

    @checks.admin_or_permissions(Manage_server=True)
    @pset.command(name='reset', no_pm=True)
    async def fix_cache(self, ctx):
        'Reset cache for applications'
        guild = ctx.guild
        self.initial_config(ctx.guild.id)
        self.settings[guild.id]['usercache'] = []
        self.save_json()
        (await ctx.send('Cache has been reset'))

    @checks.admin_or_permissions(Manage_server=True)
    @pset.command(name='channel', no_pm=True)
    async def setoutput(self, ctx, chan=None):
        'sets the place to output application embed to when finished.'
        guild = ctx.guild
        if (str(guild.id) not in self.settings):
            self.initial_config(str(guild.id))
        if (chan in self.settings[str(guild.id)]["output"]):
            return (await ctx.send('Channel already set as output'))
        for channel in guild.channels:
            if chan == channel.id:
                if self.settings[str(guild.id)]['multiout']:
                    self.settings[str(guild.id)]['output'] = chan
                    self.save_json()
                    return (await ctx.send('Channel added to output list'))
                else:
                    self.settings[str(guild.id)]['output'] = chan
                    self.save_json()
                    return (await ctx.send('Channel set as output'))
        (await ctx.send('I could not find a channel with that id'))

    @checks.admin_or_permissions(Manage_server=True)
    @pset.command(name='usermin', no_pm=True)
    async def usermin(self, ctx, usermin=0):
        'set a min number of users a server must have to apply'
        guild = ctx.guild
        author = ctx.author
        if (usermin >= 0):
            if (guild.id not in self.settings):
                self.initial_config(guild.id)
            else:
                self.settings[guild.id]['usermin'] = usermin
                (await ctx.send('{} has been set as min number of users'.format(usermin)))
        else:
            (await ctx.send('{} Input must be a number please try again'.format(author.mention)))

    @checks.admin_or_permissions(Manage_server=True)
    @pset.command(name='toggle', no_pm=True)
    async def reg_toggle(self, ctx):
        'Toggles applications for the server'
        guild = ctx.guild
        if (guild.id not in self.settings):
            self.initial_config(guild.id)
        self.settings[guild.id]['inactive'] = (not self.settings[guild.id]['inactive'])
        self.save_json()
        if self.settings[guild.id]['inactive']:
            (await ctx.send('Partner Applications disabled.'))
        else:
            (await ctx.send('Partner Applications enabled.'))

    @commands.command(name='partner')
    async def application(self, ctx):
        '"make an application by following the prompts'
        author = ctx.author
        guild = ctx.guild
        aprole = discord.utils.get(guild.roles, name='Partner Applicant')
        partnerrole = discord.utils.get(guild.roles, name='Partners')
        usermin = self.settings[guild.id]['usermin']
        if (guild.id not in self.settings):
            return (await ctx.send('Partner Applications are not setup on this server!'))
        if self.settings[guild.id]['inactive']:
            return (await ctx.send('We are not currently accepting partnership applications, Try again later'))
        if (partnerrole in author.roles):
            (await ctx.send('{}, You have already partnered with this server!'.format(author.mention)))
        elif (aprole in author.roles):
            (await ctx.send('{}You have already applied for partnership on this server!'.format(author.mention)))
        else:
            (await ctx.send('{}Ok lets start the application'.format(author.mention)))
            while True:
                avatar = (author.avatar_url if author.avatar else author.default_avatar_url)
                em = discord.Embed(timestamp=ctx.message.created_at, title='ID: {}'.format(author.id), color=discord.Color.blue())
                em.set_author(name='Partnership Application for {}'.format(author.name), icon_url=avatar)
                try:
                    membermsg = (await author.send('How many members does your server have'))
                    while True:
                        member = (await self.bot.wait_for('message', timeout=30))
                        if (member is None):
                            (await author.send('Sorry you took to long, please try again later!'))
                            break
                        else:
                            try:
                                member1 = int(member.content)
                                if (member1 > 0):
                                    if (member1 < usermin):
                                        (await author.send('You do not meet our member guidelines for parternship at'
                                                           ' this time. You must have no less than {} members in your server!'.format(usermin)))
                                        break
                                    elif (member1 >= usermin):
                                        em.add_field(name='MemberCount: ', value=member.content, inline=True)
                                    break
                            except ValueError:
                                (await author.send('MemberCount must be a number. Try again. This field is required!'))
                            break
                    if (member is None):
                        break
                    elif member1 < usermin:
                        break
                except discord.Forbidden:
                    (await self.bot.reply('You have your DMs turned off. I cannot DM you. Please enable your DMs to'
                                          ' continue. You can turn them back off after we are done.'))
                linkmsg = (await author.send('What is the Invite link to your server? Please be aware that you need to'
                                             ' make sure to set this invite to never expire. If the link expires then we will remove it from the partnership page. '))
                while True:
                    link = (await self.bot.wait_for('message', timeout=30))
                    if (link is None):
                        (await author.send('Timed out, Please run command again.'))
                        break
                    else:
                        em.add_field(name='Invite Link: ', value=link.content, inline=True)
                        break
                if (link is None):
                    break
                infomsg = (await author.send('Please provide us with a short description of your server this will be what'
                                             ' is posted in the partners channel if your application gets approved. '
                                             'Please make sure to perfect your description formatting BEFORE sending it'
                                             ' here. If you need to change it later speak to Partner Manager!'
                                             ' You have 2 Mins to write your info. Otherwise the application will'
                                             ' time out and you will have to start over!'))
                while True:
                    info = (await self.bot.wait_for('message', timeout=60))
                    if (info is None):
                        (await author.send('Timed out Please run command again'))
                        break
                    else:
                        break
                aprole = discord.utils.get(guild.roles, name='Partner Applicant')
                (await author.add_roles(aprole))
                (await author.send('You have finished the application. Thank you'))
                for output in self.settings[guild.id]['output']:
                    where = guild.get_channel(output)
                    if (where is not None):
                        if member1 < usermin:
                            (await author.send('You do not meet our member guidelines for parternship at this time. You must have no less than {} members in your server!'.format(usermin)))
                        else:
                            (await where.send(embed=em))
                            (await where.send(content=(('```\n' + info.content) + '\n```')))
                            break
                        break
                    break
                return

def check_folder():
    f = 'data/partner'
    if (not os.path.exists(f)):
        os.makedirs(f)

def check_file():
    f = 'data/partner/settings.json'
    if (dataIO.is_valid_json(f) is False):
        dataIO.save_json(f, {})

def setup(bot):
    check_folder()
    check_file()
    n = partnerapp(bot)
    bot.add_cog(n)