# 💾 OneGitBackup

Il s'agit d'un outil pour faire des backups de dépôts Github d'organisations automatiquement.

![Demo 1](https://raw.githubusercontent.com/BuyWithCrypto/OneGitBackup/main/demo/1.png)

------

# 💻 Exemples d'utilisation

## - 💿 La sauvegarde de dépôts publics  :

Nous souhaitons sauvegarder tous les dépôts publics de notre organisation ainsi que toutes leurs branches.

![Demo 2](https://raw.githubusercontent.com/BuyWithCrypto/OneGitBackup/main/demo/2.png)

Un UUID (Universally unique identifier) sera alors généré et il s'agira du nom de dossier où la sauvegarde sera enregistrée.

![Demo 3](https://raw.githubusercontent.com/BuyWithCrypto/OneGitBackup/main/demo/3.png)

Une fois que l'outil aura terminé ses tâches, les sauvegardes seront disponibles sous la forme de fichier au format .zip avec comme préfixe le nom du dépôt et comme suffixe le nom de la branche du dépôt.

![Demo 4](https://raw.githubusercontent.com/BuyWithCrypto/OneGitBackup/main/demo/4.png)

------

# 📦 Installation et utilisation

## - Pour utiliser l'outil sur Linux  :

_1. Installer les bibliothèques Python pré-requises :_
```shell
$ wget https://github.com/BuyWithCrypto/OneGitBackup/releases/download/v1.0/requirements.txt && pip3 install -r requirements.txt
```
_2. Télécharger le fichier exécutable :_
```shell
$ wget https://github.com/BuyWithCrypto/OneGitBackup/releases/download/v1.0/OneGitBackup.pyc
```
_3. Démarrer l'exécutable :_
```shell
$ python3 OneGitBackup.pyc
```
------

## - Pour utiliser l'outil sur Windows  :

_1. Cloner le dépôt avec git :_
```shell
$ git clone https://github.com/BuyWithCrypto/OneGitBackup/
```
_2. Installer les bibliothèques Python pré-requises :_
```shell
$ pip install -r requirements.txt
```
_3. Démarrer l'exécutable :_
```shell
$ python main.py
```
------

# 🔨 Contribution pour les développeurs

------

## ✅ Mise en place de l'environnement :
_1. Cloner le dépôt Github :_
```shell
$ git clone https://github.com/BuyWithCrypto/OneGitBackup/
```
_2. Naviguer vers le dossier du projet :_
```shell
$ cd OneGitBackup/
```
_3. Installer les bibliothèques Python pré-requises :_
```shell
$ pip3 install -r requirements.txt
```

------

## 🚧 Compiler le code source
_Pour compiler le code source en exécutable, vous pouvez utiliser cette commande. :_

```shell
$ python3 -m py_compile main.py
```