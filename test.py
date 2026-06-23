#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de test - Gaza Tool V9
Vérification que tous les modules fonctionnent correctement
"""

import sys
import os
from pathlib import Path


def test_imports():
    """Teste les imports"""
    print("[1] Test des imports...")
    try:
        import discord
        print("✅ discord.py")
    except ImportError as e:
        print(f"❌ discord.py - {e}")
        return False
    
    try:
        from dotenv import load_dotenv
        print("✅ python-dotenv")
    except ImportError as e:
        print(f"❌ python-dotenv - {e}")
        return False
    
    try:
        from config import Config
        print("✅ config.py")
    except ImportError as e:
        print(f"❌ config.py - {e}")
        return False
    
    try:
        from database import Database
        print("✅ database.py")
    except ImportError as e:
        print(f"❌ database.py - {e}")
        return False
    
    try:
        from utils import Logger, format_uptime, get_ascii_art
        print("✅ utils.py")
    except ImportError as e:
        print(f"❌ utils.py - {e}")
        return False
    
    try:
        from ai_analyzer import analyzer
        print("✅ ai_analyzer.py")
    except ImportError as e:
        print(f"❌ ai_analyzer.py - {e}")
        return False
    
    return True


def test_files():
    """Teste les fichiers de configuration"""
    print("\n[2] Test des fichiers...")
    
    if os.path.exists(".env"):
        print("✅ .env existe")
    else:
        print("⚠️  .env n'existe pas (créez-le depuis .env.example)")
    
    if os.path.exists(".env.example"):
        print("✅ .env.example existe")
    else:
        print("❌ .env.example manquant")
        return False
    
    if os.path.exists("requirements.txt"):
        print("✅ requirements.txt existe")
    else:
        print("❌ requirements.txt manquant")
        return False
    
    return True


def test_ai_analyzer():
    """Teste le système IA"""
    print("\n[3] Test du système IA...")
    try:
        from ai_analyzer import analyzer
        
        # Test analyse
        test_content = "Voilà le meilleur gameplay de Fortnite #gaming #streamer"
        analysis = analyzer.analyze(test_content)
        
        print(f"✅ Analyse: {analysis['main_theme'].upper()}")
        print(f"   - Catégories: {', '.join(analysis['categories'])}")
        print(f"   - Hashtags: {', '.join(analysis['hashtags'])}")
        print(f"   - Mots-clés: {', '.join(analysis['keywords'])}")
        
        # Test suggestions
        suggestions = analyzer.suggest(analysis, count=5)
        print(f"✅ Suggestions générées: {len(suggestions)}")
        for i, sugg in enumerate(suggestions[:3], 1):
            print(f"   {i}. [{sugg['relevance_score']}%] {sugg['text'][:40]}...")
        
        return True
    except Exception as e:
        print(f"❌ Erreur IA: {e}")
        return False


def test_config():
    """Teste la configuration"""
    print("\n[4] Test de la configuration...")
    try:
        from config import Config
        config = Config()
        
        if config.discord_token:
            print("✅ DISCORD_TOKEN configuré")
        else:
            print("⚠️  DISCORD_TOKEN non configuré (.env)")
        
        print(f"✅ LOG_LEVEL: {config.log_level}")
        print(f"✅ DATABASE_PATH: {config.database_path}")
        print(f"✅ DEBUG: {config.debug}")
        
        return True
    except Exception as e:
        print(f"❌ Erreur config: {e}")
        return False


def test_database():
    """Teste la base de données"""
    print("\n[5] Test de la base de données...")
    try:
        from database import Database
        db = Database("data/test.db", "data/test_logs.json")
        
        print("✅ Base de données initialisée")
        
        # Test log
        db.add_log({"test": "success", "timestamp": "now"})
        logs = db.get_logs(limit=1)
        if logs:
            print("✅ Logs fonctionnels")
        else:
            print("❌ Logs non fonctionnels")
        
        # Nettoyer
        os.remove("data/test.db")
        os.remove("data/test_logs.json")
        
        return True
    except Exception as e:
        print(f"❌ Erreur database: {e}")
        return False


def main():
    """Fonction principale"""
    print("""
╔════════════════════════════════════════════════╗
║      🧪 Tests - Gaza Tool V9 🧪              ║
╚════════════════════════════════════════════════╝
""")
    
    results = []
    
    # Exécuter tous les tests
    results.append(("Imports", test_imports()))
    results.append(("Fichiers", test_files()))
    results.append(("IA Analyzer", test_ai_analyzer()))
    results.append(("Configuration", test_config()))
    results.append(("Database", test_database()))
    
    # Résumé
    print("\n" + "="*50)
    print("📊 RÉSUMÉ DES TESTS")
    print("="*50)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
    
    print(f"\nTotal: {passed}/{total} tests réussis")
    
    if passed == total:
        print("\n🎉 Tous les tests sont passés!")
        print("Vous pouvez maintenant lancer: python bot.py")
        return 0
    else:
        print("\n⚠️  Certains tests ont échoué")
        print("Consultez les erreurs ci-dessus")
        return 1


if __name__ == "__main__":
    sys.exit(main())
