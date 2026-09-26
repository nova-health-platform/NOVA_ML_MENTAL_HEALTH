<div align="center">

  <h1>NOVA ML Mental Health</h1>

  <p>
    Microservice de scoring psychologique (dépression, anxiété, stress) pour la plateforme santé NOVA
  </p>

<p>
  <a href="https://github.com/BaditSad/NOVA_ML_MENTAL_HEALTH/commits/main">
    <img src="https://img.shields.io/github/last-commit/BaditSad/NOVA_ML_MENTAL_HEALTH" alt="last update" />
  </a>
  <a href="https://github.com/BaditSad/NOVA_ML_MENTAL_HEALTH">
    <img src="https://img.shields.io/github/languages/top/BaditSad/NOVA_ML_MENTAL_HEALTH" alt="top language" />
  </a>
</p>

</div>

<br />

# Table des matières

- [À propos](#à-propos)
  * [Stack technique](#stack-technique)
  * [Fonctionnalités](#fonctionnalités)
- [Démarrage](#démarrage)
  * [Prérequis](#prérequis)
  * [Lancer avec Docker](#lancer-avec-docker)
  * [Utilisation](#utilisation)
- [Dépôts liés](#dépôts-liés)
- [Contact](#contact)

## À propos

Ce service fait partie du module de suivi psychologique de NOVA. Il expose une API Flask qui prend en entrée les réponses d'un questionnaire de 42 questions et retourne un score de dépression, d'anxiété et de stress, chacun accompagné d'un niveau de sévérité (Normal, Mild, Moderate, Severe, Extremely Severe).

Le service charge un modèle et un scaler pré-entraînés (`joblib`) pour normaliser les réponses avant de calculer les scores par sous-échelle, selon une répartition fixe des questions par catégorie.

### Stack technique

<details>
  <summary>API</summary>
  <ul>
    <li><a href="https://www.python.org/">Python</a></li>
    <li><a href="https://flask.palletsprojects.com/">Flask</a></li>
  </ul>
</details>

<details>
  <summary>Machine Learning</summary>
  <ul>
    <li><a href="https://scikit-learn.org/">scikit-learn</a></li>
    <li><a href="https://joblib.readthedocs.io/">joblib</a></li>
    <li><a href="https://numpy.org/">NumPy</a></li>
    <li><a href="https://pandas.pydata.org/">pandas</a></li>
    <li><a href="https://keras.io/">Keras</a></li>
    <li><a href="https://www.tensorflow.org/">TensorFlow</a></li>
  </ul>
</details>

<details>
  <summary>Déploiement</summary>
  <ul>
    <li><a href="https://www.docker.com/">Docker</a></li>
  </ul>
</details>

### Fonctionnalités

- Réception d'un tableau de 42 réponses via l'API
- Normalisation des réponses avec un scaler pré-entraîné
- Calcul de trois scores indépendants : dépression, anxiété, stress
- Association de chaque score à un niveau de sévérité clinique

## Démarrage

### Prérequis

Docker doit être installé. Les fichiers `joblibs/model_mentalhealth.joblib` et `joblibs/scaler.joblib` doivent être présents dans le dossier `joblibs` à la racine du projet (non versionnés dans ce dépôt).

### Lancer avec Docker

```bash
docker build -t nova-ml-mental-health .
docker run -p 5003:5003 nova-ml-mental-health
```

### Utilisation

```bash
curl -X POST http://localhost:5003/predict \
  -H "Content-Type: application/json" \
  -d '{"answers": [0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2]}'
```

La réponse contient les scores et les niveaux de sévérité pour les trois catégories.

## Dépôts liés

NOVA est découpé en plusieurs services indépendants :

- [NOVA_WEB](https://github.com/BaditSad/NOVA_WEB) : frontend web de la plateforme
- [NOVA_API](https://github.com/BaditSad/NOVA_API) : API centrale qui orchestre les appels aux modèles
- [NOVA_DB](https://github.com/BaditSad/NOVA_DB) : base de données métier
- [NOVA_LOGS_DB](https://github.com/BaditSad/NOVA_LOGS_DB) : journalisation des analyses
- [NOVA_ML_ANALYSIS](https://github.com/BaditSad/NOVA_ML_ANALYSIS) : module d'analyse des symptômes
- [NOVA_ML_PREPROD](https://github.com/BaditSad/NOVA_ML_PREPROD) : environnement de préproduction des modèles
- [NOVA_ML_SCAN_BODY](https://github.com/BaditSad/NOVA_ML_SCAN_BODY) : module de scan et check-up dermatologique

## Contact

Brieuc Dumortier

[LinkedIn](https://www.linkedin.com/in/dumortier-brieuc/) - [GitHub](https://github.com/BaditSad) - dumortier.contact@gmail.com
