#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuration du bot
Gestion des variables d'environnement
"""

import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()


class Config:
    """Classe de gestion de configuration"""
    
    def __init__(self):
        """Initialisation de la configuration"""
        self.discord_token = os.getenv("DISCORD_TOKEN")
        self.debug = os.getenv("DEBUG", "False").lower() == "true"
        self.log_level = os.getenv("LOG_LEVEL", "INFO")
        self.database_path = os.getenv("DATABASE_PATH", "data/bot.db")
        self.logs_path = os.getenv("LOGS_PATH", "data/logs.json")
    
    def get(self, key):
        """Récupère une variable de configuration"""
        key_upper = key.upper()
        
        config_map = {
            "DISCORD_TOKEN": self.discord_token,
            "DEBUG": self.debug,
            "LOG_LEVEL": self.log_level,
            "DATABASE_PATH": self.database_path,
            "LOGS_PATH": self.logs_path,
        }
        
        return config_map.get(key_upper)
    
    def validate(self):
        """Valide la configuration"""
        errors = []
        
        if not self.discord_token:
            errors.append("❌ DISCORD_TOKEN manquant dans .env")
        
        if errors:
            for error in errors:
                print(error)
            return False
        
        return True


# Instance globale
config = Config()