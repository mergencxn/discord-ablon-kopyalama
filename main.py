mytitle = "Sunucu Kopyalama Sistemi - Mergen"
from os import system
system("title "+mytitle)
import psutil
from pypresence import Presence
import time
import sys
client_id = 'Hesabının İd'
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone

client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.BLUE}
  __  __ ______ _____   _____ ______ _   _ 
 |  \/  |  ____|  __ \ / ____|  ____| \ | |
 | \  / | |__  | |__) | |  __| |__  |  \| |
 | |\/| |  __| |  _  /| | |_ |  __| | . ` |
 | |  | | |____| | \ \| |__| | |____| |\  |
 |_|  |_|______|_|  \_\\_____|______|_| \_|
                                           
                                            
                                                                      
{Style.RESET_ALL}
{Fore.YELLOW}> İnstagram İletişim : batefortedancha .{Style.RESET_ALL}
{Fore.YELLOW}> Discord İletişim : devilwounds{Style.RESET_ALL}

{Fore.YELLOW}> Orijinal İçerik{Style.RESET_ALL}



token = input(f'Lütfen hesap tokeni belirtin:\n >')
guild_s = input('Kopyalanacak sunucu id:\n >')
guild = input('Yapıştırılacak atacağınız sunucu id:\n >')
input_guild_id = guild_s  # <-- input guild id
output_guild_id = guild  # <-- output guild id
token = token  # <-- Hesap Tokeni


print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Giriş Yapılan Hesap: {client.user}")
    print("Sunucu Kopyalanıyor")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}
  __  __ ______ _____   _____ ______ _   _  _______   ___   _ 
 |  \/  |  ____|  __ \ / ____|  ____| \ | |/ ____\ \ / / \ | |
 | \  / | |__  | |__) | |  __| |__  |  \| | |     \ V /|  \| |
 | |\/| |  __| |  _  /| | |_ |  __| | . ` | |      > < | . ` |
 | |  | | |____| | \ \| |__| | |____| |\  | |____ / . \| |\  |
 |_|  |_|______|_|  \_\\_____|______|_| \_|\_____/_/ \_\_| \_|

İşlem Başarılı 

İnstagram : Batefortedancha
Discord : Devilwounds


                                                                                                                                      
                                                                               


    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    client.close()


client.run(token, bot=False)
