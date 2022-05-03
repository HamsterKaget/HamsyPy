import os
import discord
import datetime
from dotenv import load_dotenv
from discord.ext import commands

# panggil file .env untuk mengambil bot token
load_dotenv()
# membuat / menginisiasi objek ( discord bot )
client = commands.Bot(command_prefix=['!', '?', 'h!'])
client.remove_command('help')
icon = 'https://images-ext-1.discordapp.net/external/on70in54InrZ-UDV4jK0ezXBVFUqk4dNfYHIxt-spwk/https/cdn.discordapp.com/icons/878869835805761596/d685fbdc273690a919010e761eda0c00.png'

@client.event
async def on_ready():
    print("bot sudah siap")

@client.command(name='help')
async def help(ctx):
    embed = discord.Embed(
        title = f"Panduan Penggunaan HamsyPy",
        description = f"Pesan ini merupakan panduan singkat untuk penggunaan HamsyPy. Anda bisa membaca full dokumentasi"
                      f" HamsyPy pada link berikut ini . atau kamu bisa bergabung dengan server bantuan di https://dsc.gg/HamsterArea",
        color = discord.Color.random(),
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name='!help', value='Perintah untuk mendapatkan panduan', inline=False)
    embed.add_field(name='!ping', value='Perintah untuk mengecek ping / latency bot', inline=False)
    embed.add_field(name='!info', value='Perintah untuk mendapatkan info bot', inline=False)
    embed.add_field(name='!userinfo <mention>', value='Perintah untuk mendapatkan info terhadap user yang di mention', inline=False)
    embed.add_field(name='!serverinfo', value='Perintah untuk mendapatkan info terhadap server saat ini', inline=False)
    embed.add_field(name='!serverinvite', value='Perintah untuk mendapatkan link invite server saat ini', inline=False)
    embed.add_field(name='!kick <mention>', value='Perintah untuk menendang / kick user yang di mention ', inline=False)
    embed.add_field(name='!ban <mention>', value='Perintah untuk membanned user yang di mention ', inline=False)
    embed.add_field(name='!unban <username + discriminator>', value='Perintah untuk unban user yang di mention', inline=False)
    embed.add_field(name="!purge <jumlah / all> [bulan] [tanggal] [tahun]", value='Perintah untuk menghapus pesan secara masal sesuai dengan argumen yang diteruskan')

    await ctx.reply(embed=embed)

@client.command(name='ping')
async def ping(ctx):
    await ctx.reply('**Pong ! 🏓 {0}ms **'.format(round(client.latency, 3)))

@client.command(name='info')
async def info(ctx):
    embed = discord.Embed(
        title = 'Info Untuk HamsyPy ✨#8028',
        description = 'HamsyPy adalah sebuah bot discord yang berfokus kepada utilitas untuk membantu mengatur server anda dengan lebih mudah.',
        color = discord.Color.random(),
    )
    embed.set_footer(
        text='dibuat dengan 💖 oleh HamsterKaget | Pre-Alpha v.0.22.5.1',
        icon_url=icon
    )
    embed.add_field(name='Statistik', value=f"{str(len(client.guilds))} Server!", inline=True)
    embed.add_field(name='Invite me!', value="[HamsyPy](https://discord.com/api/oauth2/authorize?client_id=965125053337444402&permissions=8&scope=bot)", inline=True)
    embed.add_field(name='Dokumentasi', value="[gitbook](https://gitbook.com)", inline=True)
    embed.add_field(name='Source Code', value="[github](https://github.com/HamsterKaget)", inline=True)
    embed.add_field(name='Support Us', value='[Donasi](https://trakteer.id/HamsterKaget)', inline=True)
    embed.add_field(name='Server Support', value='[HamsterArea](https://dsc.gg/HamsterArea)', inline=True)
    embed.set_thumbnail(url=icon)

    await ctx.reply(embed=embed)

@client.command(name='userinfo')
async def userinfo(ctx, member: discord.Member = None):
    embed = discord.Embed(
        description=f"<@{member.id}>",
        color= discord.Color.random()
    )
    embed.set_author(
        name = f'{member.name}#{member.discriminator}',
        url = '',
        icon_url = f"{member.avatar_url}"
    )
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.add_field(name='Dibuat pada', value=f"{member.created_at.strftime('%Y-%m-%d')}", inline=True)
    embed.add_field(name='Bergabung pada', value=f"{member.joined_at.strftime('%Y-%m-%d')}", inline=True)
    embed.add_field(name="Roles", value=" ".join(role.mention for role in member.roles), inline=False)
    embed.set_footer(text=f"ID :{member.id} | {member.name}#{member.discriminator}")

    await ctx.send(embed = embed)

@client.command(name='serverinfo')
async def serverinfo(ctx):
    server_name = f'{ctx.guild.name}'
    server_id = f'{ctx.guild.id}'
    server_icon = f'{ctx.guild.icon_url}'
    server_owner = f'<@{ctx.guild.owner_id}>'
    server_category = f'{len(ctx.guild.categories)}'
    server_text = f'{len(ctx.guild.text_channels)}'
    server_voice = f'{len(ctx.guild.voice_channels)}'
    server_roles = f'{len(ctx.guild.roles)}'
    server_member = f'{ctx.guild.member_count}'

    embed = discord.Embed(color= discord.Color.random())
    embed.set_author(
        name=server_name,
        url= ' ',
        icon_url=server_icon
    )
    embed.set_thumbnail(
        url=server_icon
    )
    embed.set_footer(text=f"ID : {server_id} | {ctx.guild.created_at.strftime('%Y-%m-%d')}")
    embed.add_field(name='Owner', value=server_owner, inline=True)
    embed.add_field(name='Categories', value=server_category, inline=True)
    embed.add_field(name='Text Channel', value=server_text, inline=True)
    embed.add_field(name='Voice Channel', value=server_voice, inline=True)
    embed.add_field(name='Member', value=server_member, inline=True)
    embed.add_field(name='Roles', value=server_roles, inline=True)

    await ctx.send(embed = embed)

@client.command(name='serverinvite')
@commands.has_permissions(create_instant_invite=True)
async def serverinvite(ctx):
    link = await ctx.channel.create_invite()
    await ctx.reply(f'**Your New Server Invite : {link}**')

@serverinvite.error
async def serverinvite_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply('**Maaf , Anda tidak mempunyai permission yang tepat untuk melakukan perintah ini**')

@client.command(name='purge')
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount, month=None, day=None, year=None):
    if amount == '-':
        amount = None
    if amount == 'all':
        amount = 101
    else :
        amount = int(amount) + 1

    if month == None or day == None or year == None:
        date = None
    else :
        date = datetime.datetime(int(year), int(month), int(day))

    await ctx.channel.purge(limit=amount, after=date)
    await ctx.channel.send('**Berhasil Menghapus Pesan**')

@purge.error
async def purgeerror(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply(f'**Maaf , Anda tidak mempunyai permission yang tepat untuk melakukan perintah ini**')

@client.command(name='kick')
@commands.has_guild_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *,reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'**{member} telah ditendang keluar server !**')

@kick.error
async def kickerror(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'**Maaf , Anda tidak mempunyai permission yang tepat untuk melakukan perintah ini**')

@client.command(name='ban')
@commands.has_guild_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} telah dibanned dari server!')

@ban.error
async def banerror(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'**Maaf , Anda tidak mempunyai permission yang tepat untuk melakukan perintah ini**')

@client.command(name='unban')
@commands.has_guild_permissions(ban_members=True)
async def unban(ctx, *, member) :
    banned_members = await ctx.guild.bans()
    for person in banned_members:
        user = person.user
        if member == str(user):
            await ctx.guild.unban(user)
            await ctx.send(f"**{person.user} telah di perbolehkan masuk kembali ke dalam server !**")

@unban.error
async def unbanerror(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'**Maaf , Anda tidak mempunyai permission yang tepat untuk melakukan perintah ini**')

# Mengambil bot token dari file .env kemudian jalankan bot dengan token tersebut
client.run(os.getenv("TOKEN"))