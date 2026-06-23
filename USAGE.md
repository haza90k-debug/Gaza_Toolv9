# USAGE.md - Guide d'Utilisation Complet

## 🚀 Démarrage Rapide

### Installation en 1 minute

```bash
# 1. Cloner le repo
git clone https://github.com/haza90k-debug/Gaza_Toolv9
cd Gaza_Toolv9

# 2. Installer (automatique)
python setup.py

# 3. Configurer
nano .env
# Ajouter: DISCORD_TOKEN=votre_token

# 4. Lancer
python bot.py
```

### Tester avant de lancer

```bash
python test.py
# ✅ Tous les tests doivent passer
```

---

## 📋 Commandes Disponibles

### 🔧 Commandes de Base

#### !help
Affiche la liste complète des commandes
```
!help
```
**Réponse:**
```
📖 V9 TOOL AI COMMENT BOT - Commandes
!help - Affiche cette aide
!ping - Affiche la latence du bot
!status - Affiche le statut du bot
... (liste complète)
```

#### !ping
Affiche la latence du bot
```
!ping
```
**Réponse:**
```
🏓 Pong!
Latence: 125.45ms
```

#### !status
Affiche le statut actuel du bot
```
!status
```
**Réponse:**
```
📊 Statut du Bot
🟢 Statut: En ligne
⏱️ Uptime: 2h 30m 15s
🏓 Latence: 125.45ms
📡 Serveurs: 5
👥 Utilisateurs: 250
🤖 Mode Auto: ✅ Actif
```

#### !stats
Affiche les statistiques détaillées
```
!stats
```
**Réponse:**
```
📈 Statistiques Détaillées
⏱️ Temps en ligne: 2h 30m 15s
⚙️ Commandes exécutées: 45
💬 Messages analysés: 12
🤖 Réponses générées: 150
🧠 Analyses IA: 12
💡 Suggestions IA: 150
🔄 Dernière activité: 2 minutes
📡 Serveurs connectés: 5
👥 Utilisateurs total: 250
```

#### !uptime
Affiche le temps d'activité
```
!uptime
```
**Réponse:**
```
⏱️ Temps d'Activité
2h 30m 15s
Depuis: 23 Juin 2026 à 14:32:45
```

#### !dashboard
Affiche le panneau de contrôle complet
```
!dashboard
```
**Réponse:**
```
🎮 V9 TOOL AI COMMENT BOT - Dashboard

🟢 Statut Global
État: En ligne ✅
Latence: 125.45ms
Uptime: 2h 30m 15s

⚡ Performance
Commandes: 45
Messages: 12
Réponses: 150

🧠 Système IA
Analyses: 12
Suggestions: 150
Mode Auto: Actif ✅

🌐 Réseau
Serveurs: 5
Utilisateurs: 250

📋 Dernière Activité
2 minutes
```

### 🧠 Commandes IA (Nouvelles!)

#### !analyse <texte>
Analyse un contenu et détecte automatiquement:
- Catégories
- Hashtags
- Mots-clés
- Thème principal

**Exemples:**

```
!analyse Voilà le meilleur gameplay de Fortnite #gaming #streamer 🔥
```
**Réponse:**
```
🔍 Analyse du Contenu

📝 Résumé
Voilà le meilleur gameplay de Fortnite #gaming #streamer 🔥

🎯 Thème Principal
Gaming

📂 Catégories Détectées
Gaming, Sport, Technologie

🔑 Mots-Clés Importants
gameplay, fortnite, meilleur, streamer, gaming

#️⃣ Hashtags Détectés
#gaming, #streamer

📊 Statistiques
Mots: 8
Longueur: 55 caractères
```

```
!analyse J'ai trouver ce hack incroyable sur TikTok! #tiktok #hack #viral 🤯
```
**Réponse:**
```
🎯 Thème Principal: Technologie
📂 Catégories: Technologie, Viral, Actualité
🔑 Mots-Clés: hack, tiktok, incroyable
```

```
!analyse GG à mon équipe! Match incroyable, on a gagné le tournoi! #Esport
```
**Réponse:**
```
🎯 Thème Principal: Sport
📂 Catégories: Sport, Gaming, Compétition
🔑 Mots-Clés: match, équipe, gagné, tournoi
```

#### !suggest [nombre]
Génère des suggestions de commentaires
- Nombre par défaut: 10
- Min: 5 suggestions
- Max: 20 suggestions

**Usage:**

```
!suggest
# Génère 10 suggestions (défaut)
```

```
!suggest 15
# Génère 15 suggestions
```

```
!suggest 5
# Génère 5 suggestions
```

**Exemple complet:**

```
!analyse Meilleur gameplay Fortnite #gaming
!suggest 10
```

**Réponse:**
```
💡 Suggestions de Commentaires
10 suggestions adaptées au contenu

#1 - Gaming
💬 GG! Belle partie! 🎮🔥
📊 Pertinence: [████████░░] 85%

#2 - Gaming
💬 Ton gameplay est fou! 🔥💯
📊 Pertinence: [█████████░] 92%

#3 - Gaming
💬 Je veux devenir aussi bon! 💪
📊 Pertinence: [██████████] 100%

#4 - Gaming
💬 Streaming légendaire 🎯
📊 Pertinence: [████████░░] 80%

#5 - Gaming
💬 Cette mécanique est dingue! 🚀
📊 Pertinence: [█████████░] 88%

#6 - Gaming
💬 Je dois absolument essayer ça 🎮✨
📊 Pertinence: [████████░░] 82%

#7 - Gaming
💬 Les meilleurs highlights du jour! ⭐
📊 Pertinence: [█████████░] 90%

#8 - Gaming
💬 Quel talent! Respect! 👑
📊 Pertinence: [██████████] 100%

#9 - Gaming
💬 Je reviens regarder ça ce soir 🍿
📊 Pertinence: [████████░░] 78%

#10 - Gaming
💬 Multiplayer goals! 💯
📊 Pertinence: [█████████░] 89%
```

### 🎛️ Commandes de Contrôle

#### !start
Active le mode automatique
```
!start
```
**Réponse:**
```
▶️ Mode Automatique Activé
Le bot est maintenant en mode automatique
```

#### !stop
Désactive le mode automatique
```
!stop
```
**Réponse:**
```
⏹️ Mode Automatique Désactivé
Le bot n'est plus en mode automatique
```

#### !restart
Redémarre le bot (Admin uniquement)
```
!restart
```
**Réponse:**
```
🔄 Redémarrage
Le bot redémarre... À bientôt!
```

---

## 📚 Cas d'Utilisation Pratiques

### Cas 1: Analyser et générer des commentaires

```bash
# Étape 1: Analyser le contenu
!analyse Mon nouveau clip TikTok est en ligne! Venez le voir #TikTok #Viral #NewClip

# Réponse: Détection d'une vidéo virale
# Thème: Viral/Entertainment

# Étape 2: Générer des suggestions
!suggest 15

# Réponse: 15 commentaires adaptés à un contenu viral
```

### Cas 2: Contenu Gaming

```bash
!analyse Nouvelle video gaming: J'ai battu le meilleur joueur! #Esport #Gaming #Champion
!suggest 12

# Réponse: Suggestions de commentaires pour gaming
# Inclut: GG, gameplay, streaming, tournament, etc.
```

### Cas 3: Contenu Éducatif

```bash
!analyse Tutoriel complet Python pour débutants #Python #Programming #Education
!suggest 10

# Réponse: Suggestions éducatives
# Inclut: apprentissage, clair, utile, merci, etc.
```

### Cas 4: Contenu Musical

```bash
!analyse Nouvelle chanson de Shakira 🎵 Elle chante trop bien! #Music #NewSong #Artiste
!suggest 10

# Réponse: Suggestions musicales
# Inclut: chanson, album, concert, clip, artiste, etc.
```

### Cas 5: Contenu Voyage

```bash
!analyse Vacances en Maldives! Plages magnifiques et couchers de soleil 🌅 #Travel #Paradise
!suggest 10

# Réponse: Suggestions de voyage
# Inclut: destination, plage, voyage, rêve, paradis, etc.
```

---

## 🧠 Catégories IA Détaillées

### Humour
**Mots-clés détectés:** blague, rire, drôle, marrant, lol, mdr, funny
**Suggestions incluses:**
- "Je me suis éclaté en regardant ça! 😂"
- "Hahahaha c'est trop drôle! 🤣"
- "Je suis mort de rire 💀"

### Sport
**Mots-clés détectés:** foot, basket, tennis, match, équipe, but, victoire
**Suggestions incluses:**
- "Belle performance! 💪"
- "Quel match incroyable! 🔥"
- "Respect à ce joueur! 👏"

### Gaming
**Mots-clés détectés:** jeu, game, fps, rpg, streaming, fortnite, minecraft
**Suggestions incluses:**
- "GG! Belle partie! 🎮"
- "Ton gameplay est fou! 🔥"
- "Streaming légendaire 🎯"

### Musique
**Mots-clés détectés:** chanson, musique, artiste, concert, album, clip, singer
**Suggestions incluses:**
- "Quelle chanson de feu! 🔥🎵"
- "Artiste de talent! ⭐"
- "Je mets en boucle! 🔁"

### Technologie
**Mots-clés détectés:** tech, app, software, code, ai, robot, innovation
**Suggestions incluses:**
- "Innovation impressionnante! 🚀"
- "Voilà le futur! 🤖"
- "Vraiment révolutionnaire! 🌟"

### Voyage
**Mots-clés détectés:** voyage, vacances, destination, tourisme, plage
**Suggestions incluses:**
- "Destination de rêve! ✈️"
- "Vue magnifique! 😍"
- "Je veux y aller! 🌍"

### Mode
**Mots-clés détectés:** vêtement, fashion, style, outfit, tendance
**Suggestions incluses:**
- "Style impeccable! 🔥"
- "Outfit parfait! 👗"
- "Fashion goals! 👑"

### Éducation
**Mots-clés détectés:** école, cours, apprentissage, étudiant, prof
**Suggestions incluses:**
- "Merci pour cette explication! 📚"
- "Très pédagogue! 👍"
- "Meilleur tuto jamais! 🏆"

### Food
**Mots-clés détectés:** nourriture, restaurant, cuisine, recette, délicieux
**Suggestions incluses:**
- "J'ai faim maintenant! 😋"
- "Ça a l'air délicieux! 🤤"
- "À tester absolument! ✨"

### Fitness
**Mots-clés détectés:** sport, gym, musculation, workout, entraînement
**Suggestions incluses:**
- "Inspi muscu! 💪"
- "Belle séance! 🏋️"
- "Résultats incroyables! 🤯"

### Beauté
**Mots-clés détectés:** beauté, maquillage, skincare, cosmétique, makeup
**Suggestions incluses:**
- "Peau magnifique! ✨"
- "Tuto makeup parfait! 💄"
- "Transformation incroyable! 🤯"

### Art
**Mots-clés détectés:** art, peinture, dessin, créatif, artist
**Suggestions incluses:**
- "Oeuvre d'art! 🎨"
- "Talent remarquable! 👏"
- "À exposer au musée! 🖼️"

### Religion
**Mots-clés détectés:** dieu, église, prière, foi, spirituel
**Suggestions incluses:**
- "Blessed! 🙏"
- "Amen! ✨"
- "Spiritualité pure! 💜"

### Actualité
**Mots-clés détectés:** news, breaking, nouvelle, événement, important
**Suggestions incluses:**
- "Merci de partager cette info! 📰"
- "C'est très important! ✊"
- "À partager absolument! 🔄"

---

## 📊 Système de Score de Pertinence

Chaque suggestion reçoit un score **0-100%** basé sur:

| Critère | Points | Détails |
|---------|--------|----------|
| Score de base | 50 | Tous les commentaires commencent à 50% |
| Emojis | +20 max | 5 points par emoji (max 20) |
| Hashtags du contenu | +15 par | Si la suggestion contient un hashtag du post |
| Mots-clés | +10 par | Si la suggestion mentionne un mot-clé du post |
| **Total max** | **100%** | Cap à 100% |

**Exemple:**
```
Contenu analysé: "Mon nouveau gameplay Fortnite #gaming #streamer"

Suggestion: "GG! Belle partie! 🎮🔥 #gaming"
- Score de base: 50
- 2 emojis: +10
- Hashtag #gaming trouvé: +15
- Mot-clé "gameplay" NOT dans suggestion: 0
Total: 50 + 10 + 15 = 75%
```

---

## 🔐 Permissions

### Commandes pour tous
- !help
- !ping
- !status
- !stats
- !uptime
- !dashboard
- !analyse
- !suggest
- !start
- !stop

### Commandes Admin only
- !restart (Nécessite la permission Administrateur)

---

## 💾 Stockage des Données

### Bases de données
- `data/bot.db` - SQLite (données persistantes)
- `data/logs.json` - 1000 derniers événements

### Fichiers générés automatiquement
```
data/
├── bot.db              # Base de données (auto-crée)
├── logs.json           # Logs (auto-crée)
└── ...                 # Autres fichiers système
```

---

## 🛠️ Dépannage

### Problème: Le bot ne démarre pas
```bash
# Vérifiez votre token
nano .env

# Testez l'installation
python test.py

# Relancez
python bot.py
```

### Problème: DISCORD_TOKEN invalide
```bash
# Allez sur Discord Developer Portal
# https://discord.com/developers/applications
# Créez une app → Ajouter un bot → Copier le token
```

### Problème: L'analyse IA ne fonctionne pas
```bash
# Vérifiez que ai_analyzer.py existe
ls -la ai_analyzer.py

# Testez le module
python -c "from ai_analyzer import analyzer; print('OK')"
```

### Problème: Performance lente
```bash
# Supprimez les anciens logs
rm data/logs.json

# Redémarrez le bot
python bot.py
```

---

## 📞 Support

- 📖 Consultez README.md
- 🐛 Signalez les bugs via GitHub Issues
- 💡 Proposez des améliorations
- 👥 Rejoignez la communauté

---

**Gaza Tool V9** - Made with ❤️ for Termux Android