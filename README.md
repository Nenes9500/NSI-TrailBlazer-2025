# TrailBlazer

## Description

TrailBlazer est un jeu de course en deux dimensions et en vue du dessus créé dans le cadre des Trophées NSI. Créez des circuits puis jouez en mode course sur ceux-ci.

## Version

La version du projet présentée aux trophées est la dernière version stable du projet. Celui-ci a depuis reçu quelques nouvelles fonctionalitées instables. Nous avons donc décidé de les exclure du projet pour le moment.

## Prérequis

- Un environnement supportant Python
- Assurez-vous d'avoir Python 3.1 ou une version supérieure (Il est recommandé d'avoir une version supérieure à Python 3.10 pour pygame)
- Les différents modules présents dans `requirements.txt`

## Installation

1. Installez les dépendances du projet:

   ```sh
   pip install -r requirements.txt
   ```

2. Lancez le jeu (depuis le répertoire `/sources` du projet):

   ```sh
   python main.py
   ```

## Utilisation

- **Mode Éditeur**:
    Choisissez parmis différentes tuiles pour constituer votre propre circuit! Il est possible d'orienter les tuiles dans la direction de votre choix. Une fois votre circuit constitué, placez une ligne d'arrivée et donnez un nom à votre circuit. Vous pourrez ensuite l'enregistrer.

- **Mode Course**:
    Vous pouvez choisir parmis les circuits que vois avez créé. Réalisez le plus de tours possibles sans sortir de la piste. Plus vous êtes rapide, plus votre score sera important. Attention aux virages! Ils ne pardonnent pas.

- **Replays (Beta)**:
    Il est possible en mode Course d'enregistrer et de visionner des replays (menu de pause avec la touche `p`). Un replay enregistre chacune de vos actions et les répète ensuite lorsqu'il est joué. (Le playback du replay ne fonctionne pas correctement pour le moment).

## Technologies utilisées

- Python 3
- pygame pour le moteur graphique et physique du jeu
- PIL pour la génération d'un circuit en mode Éditeur

## Bugs connus

- Le playback du replay ne fonctionne pas correctement.
- Appuyer sur plusieurs touches liées à une action en même temps double l'effet de l'action.

## Licence

Ce projet est sous la licence GNU GPL v3.0 (`licence.txt`)
