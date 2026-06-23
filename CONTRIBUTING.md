# CONTRIBUTING.md - Guide de Contribution

Merci de votre intérêt pour contribuer à **Gaza Tool V9**! 🙌

## 🚀 Comment contribuer

### 1. Fork le projet
```bash
# Allez sur https://github.com/haza90k-debug/Gaza_Toolv9
# Cliquez sur "Fork"
```

### 2. Clonez votre fork
```bash
git clone https://github.com/VOTRE_USERNAME/Gaza_Toolv9
cd Gaza_Toolv9
```

### 3. Créez une branche
```bash
git checkout -b feature/votre-feature
# ou
git checkout -b fix/votre-bug
```

### 4. Apportez vos modifications
```bash
# Éditez les fichiers
pip install -r requirements.txt
python bot.py  # Testez
```

### 5. Commitez vos changements
```bash
git add .
git commit -m "Description claire de votre changement"
```

### 6. Poussez vers votre fork
```bash
git push origin feature/votre-feature
```

### 7. Créez une Pull Request
- Allez sur GitHub
- Cliquez sur "Compare & pull request"
- Décrivez vos changements
- Attendez la review

## 📋 Types de contributions acceptées

### 🐛 Bug Fixes
- Corrections de bugs
- Améliorations de performance
- Optimisations code

### ✨ Nouvelles Fonctionnalités
- Nouvelles catégories IA
- Nouvelles commandes
- Nouvelles suggestions

### 📖 Documentation
- Amélioration README
- Nouveaux exemples
- Guide d'installation

### 🔧 Améliorations
- Refactoring code
- Meilleur logging
- Gestion d'erreurs améliorée

## 📝 Guidelines de Contribution

### Style de Code
```python
# Utilisez le format PEP 8
# Indentation: 4 espaces
# Lignes max: 100 caractères
# Docstrings: Always

def ma_fonction():
    """Description de la fonction"""
    pass
```

### Commit Messages
```bash
# Format: Type: Description
# Types: feat, fix, docs, style, refactor, perf, test

git commit -m "feat: ajouter nouvelle catégorie IA"
git commit -m "fix: corriger bug d'analyse"
git commit -m "docs: actualiser README"
```

### Tests
```bash
# Testez votre code avant de PR
python bot.py
# Vérifiez les logs
tail -f data/logs.json
```

## 🎯 Processus de Review

1. **Vérification du code** - Style, performance
2. **Tests** - Fonctionnalité correcte
3. **Documentation** - Code bien documenté
4. **Feedback** - Commentaires et suggestions
5. **Merge** - Si approuvé ✅

## ❓ Questions?

- Consultez les [Issues](https://github.com/haza90k-debug/Gaza_Toolv9/issues)
- Ouvrez une nouvelle Issue
- Lisez le README.md

## 📜 Code of Conduct

- Respectez les autres contributeurs
- Pas de contenu offensant
- Collaboration constructive
- Partage de connaissances

---

**Merci d'avoir contribué à Gaza Tool V9!** 🎉