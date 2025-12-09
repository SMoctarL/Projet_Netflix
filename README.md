# Projet d'Analyse du Catalogue Netflix

## 1. Introduction

Ce projet analyse le dataset *Netflix Titles* à l'aide d'un tableau de
bord interactif développé avec Streamlit.\
L'objectif principal est de comprendre les tendances du catalogue
Netflix à travers une série d'analyses visuelles.

## 2. Objectifs du projet

### 2.1 Objectifs analytiques

-   Identifier la répartition entre films et séries\
-   Étudier les genres les plus populaires\
-   Analyser les pays les plus représentés\
-   Déterminer les acteurs et réalisateurs les plus présents\
-   Étudier l'évolution du catalogue avec le temps

### 2.2 Objectifs techniques

-   Créer une application Streamlit\
-   Effectuer un nettoyage complet du dataset\
-   Réaliser des visualisations pertinentes\
-   Structurer un notebook d'analyse

## 3. Structure du projet

    /
    ├── app.py
    ├── netflix_titles.csv
    ├── requirements.txt
    ├── README.md
    └── netflixProject.ipynb

### 3.1 Description des fichiers

-   app.py : application Streamlit principale\
-   netflix_titles.csv : dataset utilisé\
-   requirements.txt : dépendances du projet\
-   notebooks/netflixProject.ipynb : analyse exploratoire détaillée

## 4. Installation

### 4.1 Prérequis

-   Python 3.10 ou supérieur\
-   pip installé\
-   Un terminal (Windows, macOS ou Linux)

### 4.2 Installation des dépendances

#### Windows

    python -m pip install -r requirements.txt

#### macOS

    pip3 install -r requirements.txt

ou

    python3 -m pip install -r requirements.txt

#### Linux

    pip3 install -r requirements.txt

ou

    python3 -m pip install -r requirements.txt

## 5. Exécution de l'application

### Windows

    python -m streamlit run app.py

### macOS

    streamlit run app.py

ou

    python3 -m streamlit run app.py

### Linux

    streamlit run app.py

ou

    python3 -m streamlit run app.py

L'application sera disponible à l'adresse :\
http://localhost:8501/

## 6. Fonctionnalités de l'application

### 6.1 Répartition Films / Séries

Visualisation de la distribution globale et de son évolution sur les
années.

### 6.2 Analyse des genres

Extraction, nettoyage et classement des genres les plus représentés.

### 6.3 Analyse géographique

Répartition des productions par pays.

### 6.4 Analyse des personnalités

Identification des acteurs et réalisateurs les plus fréquents.

### 6.5 Analyse temporelle

Étude du nombre de titres ajoutés par année.

## 7. Dataset

### 7.1 Source

Dataset provenant de Kaggle : Netflix Movies and TV Shows.

### 7.2 Traitements effectués

-   Gestion des données manquantes\
-   Suppression des doublons\
-   Conversion des dates\
-   Extraction de la durée\
-   Nettoyage textuel des colonnes multi-valeurs
