# FireStorm TP

TP de reverse Android sur une application qui génère dynamiquement un mot de passe utilisé pour l'authentification Firebase.

## Objectif

- Installer et analyser l'APK
- Identifier la méthode `Password()` dans `MainActivity`
- Forcer son exécution avec Frida
- Récupérer le mot de passe
- Se connecter à Firebase
- Lire la base de données et récupérer le flag

## Outils utilisés

- Android Studio
- ADB
- Jadx-GUI
- Frida
- Python 3
- `pyrebase`

## Utilisation

1. Lancer un émulateur Android depuis Android Studio.
2. Installer l'APK sur l'émulateur.
3. Démarrer `frida-server` sur l'appareil.
4. Lancer le script Frida pour afficher le mot de passe.
5. Mettre ce mot de passe dans le script Python.
6. Exécuter le script Python pour récupérer le flag.

## Fichiers importants

- rapport complet en LaTeX
- extract_secret.js : script Frida pour appeler `Password()`
- recover_flag.py : script Python pour l'authentification Firebase

## Remarque

Les valeurs sensibles comme le mot de passe final et le flag doivent être complétées après exécution des scripts.
