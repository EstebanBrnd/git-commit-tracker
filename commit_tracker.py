from discord_webhook import DiscordWebhook, DiscordEmbed
def get_last():
    try:
        with open("last.commit","r") as f:
            return f.read()
    except:
        with open("last.commit","w"):
            return ''

def get_update():
    with open("date.txt","r") as f:
        return f.read().split("\n")
    
def is_something_new(l,last):
    if l[0]==last:
        return False
    return True

def get_pos_last(l,last):
    return l.index(last)

def commit_analyse():
    with open("sortie.txt","r")as f:
        with open("commit.txt","w")as out:
            l=f.read().split("\n")
            list_files=[]
            for line in l:
                line=line.split(" ")
                if len(line)!=1:
                    if list_files!=[]:
                        text=" ".join(list_files)
                        out.write(text)
                        out.write("\n")
                        list_files=[]
                    out.write(line[0])
                    out.write(" ")
                if len(line)==1:
                    list_files.append(line[0])
            text=" ".join(list_files)
            out.write(text)
    with open("commit.txt","r") as f:
        l=f.read().split("\n")
        i=0
        for elt in l:
            a=elt.split(" ")
            l[i]=[a[0],"\n".join(a[1:])]
            i+=1
    return l

up=get_update()
last=get_last()
if is_something_new(up,last):
    with open("com.txt","r") as f:
        com=f.read().split("\n")
    with open("author.txt","r") as f:
        auth=f.read().split("\n")
    with open("name.txt","r") as f:
        name=f.read().strip("\r\n")
    with open("hash.txt","r") as f:
        hash=f.read().split("\n")
    d=commit_analyse()
    i=get_pos_last(up,last)-1
    while i>=0:
        print(f"COMMIT à {up[i]} de {auth[i]} : {com[i]}")
        webhook = DiscordWebhook(url='EMBED URL')
        embed = DiscordEmbed(title='Nouveau Commit', description='Un nouveau commit a été effectué', color='ffdd99')
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/25/25231.png")
        embed.add_embed_field(name=f"Author",value=f"{auth[i]}")
        embed.add_embed_field(name="Date",value=f"{up[i][:-6]}")
        embed.add_embed_field(name="Message",value=f"{com[i]}",inline=False)
        embed.add_embed_field(name="Hash",value=f"{hash[i]}")
        embed.add_embed_field(name="Ish",value=f"{d[i][0]}")
        embed.add_embed_field(name="Fichiers modifiés par ce commit",value=f"{d[i][1]}",inline=False)
        embed.set_footer(icon_url="https://cdn-icons-png.flaticon.com/512/25/25231.png",text=f"Modifications sur le GIT '{name}'")


        webhook.add_embed(embed)

        response = webhook.execute()
        i=i-1
    with open("last.commit","w") as f:
        f.write(up[0])
