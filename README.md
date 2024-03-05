<div align="center">
    <h1>🏡 Clone d'AirBnB - La Console 🧑‍💻</h1>
</div>


<p align="center">
    <img src="https://zupimages.net/up/24/10/4zt2.png">
</p>

## 📌 Description

Plongez dans l'univers Python avec ce projet éducatif inspiré d'AirBnB. Conçu dans le cadre du programme de développement logiciel de l'[École Holberton](https://www.holbertonschool.fr/), il pose les bases de ce qui sera, étape par étape, une application web complète.

---

<details>
<summary> <strong> 📚 Contexte </strong> </summary>
<br>

Bienvenue dans le projet Clone d'AirBnB ! Avant de commencer, familiarisez-vous avec le concept d'AirBnB en regardant [cette présentation du projet HBNB](https://youtu.be/E12Xc3H2xqo).

### Première étape : Un interpréteur de commandes pour gérer vos objets AirBnB.

C'est le premier jalon vers la création de votre application web complète : le clone d'AirBnB. Cette étape est cruciale car vous réutiliserez ce que vous créez ici dans les projets suivants, intégrant HTML/CSS, base de données, API, et l'intégration front-end.

Voici ce que vous apprendrez à faire :

- Mettre en place une classe parent (nommée `BaseModel`) pour initialiser, sérialiser et désérialiser vos instances futures.
- Créer un flux simple de sérialisation/désérialisation : Instance <-> Dictionnaire <-> Chaîne JSON <-> fichier.
- Développer toutes les classes nécessaires pour AirBnB (`User`, `State`, `City`, `Place`...) héritant de `BaseModel`.
- Implémenter le premier moteur de stockage abstrait du projet : le stockage dans des fichiers.
- Rédiger tous les tests unitaires pour valider nos classes et notre moteur de stockage.

### Qu’est-ce qu’un interpréteur de commandes ?

Pensez à la Shell, mais adapté à un cas d'utilisation spécifique. Notre objectif est de pouvoir gérer les objets de notre projet :

- Créer un nouvel objet (ex : un nouvel utilisateur ou un nouveau lieu).
- Récupérer un objet depuis un fichier, une base de données, etc.
- Effectuer des opérations sur les objets (compter, calculer des stats, etc.).
- Mettre à jour les attributs d'un objet.
- Détruire un objet.

### Objectifs d'apprentissage

Après ce projet, vous serez capable d'expliquer, sans chercher sur Google :

#### Général

- La création d'un package Python.
- La création d'un interpréteur de commandes en Python en utilisant le module `cmd`.
- Ce qu'est le test unitaire et comment l'implémenter dans un grand projet.
- La sérialisation et désérialisation d'une classe.
- La lecture et l'écriture d'un fichier JSON.
- La gestion de `datetime`.
- Ce qu'est un `UUID`.
- L'utilisation de `*args` et `**kwargs`.
- La gestion des arguments nommés dans une fonction.

### Exigences

#### Scripts Python

- Éditeurs autorisés : `vi`, `vim`, `emacs`.
- Vos fichiers seront interprétés/compilés sur Ubuntu 20.04 LTS en utilisant python3 (version 3.8.5).
- Chaque fichier doit se terminer par une nouvelle ligne.
- La première ligne de tous vos fichiers doit être exactement `#!/usr/bin/python3`.
- Un fichier `README.md`, à la racine du dossier du projet,
ChatGPT
 est obligatoire.
- Votre code doit utiliser la norme pycodestyle (version 2.7.*).
- Tous vos fichiers doivent être exécutables.
- La longueur de vos fichiers sera testée avec `wc`.
- Tous vos modules, classes et fonctions (internes et externes) doivent être documentés.

#### Tests Unitaires Python

- Doivent être placés dans un dossier `tests`.
- Utilisez le module [unittest](https://docs.python.org/3.4/library/unittest.html#module-unittest).
- Les fichiers de test doivent avoir l'extension `.py` et commencer par `test_`.
- L'organisation de vos fichiers de test doit refléter celle de votre projet.
- Exécutez tous vos tests avec : `python3 -m unittest discover tests`.

### GitHub

**Un seul dépôt de projet par groupe.**

### Exécution

Votre console doit fonctionner ainsi en mode interactif :
```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb) quit
$
```

Et en mode non interactif :
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

Tous les tests doivent aussi passer en mode non interactif : `$ echo "python3 -m unittest discover tests" | bash`

</details>

---

## 🚀 Lancer le projet

**Clonage du dépôt :**
```
git clone https://github.com/SpeedCash/holbertonschool-AirBnB_clone
```

**Démarrage de l'interpréteur :**
```
cd holbertonschool-AirBnB_clone && ./console.py
```

Vous verrez apparaître :
```
(hbnb)
```

---

## 🛠️ Utilisation de l'interpréteur

L'interpréteur permet de gérer vos objets AirBnB de façon interactive ou non. Voici quelques commandes disponibles :

| Commande   | Exemple d'utilisation                          | Description                                         |
|------------|------------------------------------------------|-----------------------------------------------------|
| `help`     | `help`                                         | Affiche toutes les commandes disponibles            |
| `create`   | `create <class>`                               | Crée un nouvel objet (ex. un nouvel Utilisateur)    |
| `show`     | `show User 123`                                | Affiche les détails d'un objet spécifié             |
| `destroy`  | `destroy User 123`                             | Supprime un objet spécifié                          |
| `all`      | `all`                                          | Affiche tous les objets de toutes les classes       |
| `quit`     | `quit`                                         | Quitte la console                                   |

---

## 🧪 Tests

Pour exécuter les tests unitaires :
```
python3 -m unittest discover tests
```

---

## ✍️ Auteurs

- **Hocine BOUABDALLAH** & **Thierry CRAVERO** - Nous avons collaboré avec passion sur ce projet, explorant les profondeurs de Python et les subtilités du développement d'applications web. Retrouvez-nous sur GitHub !

## 📜 Licence

Ce projet est distribué sous la licence de l'École Holberton.