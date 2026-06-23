#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Installation et Configuration - Gaza Tool V9
Script d'installation automatique pour Termux
"""

import os
import sys
import subprocess
from pathlib import Path


def print_header():
    """Affiche l'en-tête"""
    header = r"""
╔════════════════════════════════════════════════╗
║                                                ║
║    🤖 GAZA TOOL V9 - Installation Setup 🤖    ║
║                                                ║
║         AI Comment Bot for Termux Android      ║
║                                                ║
╚════════════════════════════════════════════════╝
    """
    print(header)


def check_python():
    """Vérifie la version de Python"""
    print("\n[1/5] Vérification de Python...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor} OK")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor} - Python 3.8+ requis")
        return False


def create_directories():
    """Crée les répertoires nécessaires"""
    print("\n[2/5] Création des répertoires...")
    dirs = ["data", "logs"]
    for dir_name in dirs:
        Path(dir_name).mkdir(exist_ok=True)
        print(f"✅ {dir_name}/ créé")


def install_requirements():
    """Installe les dépendances"""
    print("\n[3/5] Installation des dépendances...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dépendances installées")
        return True
    except subprocess.CalledProcessError:
        print("❌ Erreur lors de l'installation")
        return False


def create_env_file():
    """Crée le fichier .env"""
    print("\n[4/5] Configuration du fichier .env...")
    
    if os.path.exists(".env"):
        print("⚠️  .env existe déjà")
        return True
    
    # Copier depuis .env.example
    try:
        with open(".env.example", "r") as f:
            content = f.read()
        
        with open(".env", "w") as f:
            f.write(content)
        
        print("✅ .env créé depuis .env.example")
        print("⚠️  IMPORTANT: Éditez .env et ajoutez votre DISCORD_TOKEN")
        return True
    except FileNotFoundError:
        print("❌ .env.example non trouvé")
        return False


def verify_files():
    """Vérifie les fichiers nécessaires"""
    print("\n[5/5] Vérification des fichiers...")
    
    required_files = [
        "bot.py",
        "config.py",
        "database.py",
        "utils.py",
        "ai_analyzer.py",
        "requirements.txt",
        ".env.example",
        "README.md"
    ]
    
    all_ok = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - MANQUANT")
            all_ok = False
    
    return all_ok


def print_next_steps():
    """Affiche les prochaines étapes"""
    next_steps = """
╔════════════════════════════════════════════════╗
║          🎉 Installation Terminée! 🎉         ║
╚════════════════════════════════════════════════╝

📋 PROCHAINES ÉTAPES:

1️⃣  Éditez votre fichier .env:
    nano .env
    
    Ajoutez votre DISCORD_TOKEN:
    DISCORD_TOKEN=votre_token_ici

2️⃣  Obtenez votre token Discord:
    https://discord.com/developers/applications
    → Créer une app
    → Ajouter un bot
    → Copier le token

3️⃣  Lancez le bot:
    python bot.py

4️⃣  Utilisez les commandes:
    !help              - Aide
    !analyse <texte>   - Analyser contenu
    !suggest [nombre]  - Suggestions de commentaires
    !dashboard         - Panneau de contrôle
    !stats             - Statistiques

📚 Documentation: README.md
🐛 Problèmes? Consultez CONTRIBUTING.md

🚀 Bon usage de Gaza Tool V9!
    """
    print(next_steps)


def main():
    """Fonction principale"""
    print_header()
    
    # Vérification de Python
    if not check_python():
        sys.exit(1)
    
    # Création des répertoires
    create_directories()
    
    # Installation des dépendances
    if not install_requirements():
        print("⚠️  Continuons malgré tout...")
    
    # Configuration .env
    create_env_file()
    
    # Vérification des fichiers
    if verify_files():
        print_next_steps()
    else:
        print("\n❌ Certains fichiers sont manquants!")
        sys.exit(1)


if __name__ == "__main__":
    main()
