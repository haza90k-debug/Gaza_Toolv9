#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V9 TOOL AI COMMENT BOT
Bot Discord optimisé pour Termux Android
Contrôle complet via Discord - Zéro interface web
"""

import discord
from discord.ext import commands, tasks
import os
import sys
from datetime import datetime, timedelta
from config import Config
from database import Database
from utils import Logger, format_uptime, get_ascii_art

# Initialisation
config = Config()
db = Database()
logger = Logger()

# Afficher ASCII art au démarrage
print(get_ascii_art())
logger.info("🚀 Démarrage du V9 TOOL AI COMMENT BOT")

# Configuration du bot Discord
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Variables de statistiques
stats = {
    "start_time": datetime.now(),
    "commands_executed": 0,
    "messages_analyzed": 0,
    "responses_generated": 0,
    "last_activity": datetime.now(),
    "auto_mode": False,
    "server_count": 0,
    "user_count": 0
}


@bot.event
async def on_ready():
    """Événement: Le bot s'est connecté"""
    logger.success(f"✅ Bot connecté en tant que {bot.user}")
    logger.info(f"📊 Serveurs: {len(bot.guilds)}")
    
    stats["server_count"] = len(bot.guilds)
    stats["user_count"] = sum(guild.member_count for guild in bot.guilds)
    
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="!help pour les commandes"
        )
    )
    
    db.add_log({
        "timestamp": datetime.now().isoformat(),
        "event": "BOT_CONNECTED",
        "guilds": len(bot.guilds),
        "users": stats["user_count"]
    })
    
    # Démarrer les tâches périodiques
    if not status_panel.is_running():
        status_panel.start()


@bot.event
async def on_disconnect():
    """Événement: Déconnexion du bot"""
    logger.warning("⚠️  Bot déconnecté - Reconnexion automatique...")
    db.add_log({
        "timestamp": datetime.now().isoformat(),
        "event": "BOT_DISCONNECTED"
    })


@bot.event
async def on_command_error(ctx, error):
    """Gestion des erreurs de commandes"""
    logger.error(f"❌ Erreur: {type(error).__name__}: {error}")
    
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ Arguments manquants. Utilisez `!help` pour plus d'infos.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("❌ Commande introuvable. Utilisez `!help` pour voir les commandes.")
    else:
        await ctx.send(f"❌ Erreur: {error}")


# ============= COMMANDES =============

@bot.command(name="help")
async def cmd_help(ctx):
    """Affiche toutes les commandes disponibles"""
    logger.info(f"📖 Commande HELP utilisée par {ctx.author}")
    stats["commands_executed"] += 1
    stats["last_activity"] = datetime.now()
    
    embed = discord.Embed(
        title="📖 V9 TOOL AI COMMENT BOT - Commandes",
        description="Toutes les commandes disponibles",
        color=discord.Color.blue(),
        timestamp=datetime.now()
    )
    
    commands_list = [
        ("!help", "Affiche cette aide"),
        ("!ping", "Affiche la latence du bot"),
        ("!status", "Affiche le statut du bot"),
        ("!stats", "Affiche les statistiques détaillées"),
        ("!start", "Active le mode automatique"),
        ("!stop", "Désactive le mode automatique"),
        ("!dashboard", "Affiche le panneau Discord"),
        ("!uptime", "Affiche le temps d'activité"),
        ("!restart", "Redémarre le bot (Admin)"),
    ]
    
    for cmd, desc in commands_list:
        embed.add_field(name=cmd, value=desc, inline=False)
    
    embed.set_footer(text="V9 TOOL AI COMMENT BOT | Termux Android")
    await ctx.send(embed=embed)


@bot.command(name="ping")
async def cmd_ping(ctx):
    """Affiche la latence du bot"""
    logger.info(f"🏓 Commande PING utilisée par {ctx.author}")
    stats["commands_executed"] += 1
    stats["last_activity"] = datetime.now()
    
    latency = bot.latency * 1000
    embed = discord.Embed(
        title="🏓 Pong!",
        description=f"Latence: **{latency:.2f}ms**",
        color=discord.Color.green(),
        timestamp=datetime.now()
    )
    await ctx.send(embed=embed)


@bot.command(name="status")
async def cmd_status(ctx):
    """Affiche le statut du bot"""
    logger.info(f"📊 Commande STATUS utilisée par {ctx.author}")
    stats["commands_executed"] += 1
    stats["last_activity"] = datetime.now()
    
    uptime = format_uptime(datetime.now() - stats["start_time"])
    
    embed = discord.Embed(
        title="📊 Statut du Bot",
        color=discord.Color.green(),
        timestamp=datetime.now()
    )
    
    embed.add_field(name="🟢 Statut", value="En ligne", inline=True)
    embed.add_field(name="⏱️ Uptime", value=uptime, inline=True)
    embed.add_field(name="🏓 Latence", value=f"{bot.latency*1000:.2f}ms", inline=True)
    embed.add_field(name="📡 Serveurs", value=str(stats["server_count"]), inline=True)
    embed.add_field(name="👥 Utilisateurs", value=str(stats["user_count"]), inline=True)
    embed.add_field(name="🤖 Mode Auto", value="✅ Actif" if stats["auto_mode"] else "❌ Inactif", inline=True)
    
    embed.set_footer(text="V9 TOOL AI COMMENT BOT")
    await ctx.send(embed=embed)


@bot.command(name="stats")
async def cmd_stats(ctx):
    """Affiche les statistiques détaillées"""
    logger.info(f"📈 Commande STATS utilisée par {ctx.author}")
    stats["commands_executed"] += 1
    stats["last_activity"] = datetime.now()
    
    uptime = format_uptime(datetime.now() - stats["start_time"])
    
    embed = discord.Embed(
        title="📈 Statistiques Détaillées",
        color=discord.Color.purple(),
        timestamp=datetime.now()
    )
    
    embed.add_field(name="⏱️ Temps en ligne", value=uptime, inline=False)
    embed.add_field(name="⚙️ Commandes exécutées", value=str(stats["commands_executed"]), inline=True)
    embed.add_field(name="💬 Messages analysés", value=str(stats["messages_analyzed"]), inline=True)
    embed.add_field(name="🤖 Réponses générées", value=str(stats["responses_generated"]), inline=True)
    embed.add_field(name="🔄 Dernière activité", value=f"<t:{int(stats['last_activity'].timestamp())}:R>", inline=True)
    embed.add_field(name="📡 Serveurs connectés", value=str(stats["server_count"]), inline=True)
    embed.add_field(name="👥 Utilisateurs total", value=str(stats["user_count"]), inline=True)
    
    embed.set_footer(text="V9 TOOL AI COMMENT BOT | Termux Android")
    await ctx.send(embed=embed)


@bot.command(name="start")
async def cmd_start(ctx):
    """Active le mode automatique"""
    logger.info(f"▶️ Commande START utilisée par {ctx.author}")
    stats["commands_executed"] += 1
    stats["last_activity"] = datetime.now()
    stats["auto_mode"] = True
    
    embed = discord.Embed(
        title="▶️ Mode Automatique Activé",
        description="Le bot est maintenant en mode automatique",
        color=discord.Color.green(),
        timestamp=datetime.now()
    )
    
    db.add_log({
        "timestamp": datetime.now().isoformat(),
        "event": "AUTO_MODE_START",
        "user": str(ctx.author)
    })
    
    await ctx.send(embed=embed)
    logger.success("✅ Mode automatique activé")


@bot.command(name="stop")
async def cmd_stop(ctx):
    """Désactive le mode automatique"""
    logger.info(f"⏹️ Commande STOP utilisée par {ctx.author}")
    stats["commands_executed"] += 1
    stats["last_activity"] = datetime.now()
    stats["auto_mode"] = False
    
    embed = discord.Embed(
        title="⏹️ Mode Automatique Désactivé",
        description="Le bot n'est plus en mode automatique",
        color=discord.Color.red(),
        timestamp=datetime.now()
    )
    
    db.add_log({
        "timestamp": datetime.now().isoformat(),
        "event": "AUTO_MODE_STOP",
        "user": str(ctx.author)
    })
    
    await ctx.send(embed=embed)
    logger.warning("⏹️ Mode automatique désactivé")


@bot.command(name="uptime")
async def cmd_uptime(ctx):
    """Affiche le temps d'activité du bot"""
    logger.info(f"⏱️ Commande UPTIME utilisée par {ctx.author}")
    stats["commands_executed"] += 1
    stats["last_activity"] = datetime.now()
    
    uptime = format_uptime(datetime.now() - stats["start_time"])
    
    embed = discord.Embed(
        title="⏱️ Temps d'Activité",
        description=uptime,
        color=discord.Color.blue(),
        timestamp=datetime.now()
    )
    
    embed.add_field(name="Depuis", value=f"<t:{int(stats['start_time'].timestamp())}:F>", inline=False)
    
    await ctx.send(embed=embed)


@bot.command(name="dashboard")
async def cmd_dashboard(ctx):
    """Affiche le panneau Discord"""
    logger.info(f"📊 Commande DASHBOARD utilisée par {ctx.author}")
    stats["commands_executed"] += 1
    stats["last_activity"] = datetime.now()
    
    uptime = format_uptime(datetime.now() - stats["start_time"])
    
    embed = discord.Embed(
        title="🎮 V9 TOOL AI COMMENT BOT - Dashboard",
        description="Panneau de contrôle en temps réel",
        color=discord.Color.dark_blue(),
        timestamp=datetime.now()
    )
    
    # Section Statut
    embed.add_field(
        name="🟢 Statut Global",
        value=f"```\nÉtat: En ligne ✅\nLatence: {bot.latency*1000:.2f}ms\nUptime: {uptime}\n```",
        inline=False
    )
    
    # Section Performance
    embed.add_field(
        name="⚡ Performance",
        value=f"```\nCommandes: {stats['commands_executed']}\nMessages: {stats['messages_analyzed']}\nRéponses: {stats['responses_generated']}\n```",
        inline=False
    )
    
    # Section Réseau
    embed.add_field(
        name="🌐 Réseau",
        value=f"```\nServeurs: {stats['server_count']}\nUtilisateurs: {stats['user_count']}\nMode Auto: {'Actif ✅' if stats['auto_mode'] else 'Inactif ❌'}\n```",
        inline=False
    )
    
    # Section Activité
    embed.add_field(
        name="📋 Dernière Activité",
        value=f"<t:{int(stats['last_activity'].timestamp())}:R>",
        inline=False
    )
    
    embed.set_thumbnail(url=bot.user.avatar.url if bot.user.avatar else None)
    embed.set_footer(text="V9 TOOL AI COMMENT BOT | Termux Android | Mis à jour en temps réel")
    
    await ctx.send(embed=embed)


@bot.command(name="restart")
@commands.has_permissions(administrator=True)
async def cmd_restart(ctx):
    """Redémarre le bot (Admin uniquement)"""
    logger.warning(f"🔄 Commande RESTART utilisée par {ctx.author}")
    stats["commands_executed"] += 1
    
    embed = discord.Embed(
        title="🔄 Redémarrage",
        description="Le bot redémarre... À bientôt!",
        color=discord.Color.orange(),
        timestamp=datetime.now()
    )
    
    db.add_log({
        "timestamp": datetime.now().isoformat(),
        "event": "BOT_RESTART",
        "user": str(ctx.author)
    })
    
    await ctx.send(embed=embed)
    logger.success("🔄 Redémarrage du bot...")
    await bot.close()


# ============= TÂCHES PÉRIODIQUES =============

@tasks.loop(minutes=5)
async def status_panel():
    """Mise à jour du statut du bot toutes les 5 minutes"""
    stats["server_count"] = len(bot.guilds)
    stats["user_count"] = sum(guild.member_count for guild in bot.guilds)
    
    logger.debug(f"📊 Mise à jour: {stats['server_count']} serveurs, {stats['user_count']} utilisateurs")
    
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"{stats['server_count']} serveurs | !help"
        )
    )


# ============= MAIN =============

def main():
    """Fonction principale"""
    try:
        token = config.get("DISCORD_TOKEN")
        if not token:
            logger.error("❌ DISCORD_TOKEN non trouvé dans .env")
            sys.exit(1)
        
        logger.success("🔐 Token Discord chargé")
        logger.info("🔌 Connexion à Discord...")
        
        bot.run(token)
        
    except KeyboardInterrupt:
        logger.warning("⚠️  Arrêt demandé par l'utilisateur")
        sys.exit(0)
    except Exception as e:
        logger.error(f"❌ Erreur fatale: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()