---

# Bot Discord - "LES EUCALYPTUS COURS"

Bienvenue sur le dépôt GitHub du **Bot Discord - LES EUCALYPTUS COURS**, un bot conçu pour faciliter l'accès aux ressources scolaires et l'organisation des élèves sur un serveur Discord dédié. Le bot permet de gérer les rôles, d'envoyer des fichiers et de publier automatiquement des ressources pédagogiques tout en respectant la confidentialité des données.

## Table des matières
- [À propos](#à-propos)
- [Fonctionnalités principales](#fonctionnalités-principales)
- [Structure du code](#structure-du-code)
- [Comment installer et utiliser le projet](#comment-installer-et-utiliser-le-projet)
- [Contact](#contact)
- [Licence](#licence)

---

## À propos
Le projet **LES EUCALYPTUS COURS** est un bot Discord créé par **Mohammad Rezki** pour organiser les échanges scolaires au sein de son établissement via Discord. Ce bot permet :
- D'accueillir les nouveaux membres du serveur.
- De gérer les rôles des utilisateurs afin de leur donner accès aux canaux appropriés.
- D'automatiser la publication de fichiers et ressources éducatives.
- De supprimer automatiquement des messages envoyés par le bot en fonction des interactions des utilisateurs.

Le bot utilise **Python** avec la bibliothèque **discord.py** pour interagir avec l'API Discord.

---

## Fonctionnalités principales

### 1. **Envoi automatisé de fichiers**
Le bot peut envoyer des fichiers, comme des fiches de révision, à des utilisateurs spécifiques, tout en incluant un message d'avertissement concernant l'utilisation interne des fichiers.
- 💡 **Illustration suggérée** : Capture d'écran d'un fichier envoyé via message privé avec l'avertissement.

### 2. **Gestion des rôles et permissions**
Le bot attribue automatiquement les permissions nécessaires en fonction des rôles des utilisateurs, ce qui permet de limiter l'accès à certaines sections du serveur.
- 💡 **Illustration suggérée** : Capture d'écran des rôles affectés à des utilisateurs.

### 3. **Suppression des messages du bot**
Le bot supprime automatiquement les messages qu'il a envoyés après un certain temps, notamment après avoir envoyé des fichiers en message privé.
- 💡 **Illustration suggérée** : Capture d'écran de la commande `delete_messages` en action.

### 4. **Publication automatisée des cours**
Le bot peut parcourir un répertoire de fichiers et publier des documents comme des images ou des PDF dans un canal spécifique. Cela permet aux élèves d'accéder aux ressources sans attendre.
- 💡 **Illustration suggérée** : Capture d'écran de la commande `cpi` publiant des fichiers dans un canal.

### 5. **Messages de bienvenue**
Le bot envoie automatiquement un message de bienvenue à chaque nouvel utilisateur rejoignant le serveur, les guidant dans le choix de leur classe et rôles.
- 💡 **Illustration suggérée** : Capture d'écran du message de bienvenue.

---

## Structure du code

### Fichiers principaux :
- **`bot.py`** : Fichier principal contenant la logique du bot.
- **`requirements.txt`** : Liste des dépendances Python nécessaires pour exécuter le bot.

### Exemple de commandes incluses :
- **`%test`** : Vérifie si le bot fonctionne correctement.
- **`%cpi <channel_id> <chemin>`** : Publie automatiquement les fichiers trouvés dans un dossier spécifique vers un canal Discord.
- **`%send <@utilisateur> <chemin_du_fichier>`** : Envoie un fichier à un utilisateur spécifique via message privé.
- **`%sendd <@utilisateur>`** : Envoie un fichier PDF de révision à un utilisateur spécifique.

### Gestion des événements :
- **`on_ready()`** : S'exécute lorsque le bot se connecte avec succès à Discord.
- **`on_member_join(member)`** : Accueille les nouveaux membres et les guide pour choisir leurs rôles et classes.

---

## Comment installer et utiliser le projet

### Prérequis
- **Python 3.8+**
- **discord.py** (bibliothèque Python)
  
### Installation
1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/votre-utilisateur/bot-eucalyptus.git
   ```

2. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurer le bot** :
   - Créez une application sur [Discord Developer Portal](https://discord.com/developers/applications) et récupérez le token du bot.
   - Modifiez le fichier `bot.py` pour y ajouter votre token :
     ```python
     bot.run('VOTRE_TOKEN_ICI')
     ```

4. **Exécuter le bot** :
   ```bash
   python bot.py
   ```

### Utilisation
- Utilisez la commande **`%cpi <channel_id> <chemin>`** pour publier automatiquement des fichiers dans un canal spécifique.
- Utilisez **`%send <@utilisateur> <chemin_du_fichier>`** pour envoyer des fichiers à un utilisateur spécifique.
- À chaque connexion ou ajout de membre, le bot envoie automatiquement des messages de bienvenue et gère les rôles.

---

## Contact
Si vous avez des questions ou des suggestions pour améliorer le bot, vous pouvez me contacter à l'adresse suivante :
- **E-mail** : rezki.mohammad@exemple.com

---

## Licence
Ce projet est sous licence [MIT](LICENSE). Vous pouvez librement utiliser, modifier et distribuer ce projet tant que vous respectez les termes de la licence.

---
