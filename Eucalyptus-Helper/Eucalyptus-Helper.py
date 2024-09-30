# Import des modules nécessaires
import discord
import os
from discord.ext import commands
import logging
import fitz
from watchdog.events import FileSystemEventHandler
import subprocess

# Configuration des logs et des permissions
logging.basicConfig(level=logging.DEBUG)
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='%', intents=intents)

# Fonction pour envoyer un message plus long que la limite Discord (2000 caractères)
async def send_long_message(channel, message):
    if len(message) <= 2000:
        await channel.send(message)
    else:
        message_parts = [message[i:i+2000] for i in range(0, len(message), 2000)]
        for part in message_parts:
            await channel.send(part)

# Commande pour exécuter une commande shell sur le serveur
@bot.command()
async def konsole(ctx, *args):
    command = " ".join(args)
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout.strip()
    channel_id = 1083635115399319572  # ID du canal Discord pour l'envoi des résultats
    channel = bot.get_channel(channel_id)
    await ctx.send(output)

# Événement déclenché lorsque le bot est prêt
@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

# Commande pour envoyer le journal système via journalctl
@bot.command()
async def log(ctx):
    try:
        process = subprocess.Popen(['sudo', 'journalctl', '-b', '-u', 'rc-local.service'], stdout=subprocess.PIPE)
        output, error = process.communicate()
        output_str = output.decode("utf-8")
        await send_long_message(ctx.channel, f'```\n{output_str}\n```')
    except Exception as e:
        await ctx.send(f'Une erreur est survenue: {e}')

# Gestionnaire d'erreurs pour envoyer des erreurs dans un canal Discord
@bot.event
async def on_error(event, *args, **kwargs):
    channel_id = "1083635115399319572"  # Remplacez par l'ID du canal approprié
    channel = bot.get_channel(channel_id)
    await channel.send(f"Erreur lors de l'événement {event}: {args[0]}")

# Classe pour gérer la surveillance des modifications de fichiers avec watchdog
class LogsEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == './nohup.out':  # Vérifie si le fichier modifié est nohup.out
            with open('./nohup.out', 'r') as f:
                logs = f.readlines()
                logs = ''.join(logs[-10:])  # Envoie les 10 dernières lignes
            channel = bot.get_channel(980244169996005396)  # ID du canal de logs
            if channel:
                bot.loop.create_task(channel.send(logs))

# Deuxième méthode on_ready pour initialiser le bot et les observateurs de fichier
@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    event_handler = LogsEventHandler()
    observer = Observer()
    observer.schedule(event_handler, './', recursive=False)
    observer.start()

# Méthode on_ready déclenchée pour notifier que le bot est en ligne
@bot.event
async def on_ready():
    print(f'{bot.user.name} est en ligne !')

# Commande test pour vérifier le fonctionnement du bot
@bot.command()
async def test(ctx):
    await ctx.send("La commande test fonctionne correctement !")

# Événement déclenché lorsqu'un nouveau membre rejoint le serveur
@bot.event
async def on_member_join(member):
    channel = bot.get_channel("1039938742053519462")  # Remplacez avec l'ID du canal de bienvenue
    await channel.send(f"Bienvenue sur le serveur, {member.mention} !")
    await bot.process_commands(member)

# Commande pour envoyer des images d'un dossier vers un canal Discord
@bot.command()
async def cpi(ctx, channel_id, chemin):
    channel = bot.get_channel(int(channel_id.strip('"')))
    try:
        for filename in os.listdir(chemin):
            if filename.endswith((".jpg", ".jpeg", ".png", ".gif", ".JPEG", ".PNG", ".GIF")):
                filepath = os.path.join(chemin, filename)
                with open(filepath, "rb") as f:
                    file = discord.File(f)
                    await channel.send(file=file)
    except FileNotFoundError:
        await ctx.send("Le chemin spécifié est incorrect ou ne peut pas être trouvé.")

# Commande pour envoyer un fichier PDF à un utilisateur spécifique en privé
@bot.command()
async def sendd(ctx, user: discord.User):
    filename = "Fiches De Révision Et Fiches Méthode.pdf"
    filepath = "E:/Rezki/Desktop/ma sauvgarde/ma clé/bac fiche/" + filename
    with open(filepath, 'rb') as f:
        file = discord.File(f, filename=filename)
        message = await user.send(
            "Bonjour, voici un fichier réservé à un usage interne. Veuillez ne pas le partager sans autorisation."
        )
        await user.send(file=file)
        await ctx.send(f"Le fichier {os.path.basename(filepath)} a été envoyé à {user}.")

# Méthode pour gérer les permissions d'accès à certains canaux selon les rôles (commentée car non utilisée)
"""
@bot.event
async def on_ready():
    # Implémentez la gestion des permissions ici pour différents rôles et canaux
"""

# Méthode pour renommer des canaux selon des conditions spécifiques (commentée car non utilisée)
"""
@bot.event
async def on_ready():
    guild = bot.get_guild(908429064228995073)
    for channel in guild.text_channels:
        if "correction" in channel.name:
            await channel.edit(name=f"✔️{channel.name}")
"""

# Méthode pour gérer la traduction du texte (commentée car non utilisée)
"""
# Implémentez ici une méthode pour la traduction automatique du texte
"""

# Lancement du bot (clé à ajouter manuellement lors du déploiement)
bot.run('VOTRE_CLE_BOT_DISCORD_ICI')
