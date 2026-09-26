<div align="center">
  <img src=".github/assets/banner.png" alt="NOVA_ML_MENTAL_HEALTH banner" width="100%" />

  <h1>NOVA_ML_MENTAL_HEALTH</h1>

  <p>
    Psychological scoring microservice (depression, anxiety, stress) for the NOVA health platform.
  </p>

<p>
  <a href="https://github.com/nova-health-platform/NOVA_ML_MENTAL_HEALTH/commits/main">
    <img src="https://img.shields.io/github/last-commit/nova-health-platform/NOVA_ML_MENTAL_HEALTH" alt="last update" />
  </a>
  <a href="https://github.com/nova-health-platform/NOVA_ML_MENTAL_HEALTH">
    <img src="https://img.shields.io/github/languages/top/nova-health-platform/NOVA_ML_MENTAL_HEALTH" alt="top language" />
  </a>
</p>

</div>

<br />

## :notebook_with_decorative_cover: Table of Contents

- [About](#star2-about)
  * [Tech Stack](#space_invader-tech-stack)
  * [Features](#dart-features)
- [Getting Started](#toolbox-getting-started)
  * [Prerequisites](#bangbang-prerequisites)
  * [Run with Docker](#whale-run-with-docker)
  * [Usage](#eyes-usage)
- [Related Repositories](#link-related-repositories)
- [Contact](#handshake-contact)

## :star2: About

This service is part of NOVA's psychological monitoring module. It exposes a Flask API that takes the answers of a 42-question questionnaire as input and returns a depression, anxiety and stress score, each paired with a severity level (Normal, Mild, Moderate, Severe, Extremely Severe).

The service loads a pre-trained model and scaler (`joblib`) to normalize the answers before computing scores per subscale, based on a fixed distribution of questions across categories.

### :space_invader: Tech Stack

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
  <summary>Deployment</summary>
  <ul>
    <li><a href="https://www.docker.com/">Docker</a></li>
  </ul>
</details>

### :dart: Features

- Receives an array of 42 answers via the API
- Normalizes the answers with a pre-trained scaler
- Computes three independent scores: depression, anxiety, stress
- Maps each score to a clinical severity level

## :toolbox: Getting Started

### :bangbang: Prerequisites

Docker must be installed. The files `joblibs/model_mentalhealth.joblib` and `joblibs/scaler.joblib` must be present in the `joblibs` folder at the project root (not versioned in this repository).

### :whale: Run with Docker

```bash
docker build -t nova-ml-mental-health .
docker run -p 5003:5003 nova-ml-mental-health
```

### :eyes: Usage

```bash
curl -X POST http://localhost:5003/predict \
  -H "Content-Type: application/json" \
  -d '{"answers": [0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2]}'
```

The response contains the scores and severity levels for the three categories.

## :link: Related Repositories

NOVA is split into several independent services:

- [NOVA_WEB](https://github.com/nova-health-platform/NOVA_WEB): web frontend of the platform
- [NOVA_API](https://github.com/nova-health-platform/NOVA_API): central API that orchestrates calls to the models
- [NOVA_DB](https://github.com/nova-health-platform/NOVA_DB): business database
- [NOVA_LOGS_DB](https://github.com/nova-health-platform/NOVA_LOGS_DB): analysis log storage
- [NOVA_ML_ANALYSIS](https://github.com/nova-health-platform/NOVA_ML_ANALYSIS): symptom analysis module
- [NOVA_ML_PREPROD](https://github.com/nova-health-platform/NOVA_ML_PREPROD): model staging environment
- [NOVA_ML_SCAN_BODY](https://github.com/nova-health-platform/NOVA_ML_SCAN_BODY): scan and dermatological check-up module
- [NOVA-CORE](https://github.com/nova-health-platform/NOVA-CORE): architecture overview and local orchestration for the whole platform

## :handshake: Contact

Brieuc Dumortier

[LinkedIn](https://www.linkedin.com/in/dumortier-brieuc/) - [GitHub](https://github.com/BaditSad) - dumortier.contact@gmail.com
