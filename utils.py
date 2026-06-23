#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utilitaires du bot
Logging, formatage, etc.
"""

import os
from datetime import datetime, timedelta


class Logger:
    """Classe de logging personnalisée"""
    
    # Codes de couleur ANSI
    COLORS = {
        "RESET": "\033[0m",
        "RED": "\033[91m",
        "GREEN": "\033[92m",
        "YELLOW": "\033[93m",
        "BLUE": "\033[94m",
        "PURPLE": "\033[95m",
        "CYAN": "\033[96m",
        "GRAY": "\033[90m",
    }
    
    def __init__(self, debug=False):
        """Initialisation du logger"""
        self.debug = debug
    
    def _format_time(self):
        """Formate l'heure actuelle"""
        return datetime.now().strftime("%H:%M:%S")
    
    def _print_log(self, level, message, color):
        """Affiche un log formaté"""
        timestamp = self._format_time()
        reset = self.COLORS["RESET"]
        
        print(f"{color}[{timestamp}] {level}: {message}{reset}")
    
    def info(self, message):
        """Log d'information"""
        self._print_log("INFO", message, self.COLORS["CYAN"])
    
    def success(self, message):
        """Log de succès"""
        self._print_log("SUCCESS", message, self.COLORS["GREEN"])
    
    def warning(self, message):
        """Log d'avertissement"""
        self._print_log("WARNING", message, self.COLORS["YELLOW"])
    
    def error(self, message):
        """Log d'erreur"""
        self._print_log("ERROR", message, self.COLORS["RED"])
    
    def debug(self, message):
        """Log de débogage"""
        if self.debug:
            self._print_log("DEBUG", message, self.COLORS["GRAY"])


def format_uptime(delta):
    """Formate un timedelta en chaîne lisible"""
    total_seconds = int(delta.total_seconds())
    
    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    parts = []
    if days > 0:
        parts.append(f"{days}j")
    if hours > 0:
        parts.append(f"{hours}h")
    if minutes > 0:
        parts.append(f"{minutes}m")
    if seconds > 0 or not parts:
        parts.append(f"{seconds}s")
    
    return " ".join(parts)


def get_ascii_art():
    """Retourne l'ASCII art du bot"""
    art = r"""
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║               ██╗   ██╗███╗   ██╗ █████╗ ████████╗            ║
║               ██║   ██║████╗  ██║██╔══██╗╚══██╔══╝            ║
║               ██║   ██║██╔██╗ ██║███████║   ██║               ║
║               ╚██╗ ██╔╝██║╚██╗██║██╔══██║   ██║               ║
║                ╚████╔╝ ██║ ╚████║██║  ██║   ██║               ║
║                 ╚═══╝  ╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝               ║
║                                                                ║
║          🤖 V9 TOOL AI COMMENT BOT - TERMUX ANDROID 🤖         ║
║                                                                ║
║                    Discord-Powered • Lightweight               ║
║              Zero Web • Zero Dashboard • Pure CLI              ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
    """
    return art


def truncate_string(s, length=100):
    """Tronque une chaîne à la longueur spécifiée"""
    if len(s) > length:
        return s[:length-3] + "..."
    return s


def sanitize_input(text):
    """Nettoie une entrée texte"""
    # Supprimer les caractères de contrôle
    return "".join(char for char in text if ord(char) >= 32 or char in "\n\t")


def format_bytes(bytes_value):
    """Formate des bytes en chaîne lisible"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_value < 1024:
            return f"{bytes_value:.2f} {unit}"
        bytes_value /= 1024
    return f"{bytes_value:.2f} TB"


def get_system_info():
    """Récupère les informations système de base"""
    info = {
        "platform": os.name,
        "python_version": __import__("sys").version.split()[0],
        "timestamp": datetime.now().isoformat()
    }
    return info


class RateLimiter:
    """Classe pour limiter le taux de requêtes"""
    
    def __init__(self, max_calls=10, time_window=60):
        """
        Initialisation du limiteur
        max_calls: nombre maximum d'appels
        time_window: fenêtre de temps en secondes
        """
        self.max_calls = max_calls
        self.time_window = time_window
        self.calls = []
    
    def is_allowed(self):
        """Vérifie si un appel est autorisé"""
        now = datetime.now()
        
        # Supprimer les appels hors de la fenêtre de temps
        self.calls = [call for call in self.calls if (now - call).total_seconds() < self.time_window]
        
        # Vérifier si nous avons dépassé la limite
        if len(self.calls) < self.max_calls:
            self.calls.append(now)
            return True
        
        return False


# Instance globale de logger
logger = Logger()