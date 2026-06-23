#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gestion de la base de données
Stockage des logs et statistiques
"""

import sqlite3
import json
import os
from datetime import datetime
from pathlib import Path


class Database:
    """Classe de gestion de la base de données SQLite"""
    
    def __init__(self, db_path="data/bot.db", logs_path="data/logs.json"):
        """Initialisation de la base de données"""
        self.db_path = db_path
        self.logs_path = logs_path
        
        # Créer le répertoire data s'il n'existe pas
        Path(os.path.dirname(db_path)).mkdir(parents=True, exist_ok=True)
        
        self.init_database()
    
    def get_connection(self):
        """Retourne une connexion à la base de données"""
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            return conn
        except sqlite3.Error as e:
            print(f"❌ Erreur de connexion BDD: {e}")
            return None
    
    def init_database(self):
        """Initialise la base de données"""
        try:
            conn = self.get_connection()
            if conn is None:
                return False
            
            cursor = conn.cursor()
            
            # Table des statistiques
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS statistics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    commands_executed INTEGER DEFAULT 0,
                    messages_analyzed INTEGER DEFAULT 0,
                    responses_generated INTEGER DEFAULT 0,
                    guilds_count INTEGER DEFAULT 0,
                    users_count INTEGER DEFAULT 0
                )
            """)
            
            # Table des événements
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    event_type TEXT NOT NULL,
                    description TEXT,
                    user_id TEXT,
                    user_name TEXT
                )
            """)
            
            # Table des utilisateurs
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    discord_id TEXT UNIQUE NOT NULL,
                    username TEXT NOT NULL,
                    first_seen DATETIME DEFAULT CURRENT_TIMESTAMP,
                    last_seen DATETIME DEFAULT CURRENT_TIMESTAMP,
                    interactions INTEGER DEFAULT 0
                )
            """)
            
            # Table des serveurs
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS guilds (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    guild_id TEXT UNIQUE NOT NULL,
                    guild_name TEXT NOT NULL,
                    joined_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    member_count INTEGER DEFAULT 0,
                    active BOOLEAN DEFAULT 1
                )
            """)
            
            conn.commit()
            conn.close()
            print("✅ Base de données initialisée")
            return True
            
        except sqlite3.Error as e:
            print(f"❌ Erreur initialisation BDD: {e}")
            return False
    
    def add_event(self, event_type, description="", user_id=None, user_name=None):
        """Ajoute un événement à la base de données"""
        try:
            conn = self.get_connection()
            if conn is None:
                return False
            
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO events (event_type, description, user_id, user_name)
                VALUES (?, ?, ?, ?)
            """, (event_type, description, user_id, user_name))
            
            conn.commit()
            conn.close()
            return True
            
        except sqlite3.Error as e:
            print(f"❌ Erreur ajout événement: {e}")
            return False
    
    def add_user(self, discord_id, username):
        """Ajoute ou met à jour un utilisateur"""
        try:
            conn = self.get_connection()
            if conn is None:
                return False
            
            cursor = conn.cursor()
            
            # Vérifier si l'utilisateur existe
            cursor.execute("SELECT id FROM users WHERE discord_id = ?", (discord_id,))
            
            if cursor.fetchone():
                # Mise à jour
                cursor.execute("""
                    UPDATE users SET last_seen = CURRENT_TIMESTAMP, interactions = interactions + 1
                    WHERE discord_id = ?
                """, (discord_id,))
            else:
                # Insertion
                cursor.execute("""
                    INSERT INTO users (discord_id, username)
                    VALUES (?, ?)
                """, (discord_id, username))
            
            conn.commit()
            conn.close()
            return True
            
        except sqlite3.Error as e:
            print(f"❌ Erreur ajout utilisateur: {e}")
            return False
    
    def add_guild(self, guild_id, guild_name, member_count=0):
        """Ajoute ou met à jour un serveur"""
        try:
            conn = self.get_connection()
            if conn is None:
                return False
            
            cursor = conn.cursor()
            
            # Vérifier si le serveur existe
            cursor.execute("SELECT id FROM guilds WHERE guild_id = ?", (guild_id,))
            
            if cursor.fetchone():
                # Mise à jour
                cursor.execute("""
                    UPDATE guilds SET member_count = ?, guild_name = ?
                    WHERE guild_id = ?
                """, (member_count, guild_name, guild_id))
            else:
                # Insertion
                cursor.execute("""
                    INSERT INTO guilds (guild_id, guild_name, member_count)
                    VALUES (?, ?, ?)
                """, (guild_id, guild_name, member_count))
            
            conn.commit()
            conn.close()
            return True
            
        except sqlite3.Error as e:
            print(f"❌ Erreur ajout serveur: {e}")
            return False
    
    def get_statistics(self):
        """Récupère les statistiques actuelles"""
        try:
            conn = self.get_connection()
            if conn is None:
                return None
            
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM statistics
                ORDER BY timestamp DESC
                LIMIT 1
            """)
            
            result = cursor.fetchone()
            conn.close()
            
            return dict(result) if result else None
            
        except sqlite3.Error as e:
            print(f"❌ Erreur récupération stats: {e}")
            return None
    
    def add_log(self, log_data):
        """Ajoute un log au fichier JSON"""
        try:
            # Créer le répertoire s'il n'existe pas
            Path(os.path.dirname(self.logs_path)).mkdir(parents=True, exist_ok=True)
            
            logs = []
            
            # Charger les logs existants
            if os.path.exists(self.logs_path):
                with open(self.logs_path, "r", encoding="utf-8") as f:
                    try:
                        logs = json.load(f)
                    except json.JSONDecodeError:
                        logs = []
            
            # Ajouter le nouveau log
            logs.append(log_data)
            
            # Garder seulement les 1000 derniers logs
            if len(logs) > 1000:
                logs = logs[-1000:]
            
            # Écrire les logs
            with open(self.logs_path, "w", encoding="utf-8") as f:
                json.dump(logs, f, indent=2, ensure_ascii=False)
            
            return True
            
        except Exception as e:
            print(f"❌ Erreur ajout log: {e}")
            return False
    
    def get_logs(self, limit=100):
        """Récupère les derniers logs"""
        try:
            if not os.path.exists(self.logs_path):
                return []
            
            with open(self.logs_path, "r", encoding="utf-8") as f:
                logs = json.load(f)
            
            return logs[-limit:]
            
        except Exception as e:
            print(f"❌ Erreur lecture logs: {e}")
            return []


# Instance globale
db = Database()