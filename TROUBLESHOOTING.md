# TROUBLESHOOTING.md - Résolution de Problèmes

## 🔴 Problèmes Courants

### Le bot ne démarre pas

**Symptôme:** Erreur au lancement

**Solutions:**

1. **Vérifiez Python 3.8+**
```bash
python --version
# Doit afficher: Python 3.X.X (X >= 8)
```

2. **Vérifiez les dépendances**
```bash
pip install -r requirements.txt --upgrade
```

3. **Testez les imports**
```bash
python -c "import discord; print('discord.py OK')"
python -c "from dotenv import load_dotenv; print('python-dotenv OK')"
```

4. **Vérifiez le .env**
```bash
cat .env
# Doit contenir: DISCORD_TOKEN=votre_token
```

---

### Erreur: "discord.py not found"

**Cause:** discord.py n'est pas installé

**Solution:**
```bash
pip install discord.py==2.3.2
python bot.py
```

---

### Erreur: "Token is invalid"

**Cause:** Le token Discord est invalide ou expiré

**Solutions:**

1. **Obtenez un nouveau token**
   - Allez sur https://discord.com/developers/applications
   - Sélectionnez votre application
   - Allez à "Bot" → "TOKEN" → "Reset Token"
   - Copiez le nouveau token

2. **Mettez à jour le .env**
```bash
nano .env
# Remplacez DISCORD_TOKEN par le nouveau
```

3. **Relancez le bot**
```bash
python bot.py
```

---

### Erreur: "DISCORD_TOKEN not found in .env"

**Cause:** Le fichier .env n'existe pas ou est mal configuré

**Solutions:**

1. **Créez le .env**
```bash
cp .env.example .env
```

2. **Éditez le .env**
```bash
nano .env
# Ajoutez votre token après le signe "="
```

3. **Vérifiez le format**
```bash
cat .env | grep DISCORD_TOKEN
# Doit afficher: DISCORD_TOKEN=votre_token_sans_espace
```

---

### Le bot se connecte mais ne répond pas

**Cause:** Permissions insuffisantes ou bot mal configuré

**Solutions:**

1. **Vérifiez les permissions Discord**
   - Allez dans votre serveur
   - Paramètres → Rôles
   - Assignez les permissions au bot:
     - View Channels
     - Send Messages
     - Read Message History
     - Use Application Commands

2. **Vérifiez que les intents sont activés**
   - https://discord.com/developers/applications
   - Votre app → Bot → Scroll down → Intents
   - Activez:
     - Message Content Intent
     - Server Members Intent

3. **Relancez le bot**
```bash
python bot.py
```

---

### Erreur: "Command not recognized"

**Cause:** Le préfixe de commande n'est pas reconnu

**Solution:** Assurez-vous d'utiliser le bon préfixe
```
✅ !help
❌ /help
❌ >help
```

---

### La base de données est corrompue

**Symptôme:** Erreurs SQLite ou logs vides

**Solutions:**

1. **Supprimez la base de données**
```bash
rm data/bot.db
rm data/logs.json
```

2. **Relancez le bot**
```bash
python bot.py
# Les bases seront recréées automatiquement
```

---

### L'analyse IA ne fonctionne pas

**Symptôme:** Erreur avec !analyse ou !suggest

**Solutions:**

1. **Vérifiez que ai_analyzer.py existe**
```bash
ls -la ai_analyzer.py
```

2. **Testez le module IA**
```bash
python -c "from ai_analyzer import analyzer; print('IA OK')"
```

3. **Vérifiez les imports dans bot.py**
```bash
grep "ai_analyzer" bot.py
```

4. **Relancez le bot**
```bash
python bot.py
```

---

### Performance lente ou bot lag

**Symptôme:** Commandes lentes à répondre

**Causes possibles:**
- Trop de logs accumulés
- Base de données trop grande
- Connexion internet faible

**Solutions:**

1. **Nettoyez les logs**
```bash
rm data/logs.json
```

2. **Nettoyez la base de données**
```bash
rm data/bot.db
python bot.py
# Recréation automatique
```

3. **Vérifiez votre connexion**
```bash
ping discord.com
# Doit montrer des réponses
```

4. **Redémarrez le bot**
```bash
# Ctrl+C pour arrêter
# python bot.py pour relancer
```

---

### Erreur: "Memory error" ou "Out of memory"

**Cause:** Trop de RAM utilisée

**Solutions:**

1. **Nettoyez les logs**
```bash
rm data/logs.json
```

2. **Limitez la taille des logs**
Dans database.py, réduisez:
```python
if len(logs) > 500:  # Au lieu de 1000
    logs = logs[-500:]
```

3. **Relancez le bot**
```bash
python bot.py
```

---

### Erreur: "Connection timeout"

**Cause:** Problème de connexion à Discord

**Solutions:**

1. **Vérifiez votre connexion internet**
```bash
ping google.com
```

2. **Vérifiez que Discord est accessible**
```bash
ping discord.com
```

3. **Attendez quelques secondes et relancez**
```bash
python bot.py
```

4. **Vérifiez si Discord est en panne**
   - Consultez https://status.discord.com/

---

### Les suggestions IA sont répétitives

**Cause:** Normal - les suggestions sont limitées par catégorie

**Solutions:**

1. **Générez plus (max 20)**
```
!suggest 20
```

2. **Analysez un contenu différent**
```
!analyse [nouveau contenu]
!suggest 10
```

3. **Attendez que le cache se réinitialise** (automatique)

---

### Le bot n'analyse pas correctement les catégories

**Cause:** Contenu ambigü ou mots-clés insuffisants

**Solutions:**

1. **Utilisez plus de mots-clés**
```
✅ !analyse Voilà mon meilleur gameplay de Fortnite, incroyable! #gaming #streamer
❌ !analyse Fortnite
```

2. **Ajoutez des hashtags**
```
!analyse Mon contenu #categorie #tags
```

3. **Utilisez des mots-clés spécifiques**
   - Consultez USAGE.md pour les mots-clés par catégorie

---

## 🟡 Avertissements (non-bloquants)

### Avertissement: "Bot is already running"

**Cause:** Un autre processus du bot est actif

**Solutions:**

1. **Trouvez le processus**
```bash
ps aux | grep bot.py
```

2. **Arrêtez-le**
```bash
kill -9 PID
```

3. **Relancez**
```bash
python bot.py
```

---

### Avertissement: "Low memory available"

**Cause:** Peu de RAM disponible sur Termux

**Solutions:**

1. **Fermez les applications inutiles**

2. **Nettoyez le cache Termux**
```bash
pkg clean
```

3. **Libérez de la RAM**
```bash
sync && echo 3 > /proc/sys/vm/drop_caches  # Sur Linux
```

---

## 📊 Vérification de Santé

### Exécutez les tests

```bash
python test.py
```

**Résultat attendu:**
```
✅ PASS - Imports
✅ PASS - Fichiers
✅ PASS - IA Analyzer
✅ PASS - Configuration
✅ PASS - Database

Total: 5/5 tests réussis
🎉 Tous les tests sont passés!
```

---

## 🆘 Aide Avancée

### Mode Debug

```bash
DEBUG=True python bot.py
```

Cela affichera des logs supplémentaires pour le débogage.

### Vérifiez les logs

```bash
tail -f data/logs.json
```

Affiche les 100 derniers événements.

### Réinitialisez complètement

```bash
# Arrêtez le bot (Ctrl+C)

# Supprimez tout
rm -rf data/
mkdir data

# Relancez
python bot.py
```

---

## 📞 Besoin d'Aide?

- 📖 Consultez README.md
- 🚀 Consultez USAGE.md
- 💻 Consultez CONTRIBUTING.md
- 🐛 Ouvrez une GitHub Issue
- 💬 Posez une question

---

**Gaza Tool V9** - Support complet