# 🤖 GAZA TOOL V9

Un bot Discord puissant, léger et optimisé pour **Termux Android**. Contrôle complet via Discord, **zéro interface web**, **zéro dashboard**, **zéro API FastAPI**. **Système IA avancé intégré** pour analyse et suggestions de commentaires.

## ✨ Caractéristiques

- ✅ **100% CLI** - Contrôle complet depuis le terminal
- ✅ **Discord-Powered** - Commandes via Discord
- ✅ **Léger et Rapide** - Optimisé pour Android/Termux
- ✅ **Zéro Web** - Aucune interface web, aucun dashboard
- ✅ **SQLite + JSON** - Stockage local, aucune base de données externe
- ✅ **Reconnexion Auto** - Gestion complète des erreurs
- ✅ **Logging Propre** - Logs horodatés dans le terminal
- ✅ **Mode Automatique** - Activation/désactivation via commandes
- ✅ **Statistiques** - Uptime, commandes, messages, réponses
- ✅ **Dashboard Discord** - Panneau embed moderne
- ✅ **🧠 Système IA Avancé** - Analyse de contenu + suggestions intelligentes
- ✅ **14 Catégories** - Humour, Sport, Gaming, Religion, Actualité, Musique, Tech, Voyage, Mode, Éducation, Food, Fitness, Beauté, Art
- ✅ **Détection Automatique** - Hashtags, mots-clés, contexte, thème principal
- ✅ **Suggestions Humaines** - 5-20 commentaires variés et naturels
- ✅ **Score Pertinence** - Évaluation de chaque suggestion (0-100%)

## 🚀 Installation sur Termux

### Étape 1: Mettre à jour Termux
```bash
pkg update && pkg upgrade -y
```

### Étape 2: Installer Python 3
```bash
pkg install python -y
```

### Étape 3: Cloner le projet
```bash
cd ~
git clone https://github.com/haza90k-debug/Gaza_Toolv9
cd Gaza_Toolv9
```

### Étape 4: Installer les dépendances
```bash
pip install -r requirements.txt
```

### Étape 5: Configurer le bot
```bash
cp .env.example .env
nano .env
```

**Remplissez vos valeurs dans `.env`:**
- `DISCORD_TOKEN=votre_token_ici`

Pour obtenir votre token Discord:
1. Allez sur https://discord.com/developers/applications
2. Créez une nouvelle application
3. Dans "Bot", créez un bot
4. Copiez le token

### Étape 6: Démarrer le bot
```bash
python bot.py
```

## 📋 Commandes Discord

### Commandes Générales
- `!help` - Affiche cette aide
- `!ping` - Affiche la latence du bot
- `!status` - Affiche le statut du bot
- `!stats` - Affiche les statistiques détaillées
- `!uptime` - Affiche le temps d'activité
- `!dashboard` - Affiche le panneau Discord

### Commandes de Contrôle
- `!start` - Active le mode automatique
- `!stop` - Désactive le mode automatique
- `!restart` - Redémarre le bot (Admin)

### 🧠 Commandes IA (Nouvelles!)
- `!analyse <texte>` - Analyse un contenu (texte, hashtags, URL)
  - Détecte les catégories
  - Extrait les hashtags
  - Identifie les mots-clés
  - Détecte le thème principal
  - Génère un résumé

- `!suggest [nombre]` - Génère des suggestions de commentaires
  - Par défaut: 10 suggestions
  - Min: 5 suggestions
  - Max: 20 suggestions
  - Chaque suggestion a un score de pertinence (0-100%)
  - Les suggestions varient à chaque génération

## 📊 Système IA Détaillé

### Détection de Catégories

Le bot détecte automatiquement les catégories principales du contenu:

| Catégorie | Mots-clés | Emoji |
|-----------|-----------|-------|
| Humour | blague, rire, drôle, marrant, lol | 😂 |
| Sport | foot, basket, tennis, match, équipe | ⚽ |
| Gaming | jeu, game, fps, rpg, streaming, fortnite | 🎮 |
| Religion | dieu, église, prière, foi, spirituel | ✝️ |
| Actualité | news, breaking, nouvelle, événement | 📰 |
| Musique | chanson, musique, artiste, concert, album | 🎵 |
| Technologie | tech, app, software, code, ai, robot | 💻 |
| Voyage | voyage, vacances, destination, plage | ✈️ |
| Mode | vêtement, fashion, style, outfit, tendance | 👗 |
| Éducation | école, cours, apprentissage, étudiant | 📚 |
| Food | nourriture, restaurant, cuisine, recette | 🍽️ |
| Fitness | sport, gym, musculation, workout | 💪 |
| Beauté | beauté, maquillage, skincare, cosmétique | 💄 |
| Art | art, peinture, dessin, créatif, artist | 🎨 |

### Analyse de Contenu

La commande `!analyse` vous fournit:

```
📝 Résumé - Les 250 premiers caractères du contenu
🎯 Thème Principal - La catégorie dominante
📂 Catégories Détectées - Jusqu'à 3 catégories
🔑 Mots-Clés Importants - Les 5 mots les plus fréquents
#️⃣ Hashtags Détectés - Tous les hashtags du texte
📊 Statistiques - Nombre de mots et de caractères
```

### Suggestions Intelligentes

La commande `!suggest` génère des commentaires:

```
✅ Naturels - Ressemblent à de vrais commentaires
✅ Variés - Différents à chaque génération
✅ Adaptés - Basés sur la catégorie détectée
✅ Crédibles - Avec emojis et contexte appropriés
✅ Scorés - Score de pertinence 0-100%
```

### Exemple d'utilisation

```
Utilisateur: !analyse Voilà le meilleur gameplay de Fortnite #gaming #streamer

Bot: 📝 Résumé: Voilà le meilleur gameplay de Fortnite...
🎯 Thème Principal: Gaming
📂 Catégories: Gaming, Sport, Technologie
🔑 Mots-Clés: Gameplay, Fortnite, meilleur
#️⃣ Hashtags: #gaming, #streamer
📊 Mots: 8 | Caractères: 45

Utilisateur: !suggest 10

Bot:
#1 - Gaming
💬 GG! Belle partie! 🎮🔥
📊 Pertinence: [████████░░] 85%

#2 - Gaming
💬 Ton gameplay est fou! 🔥💯
📊 Pertinence: [█████████░] 92%

(... 8 autres suggestions)
```

## 📈 Statistiques Disponibles

Le bot enregistre automatiquement:
- ⏱️ **Uptime** - Temps en ligne
- ⚙️ **Commandes** - Nombre de commandes exécutées
- 💬 **Messages** - Nombre de messages analysés
- 🤖 **Réponses** - Nombre de réponses générées
- 🧠 **Analyses IA** - Nombre d'analyses réalisées
- 💡 **Suggestions IA** - Nombre de suggestions générées
- 📡 **Serveurs** - Nombre de serveurs connectés
- 👥 **Utilisateurs** - Nombre total d'utilisateurs
- 📋 **Dernière Activité** - Quand était la dernière action

## 📁 Structure du Projet

```
Gaza_Toolv9/
├── bot.py              # Fichier principal du bot
├── config.py           # Gestion de la configuration
├── database.py         # Gestion de la base de données
├── utils.py            # Utilitaires et logging
├── ai_analyzer.py      # 🧠 Système IA avancé (NOUVEAU!)
├── requirements.txt    # Dépendances Python
├── .env.example        # Exemple de configuration
├── .env                # Configuration (à créer)
├── .gitignore          # Fichiers à ignorer
├── README.md           # Cette documentation
└── data/
    ├── bot.db          # Base de données SQLite
    └── logs.json       # Logs en JSON
```

## 🔧 Configuration Avancée

Éditez votre `.env` pour personnaliser:

```env
# Token Discord (obligatoire)
DISCORD_TOKEN=votre_token_ici

# Mode débogage
DEBUG=False

# Niveau de logging
LOG_LEVEL=INFO

# Chemins de stockage
DATABASE_PATH=data/bot.db
LOGS_PATH=data/logs.json
```

## 📝 Logging

Les logs sont affichés en temps réel dans le terminal avec:
- 🕐 Horodatage au format HH:MM:SS
- 🎨 Couleurs ANSI pour meilleure lisibilité
- 📊 Différents niveaux: INFO, SUCCESS, WARNING, ERROR, DEBUG

### Exemple de logs:
```
[14:32:45] INFO: 🚀 Démarrage du V9 TOOL AI COMMENT BOT
[14:32:46] SUCCESS: ✅ Bot connecté en tant que Gaza-BOT#1234
[14:32:47] INFO: 📊 Serveurs: 5
[14:32:50] INFO: 📖 Commande HELP utilisée par User#1234
[14:33:00] INFO: 🔍 Commande ANALYSE utilisée par User#1234
[14:33:01] SUCCESS: ✅ Analyse complétée - Thème: Gaming
[14:33:05] INFO: 💡 Commande SUGGEST utilisée par User#1234
[14:33:06] SUCCESS: ✅ 10 suggestions générées
```

## 💾 Base de Données

### SQLite (`data/bot.db`)
Stocke les données persistantes:
- **statistics** - Statistiques du bot
- **events** - Événements et actions
- **users** - Utilisateurs et interactions
- **guilds** - Serveurs Discord

### JSON (`data/logs.json`)
Conserve les 1000 derniers événements:
- Connexions/déconnexions
- Activation/désactivation du mode auto
- Analyses IA réalisées
- Suggestions générées
- Redémarrages
- Événements personnalisés

## 🛡️ Gestion des Erreurs

Le bot gère automatiquement:
- ✅ Reconnexion en cas de déconnexion
- ✅ Erreurs de commandes
- ✅ Arguments manquants
- ✅ Permissions insuffisantes
- ✅ Timeouts et erreurs réseau
- ✅ Erreurs d'analyse IA
- ✅ Erreurs de génération de suggestions

## 🔐 Sécurité

- ✅ Token stocké localement dans `.env` (non versionné)
- ✅ Pas d'envoi de données à des serveurs externes
- ✅ Contrôle d'accès administrateur pour les commandes sensibles
- ✅ Validation des entrées utilisateur
- ✅ Analyse de contenu locale (pas de cloud)

## 📱 Optimisation Termux Android

Le bot est optimisé pour:
- ✅ Consommation RAM faible (~50-100MB)
- ✅ Pas de serveur web (moins de ressources)
- ✅ Base de données SQLite légère
- ✅ Logs JSON compacts
- ✅ Pas de dépendances externes lourdes
- ✅ Système IA intégré (pas d'API externe)
- ✅ Analyse instantanée du contenu

## 🐛 Dépannage

### Le bot ne démarre pas
```bash
# Vérifiez votre token
nano .env

# Vérifiez les dépendances
pip install -r requirements.txt --upgrade

# Lancez en mode debug
DEBUG=True python bot.py
```

### Erreur de connexion Discord
```bash
# Vérifiez votre connexion internet
ping discord.com

# Vérifiez le token dans le portail développeur Discord
```

### L'analyse IA ne fonctionne pas
```bash
# Vérifiez que ai_analyzer.py existe
ls -la ai_analyzer.py

# Relancez le bot
python bot.py
```

### La base de données est corrompue
```bash
# Supprimez la base de données
rm data/bot.db

# Relancez le bot pour la recréer
python bot.py
```

## 📦 Dépendances

- **discord.py** (2.3.2) - Client Discord API
- **python-dotenv** (1.0.0) - Gestion .env
- **aiohttp** (3.9.0) - Requêtes HTTP asynchrones
- **sqlite3** - Intégré à Python
- **json** - Intégré à Python
- **collections** - Intégré à Python
- **re** - Intégré à Python
- **random** - Intégré à Python

Toutes les dépendances sont légères et optimisées pour Android.

## 🚀 Utilisation en Production

### Garder le bot actif sur Termux

Utilisez `tmux` ou `screen`:

```bash
# Avec tmux
pkg install tmux -y
tmux new-session -d -s bot "cd ~/Gaza_Toolv9 && python bot.py"

# Vérifier le statut
tmux list-sessions

# Se connecter
tmux attach-session -t bot

# Quitter (Ctrl+B puis D)
```

### Lancer au démarrage

Créez un script de démarrage:
```bash
cat > ~/.bashrc << 'EOF'
# Démarrer le bot au login
if [ -z "$TMUX" ]; then
    cd ~/Gaza_Toolv9
    tmux new-session -d -s bot "python bot.py"
fi
EOF
```

## 🎯 Exemples d'Utilisation

### Analyse d'un TikTok
```
!analyse J'ai trouvé ce hack incroyable sur TikTok #tiktok #hack #viral 🔥

Résultat:
- Thème: Technologie / Viral
- Mots-clés: Hack, Incroyable, TikTok
- Hashtags: #tiktok, #hack, #viral
```

### Analyse d'un post gaming
```
!analyse GG à mon équipe! Match incroyable sur Fortnite, on a gagné le tournoi! #Esport #Gaming

Résultat:
- Thème: Gaming
- Catégories: Gaming, Sport
- Mots-clés: GG, Match, Fortnite, Équipe
```

### Génération de suggestions
```
!suggest 15

Résultat: 15 commentaires variés et naturels avec scores de pertinence
```

## 📄 Licence

Ce projet est sous licence MIT. Voir LICENSE pour plus de détails.

## 🤝 Contributions

Les contributions sont les bienvenues! N'hésitez pas à:
- 🐛 Signaler des bugs
- ✨ Proposer des améliorations
- 🔧 Envoyer des pull requests
- 🧠 Ajouter de nouvelles catégories IA

## 📞 Support

Pour l'aide:
1. Consultez la documentation Discord.py: https://discordpy.readthedocs.io/
2. Vérifiez les logs avec `tail -f data/logs.json`
3. Lancez en mode debug: `DEBUG=True python bot.py`
4. Consultez les exemples ci-dessus

## 🎯 Roadmap Futur

- [ ] Support d'URLs directes (TikTok, Instagram, YouTube)
- [ ] Cache d'analyses pour performances
- [ ] Système de plugins pour nouvelles catégories
- [ ] Modération automatique
- [ ] Système de récompenses
- [ ] Support multilingue
- [ ] Webhooks personnalisés
- [ ] Interface Web optionnelle
- [ ] API REST légère
- [ ] Dashboard en ligne optionnel

---

**GAZA TOOL V9** - Fait avec ❤️ pour Termux Android

**Version:** 1.1 avec système IA avancé 🧠

**Dernière mise à jour:** 23 Juin 2026