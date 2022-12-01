from discord_webhook import DiscordWebhook, DiscordEmbed
import subprocess
def get_last():
    with open("last.commit","r") as f:
        return f.read()

def get_update():
    with open("date.txt","r") as f:
        return f.read().split("\n")
    
def is_something_new(l,last):
    if l[0]==last:
        return False
    return True

def get_pos_last(l,last):
    return l.index(last)

up=get_update()
last=get_last()
if is_something_new(up,last):
    with open("com.txt","r") as f:
        com=f.read().split("\n")
    with open("author.txt","r") as f:
        auth=f.read().split("\n")
    i=get_pos_last(up,last)-1
    while i>=0:
        print(f"COMMIT à {up[i]} de {auth[i]} : {com[i]}")
        webhook = DiscordWebhook(url='EMBED URL')
        embed = DiscordEmbed(title='Nouveau Commit', description='Un nouveau commit a été effectué', color='ffdd99')
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/25/25231.png")
        embed.add_embed_field(name=f"Author",value=f"{auth[i]}")
        embed.add_embed_field(name="Date",value=f"{up[i]}")
        embed.add_embed_field(name="Message",value=f"{com[i]}",inline=False)


        webhook.add_embed(embed)

        response = webhook.execute()
        i=i-1
    with open("last.commit","w") as f:
        f.write(up[0])