#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Système IA de suggestion de commentaires
Analyse de contenu et génération intelligente
"""

import re
import random
from datetime import datetime
from typing import List, Dict, Tuple
from collections import Counter


class AIAnalyzer:
    """Analyseur IA pour contenu social"""
    
    # Dictionnaire de catégories avec mots-clés
    CATEGORIES = {
        "humour": ["blague", "rire", "drôle", "marrant", "lol", "haha", "mdr", "funny", "laugh", "joke"],
        "sport": ["foot", "basket", "tennis", "match", "équipe", "but", "victoire", "championnat", "sports", "athlete", "game"],
        "gaming": ["jeu", "game", "fps", "rpg", "streaming", "twitch", "fortnite", "minecraft", "gaming", "esport", "player"],
        "religion": ["dieu", "église", "prière", "foi", "spirituel", "blessed", "amen", "spirituality", "faith"],
        "actualité": ["news", "breaking", "nouvelle", "événement", "important", "alert", "urgent", "today", "actualité"],
        "musique": ["chanson", "musique", "artiste", "chanteuse", "concert", "album", "clip", "singer", "song", "music"],
        "technologie": ["tech", "app", "software", "code", "ai", "robot", "innovation", "startup", "développement", "programming"],
        "voyage": ["voyage", "vacances", "destination", "tourisme", "pays", "plage", "montagne", "tour", "trip", "travel"],
        "mode": ["vêtement", "fashion", "style", "outfit", "tendance", "marque", "mode", "look", "shopping", "design"],
        "éducation": ["école", "cours", "apprentissage", "étudiant", "prof", "éducation", "learning", "university", "student"],
        "food": ["nourriture", "restaurant", "cuisine", "recette", "délicieux", "food", "cooking", "lunch", "dinner", "eat"],
        "fitness": ["sport", "gym", "musculation", "workout", "entraînement", "health", "fitness", "exercise", "training"],
        "beauté": ["beauté", "maquillage", "skincare", "cosmétique", "makeup", "beauty", "skincare", "cosmetics"],
        "art": ["art", "peinture", "dessin", "créatif", "artist", "creativity", "création", "artwork", "creative"],
    }
    
    # Suggestions prédéfinies par catégorie
    SUGGESTIONS_TEMPLATES = {
        "humour": [
            "😂 Je me suis éclaté en regardant ça!",
            "Hahahaha c'est trop drôle! 🤣",
            "Je suis mort de rire 💀",
            "C'est fou comme c'est marrant 😆",
            "Ça m'a tué 😂💯",
            "Meilleur contenu que j'ai vu aujourd'hui 🔥",
            "Je ne peux pas arrêter de rire 😂😂",
            "Ça c'est du bon humour! 👌",
            "Je recommande à tous mes potes 😂",
            "Qualité maximum 🎯",
        ],
        "sport": [
            "Belle performance! 💪",
            "Quel match incroyable! 🔥",
            "Respect à ce joueur! 👏",
            "La meilleure équipe gagne 🏆",
            "Quel talent extraordinaire! ⚡",
            "Je revois cette action 100 fois 🎬",
            "Du vrai football/basketball/sport 💯",
            "Incroyable! 🤯",
            "Les meilleurs moments du match! ⭐",
            "Voilà comment on joue! 🎯",
        ],
        "gaming": [
            "GG! Belle partie! 🎮",
            "Ton gameplay est fou! 🔥",
            "Je veux devenir aussi bon! 💪",
            "Streaming légendaire 🎯",
            "Cette mécanique est dingue! 🚀",
            "Je dois absolument essayer ça 🎮",
            "Les meilleurs highlights du jour! ⭐",
            "Quel talent! Respect! 👑",
            "Je reviens regarder ça ce soir 🍿",
            "Multiplayer goals! 💯",
        ],
        "actualité": [
            "Merci de partager cette info! 📰",
            "C'est très important! ✊",
            "Les gens doivent le savoir 📢",
            "À partager absolument! 🔄",
            "Excellente couverture! 👍",
            "Bien rapporté! 🎯",
            "À voir absolument! 👀",
            "Vraiment révélateur! 🤔",
            "Cela mérite plus d'attention 📣",
            "Merci pour cette perspective! 💡",
        ],
        "musique": [
            "Quelle chanson de feu! 🔥🎵",
            "J'ai l'oreille qui tourne! 🎧",
            "Artiste de talent! ⭐",
            "Je mets en boucle! 🔁",
            "Les paroles sont magnifiques 💜",
            "Meilleur son de l'année! 🎼",
            "Elle chante trop bien! 👑",
            "Clip incroyable! 🎬",
            "C'est un hit assuré! 💯",
            "Ça va cartonner! 🚀",
        ],
        "technologie": [
            "Innovation impressionnante! 🚀",
            "Voilà le futur! 🤖",
            "Tech de dingue! ⚡",
            "C'est génial comme idée! 💡",
            "Les développeurs ont du talent! 💻",
            "Ça change tout! 🔄",
            "Vraiment révolutionnaire! 🌟",
            "Code propre et efficace! 👍",
            "L'IA progresse vite! 🤯",
            "À suivre de près! 👀",
        ],
        "voyage": [
            "Destination de rêve! ✈️",
            "Vue magnifique! 😍",
            "Je veux y aller! 🌍",
            "Paradis sur terre! 🏝️",
            "Photos extraordinaires! 📸",
            "À visiter absolument! 🗺️",
            "C'est trop beau! 😭",
            "Vacances de rêve! 🌴",
            "Je l'ajoute à ma liste! 📝",
            "Paysages à couper le souffle! 🏔️",
        ],
        "mode": [
            "Style impeccable! 🔥",
            "Outfit parfait! 👗",
            "Fashion goals! 👑",
            "C'est tendance! ✨",
            "Très à la mode! 💃",
            "L'assortiment est parfait! 🎯",
            "Goût impeccable! 👌",
            "Je veux la même chose! 😍",
            "Design luxe! 💎",
            "Vraiment élégant! 🤎",
        ],
        "éducation": [
            "Merci pour cette explication! 📚",
            "Très pédagogue! 👍",
            "J'ai appris plein de choses! 🧠",
            "C'est brillamment expliqué! ⭐",
            "Exactement ce qu'il me fallait! 💯",
            "Contenu de qualité! 📖",
            "À recommander aux étudiants! ✊",
            "Simple et clair! 🎯",
            "Je partage avec mes camarades! 🔄",
            "Meilleur tuto jamais! 🏆",
        ],
        "food": [
            "J'ai faim maintenant! 😋",
            "Ça a l'air délicieux! 🤤",
            "Je veux goûter! 🍽️",
            "Recette parfaite! 👨‍🍳",
            "Restaurant de rêve! ⭐",
            "Présentation magnifique! 📸",
            "À tester absolument! ✨",
            "Mes papilles frétillent! 👅",
            "Qualité premium! 💎",
            "Saveurs incroyables! 🌶️",
        ],
        "fitness": [
            "Inspi muscu! 💪",
            "Belle séance! 🏋️",
            "Défi accepté! 🔥",
            "Résultats incroyables! 🤯",
            "Motivation maximale! ⚡",
            "C'est possible! 💯",
            "Programmes de fou! 🎯",
            "Transformation époustouflante! ✨",
            "Respect l'athlète! 👑",
            "À faire ! 🚀",
        ],
        "beauté": [
            "Peau magnifique! ✨",
            "Tuto makeup parfait! 💄",
            "Résultat waouh! 😍",
            "Beauté naturelle! 💜",
            "Technique pro! 👌",
            "Produits de qualité! 💎",
            "À essayer! 🛍️",
            "Transformation incroyable! 🤯",
            "Tutoriel utile! 📖",
            "Luminosité radieuse! ☀️",
        ],
        "art": [
            "Oeuvre d'art! 🎨",
            "Talent remarquable! 👏",
            "C'est magnifique! 😍",
            "Créativité sans limite! ✨",
            "Détail impressionnant! 🔍",
            "Vrai artiste! 👑",
            "À exposer au musée! 🖼️",
            "Coup de pinceau expert! 🎭",
            "Inspiration trouvée! 💡",
            "Masterpiece! 💯",
        ],
    }
    
    def __init__(self):
        """Initialisation de l'analyseur"""
        self.last_suggestions = {}  # Pour éviter les répétitions
    
    def analyze(self, content: str) -> Dict:
        """Analyse le contenu et retourne les métadonnées"""
        content_lower = content.lower()
        
        # Détecter les catégories
        categories = self._detect_categories(content_lower)
        
        # Extraire les hashtags
        hashtags = self._extract_hashtags(content)
        
        # Extraire les mots-clés
        keywords = self._extract_keywords(content_lower)
        
        # Détecter le thème principal
        main_theme = categories[0] if categories else "général"
        
        # Résumer le contenu
        summary = self._generate_summary(content, categories, keywords)
        
        return {
            "content": content,
            "categories": categories,
            "hashtags": hashtags,
            "keywords": keywords,
            "main_theme": main_theme,
            "summary": summary,
            "timestamp": datetime.now().isoformat(),
            "word_count": len(content.split()),
        }
    
    def suggest(self, analysis: Dict, count: int = 10) -> List[Dict]:
        """Génère des suggestions de commentaires"""
        suggestions = []
        category = analysis["main_theme"]
        
        # Obtenir les templates pour la catégorie
        templates = self.SUGGESTIONS_TEMPLATES.get(category, self.SUGGESTIONS_TEMPLATES.get(list(self.SUGGESTIONS_TEMPLATES.keys())[0]))
        
        # S'assurer qu'on n'utilise pas les mêmes suggestions
        cache_key = f"{category}_{count}"
        if cache_key in self.last_suggestions:
            used_indices = set(self.last_suggestions[cache_key])
        else:
            used_indices = set()
        
        # Générer les suggestions
        available_templates = [i for i in range(len(templates)) if i not in used_indices]
        
        # Si toutes sont utilisées, reset
        if len(available_templates) < count:
            used_indices = set()
            available_templates = list(range(len(templates)))
        
        # Sélectionner aléatoirement
        selected_indices = random.sample(available_templates, min(count, len(available_templates)))
        
        # Créer les suggestions
        for idx, index in enumerate(selected_indices):
            template = templates[index]
            
            # Ajouter des variations
            suggestion_text = self._add_variations(template, analysis)
            
            # Calculer le score de pertinence
            relevance_score = self._calculate_relevance(suggestion_text, analysis)
            
            suggestions.append({
                "id": idx + 1,
                "text": suggestion_text,
                "relevance_score": relevance_score,
                "category": category,
                "emoji_count": len([c for c in suggestion_text if ord(c) > 127]),
            })
        
        # Trier par pertinence
        suggestions.sort(key=lambda x: x["relevance_score"], reverse=True)
        
        # Sauvegarder pour éviter les répétitions
        self.last_suggestions[cache_key] = selected_indices
        
        return suggestions
    
    def _detect_categories(self, content: str) -> List[str]:
        """Détecte les catégories du contenu"""
        detected = []
        scores = {}
        
        for category, keywords in self.CATEGORIES.items():
            score = 0
            for keyword in keywords:
                if keyword in content:
                    score += content.count(keyword)
            if score > 0:
                scores[category] = score
        
        # Retourner les 3 meilleures catégories
        if scores:
            sorted_categories = sorted(scores.items(), key=lambda x: x[1], reverse=True)
            detected = [cat for cat, _ in sorted_categories[:3]]
        
        # Si aucune détectée, ajouter "général"
        if not detected:
            detected = ["général"]
        
        return detected
    
    def _extract_hashtags(self, content: str) -> List[str]:
        """Extrait les hashtags du contenu"""
        hashtags = re.findall(r"#\w+", content)
        return list(set(hashtags))  # Unique
    
    def _extract_keywords(self, content: str) -> List[str]:
        """Extrait les mots-clés importants"""
        # Supprimer la ponctuation et splitter
        words = re.findall(r"\b\w+\b", content)
        
        # Filtrer les mots courts et courants
        stop_words = {"le", "la", "de", "du", "et", "ou", "un", "une", "des", "a", "à", "est", "son", "ma", "ce"}
        keywords = [w for w in words if len(w) > 2 and w.lower() not in stop_words]
        
        # Obtenir les 5 les plus fréquents
        freq = Counter(keywords)
        top_keywords = [word for word, _ in freq.most_common(5)]
        
        return top_keywords
    
    def _generate_summary(self, content: str, categories: List[str], keywords: List[str]) -> str:
        """Génère un résumé du contenu"""
        # Limiter à 200 caractères
        if len(content) > 200:
            summary = content[:197] + "..."
        else:
            summary = content
        
        return summary
    
    def _add_variations(self, template: str, analysis: Dict) -> str:
        """Ajoute des variations au template"""
        variation = template
        
        # Ajouter aléatoirement des emojis supplémentaires
        if random.random() > 0.5:
            emojis = ["💯", "🔥", "✨", "⭐", "👍", "❤️"]
            variation += f" {random.choice(emojis)}"
        
        # Ajouter parfois un hashtag du contenu
        if analysis["hashtags"] and random.random() > 0.6:
            variation += f" {random.choice(analysis['hashtags'])}"
        
        return variation
    
    def _calculate_relevance(self, suggestion: str, analysis: Dict) -> int:
        """Calcule le score de pertinence (0-100)"""
        score = 50  # Score de base
        
        # Points bonus pour emojis (20 points max)
        emoji_count = len([c for c in suggestion if ord(c) > 127])
        score += min(20, emoji_count * 5)
        
        # Points bonus si contient un hashtag du contenu
        for hashtag in analysis["hashtags"]:
            if hashtag in suggestion:
                score += 15
        
        # Points bonus si mentionne des mots-clés
        for keyword in analysis["keywords"]:
            if keyword.lower() in suggestion.lower():
                score += 10
        
        # Cap à 100
        return min(100, score)


# Instance globale
analyzer = AIAnalyzer()