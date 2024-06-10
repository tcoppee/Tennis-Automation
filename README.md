# Tennis Reservation Automation

Ce projet a pour but de permettre la réservation automatique des terrains de tennis en utilisant un fichier de disponibilités. Il faut renseigner un maximum de disponibilité, par exemple sur tout le quadrimestre. Le code se lancera à chaque démarrage de l'ordinateur vérifiant automatiquement les disponibilités sur une semaine.

## Fonctionnement
Le script permet de réserver automatiquement les terrains de tennis en se basant sur les disponibilités fournies dans un fichier texte. Les disponibilités doivent être au format suivant :

```
11/06/2024 13:00 > 14:00
13/06/2024 15:00 > 16:00
17/06/2024 12:00 > 13:00
```

Pour utiliser ce script, veuillez renseigner votre nom d'utilisateur et votre mot de passe dans le fichier `main.py`.

## Comment lancer le script au démarrage

### Windows
1. Ouvrez Notepad et collez-y le code suivant :
   ```
   python [path vers main.py]
   ```
2. Sauvegardez le fichier avec l'extension `.bat` dans le dossier du projet, par exemple `start_script.bat`.

3. Placez ce fichier `.bat` dans le dossier de démarrage de Windows. Vous pouvez y accéder en appuyant sur `Win + R`, puis en tapant `shell:startup` et en appuyant sur `Entrée`.

### macOS
1. Ouvrez Terminal et créez un script shell en tapant :
   ```
   nano start_script.sh
   ```
   Collez ensuite le code suivant dans le terminal :
   ```
   #!/bin/bash
   python3 /chemin/vers/votre/script.py
   ```
   Remplacez `/chemin/vers/votre/script.py` par le chemin vers votre script Python.

2. Sauvegardez le fichier en appuyant sur `Ctrl + X`, puis en tapant `Y` et en appuyant sur `Entrée`.

3. Rendez le script exécutable en tapant :
   ```
   chmod +x start_script.sh
   ```

4. Pour lancer le script au démarrage, ajoutez-le aux applications de démarrage via `Préférences Système > Utilisateurs et groupes > Ouverture`.

### Linux
1. Ouvrez un terminal et créez un script shell en tapant :
   ```
   nano start_script.sh
   ```
   Collez ensuite le code suivant dans le terminal :
   ```
   #!/bin/bash
   python3 /chemin/vers/votre/script.py
   ```
   Remplacez `/chemin/vers/votre/script.py` par le chemin vers votre script Python.

2. Sauvegardez le fichier en appuyant sur `Ctrl + X`, puis en tapant `Y` et en appuyant sur `Entrée`.

3. Rendez le script exécutable en tapant :
   ```
   chmod +x start_script.sh
   ```

4. Pour lancer le script au démarrage, ajoutez-le aux applications de démarrage via le dossier `~/.config/autostart`.
