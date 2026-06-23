# SECURITY.md - Politique de Sécurité

## 🔒 Sécurité

### Stockage du Token

✅ **À faire:**
- Stockez le token dans `.env` (non versionné)
- Utilisez des variables d'environnement
- Gardez `.env` privé

❌ **À ne pas faire:**
- Ne commitez jamais le `.env`
- N'envoyez jamais le token par message
- Ne partagez pas le token

### Permissions Discord

**Le bot requiert:**
- View Channels
- Send Messages
- Read Message History
- Message Content Intent

**Permissions optionnelles:**
- Manage Messages (pour la modération future)
- Kick Members (pour la modération future)

### Protection des Données

✅ **Sécurisé:**
- Tout est stocké localement
- Pas d'envoi à des serveurs externes
- Pas d'API cloud utilisée
- Données SQLite chiffrées optionnellement

### Validation des Entrées

Tous les inputs utilisateur sont validés:
```python
# Sanitisation de l'entrée
truncate_string(content, 5000)  # Max 5000 caractères
sanitize_input(content)         # Supprime caractères contrôle
```

### Gestion des Erreurs

Les erreurs ne révèlent pas d'informations sensibles:
```python
# ❌ Mauvais
except Exception as e:
    await ctx.send(f"Error: {e}")

# ✅ Bon
except Exception as e:
    logger.error(f"Error: {e}")
    await ctx.send("Une erreur est survenue")
```

### Permissions Discord Requises

Assurez-vous que le bot a les permissions:
```
✅ View Channels
✅ Send Messages
✅ Read Message History
✅ Message Content Intent (activé)
```

### Signaler une Vulnérabilité

Si vous découvrez une vulnérabilité:

1. **Ne la publiez pas publiquement**
2. **Envoyez un email** (voir maintainer)
3. **Décrivez en détail**
4. **Nous réparerons rapidement**

---

## 🔐 Bonnes Pratiques

### Environnement Termux Sécurisé

```bash
# Protégez le .env
chmod 600 .env

# Protégez la base de données
chmod 600 data/bot.db

# Protégez les scripts
chmod 700 *.py
```

### Mise à Jour de Sécurité

```bash
# Mettez à jour régulièrement
pip install -r requirements.txt --upgrade

# Vérifiez les vulnérabilités
pip install safety
safety check
```

### Audit de Sécurité

```bash
# Utilisez un outil de scanning
pip install bandit
bandit -r .
```

---

## 🚨 Incidents de Sécurité

### Le token a été exposé

**Actions immédiatement:**

1. **Regénérez le token**
   - https://discord.com/developers/applications
   - Bot → Reset Token

2. **Mettez à jour .env**
   - Ajoutez le nouveau token

3. **Redémarrez le bot**
   ```bash
   python bot.py
   ```

4. **Vérifiez les logs**
   ```bash
   tail -f data/logs.json
   ```

---

**Gaza Tool V9** - Sécurisé par défaut