import streamlit as st
import pandas as pd

# ----------------------- CONFIG -----------------------
st.set_page_config(page_title="Dashboard Netflix", layout="wide")

# ----------------------- CHARGEMENT --------------------
@st.cache_data
def load_data():
    df = pd.read_csv("netflix_titles.csv")

    """Pipeline de nettoyage pour le dataset Netflix."""

    print("1- Inspection initiale...")
    print(df.info(), "\n")

    print("2- Détection de valeurs manquantes...")
    print(df.isnull().sum(), "\n")

    print("3- Nettoyage et standardisation...")
    df_clean = df.copy()

    # 3.1 Suppression des doublons
    df_clean = df_clean.drop_duplicates()

    # 3.2 Standardisation de certaines colonnes texte
    text_cols = ["type", "title", "director", "cast", "country", 
                 "rating", "duration", "listed_in"]
    for col in text_cols:
        df_clean[col] = df_clean[col].astype(str).str.strip()

    # 3.3 Conversion colonne date_added → datetime
    df_clean["date_added"] = pd.to_datetime(df_clean["date_added"], errors="coerce")

    # 3.4 Extraction de la durée (pour les films vs séries)
    # Ex: "90 min" → 90 | "3 Seasons" → 3
    df_clean["duration_int"] = df_clean["duration"].str.extract('(\d+)').astype(float)

    # 3.5 Nettoyage pays (country) : si NA → "Unknown"
    df_clean["country"] = df_clean["country"].fillna("Unknown")

    print("4- Validation des types...")
    print(df_clean.dtypes, "\n")

    print("5- Aperçu du dataset nettoyé:")
    print(df_clean.head(), "\n")

    return df_clean

df = load_data()

st.title("📺 Analyse exploratoire du catalogue Netflix (Movies & TV Shows)")

# ----------------------- SIDEBAR -----------------------
st.sidebar.header("🔧 Filtres interactifs")

types = sorted(df["type"].unique())
type_filtre = st.sidebar.multiselect("Type :", types, default=types)

annees = sorted(df["release_year"].unique())
annee_min, annee_max = st.sidebar.select_slider(
    "Années de sortie :",
    options=annees,
    value=(min(annees), max(annees))
)

# ----------------------- 1. FILMS VS SERIES -----------------------
st.header("🎬 1. Films vs Séries")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Proportion globale")
    st.bar_chart(df["type"].value_counts())

with col2:
    st.subheader("Tendance par année")
    tendance_type = df.groupby(["release_year", "type"]).size().unstack(fill_value=0)
    st.line_chart(tendance_type)

# ----------------------- 2. GENRES -----------------------
st.header("🎭 2. Genres les plus fréquents")

all_genres = df['listed_in'].str.split(', ').explode()
top_genres = all_genres.value_counts().head(15)
st.bar_chart(top_genres)

# ----------------------- 3. GEOGRAPHIE -----------------------
st.header("🌍 3. Pays les plus représentés")

country_no_na = df['country'].dropna()
# Supprimer les chaînes "nan" (texte)
all_country = country_no_na[country_no_na.str.lower() != "nan"]
top_pays = all_country.value_counts().head(15)
st.bar_chart(top_pays)

# ----------------------- 4. CASTING & REALISATEURS -----------------------
st.header("🎥 4. Casting & Réalisateurs les plus présents")

colA, colB = st.columns(2)

with colA:
    st.subheader("Acteurs les plus présents")
    cast_no_na = df['cast'].dropna()

    all_cast = cast_no_na.str.split(', ').explode()

    # Supprimer les chaînes "nan" (texte)
    all_cast = all_cast[all_cast.str.lower() != "nan"]
    top_cast = all_cast.value_counts().head(10).drop('Unknown', errors='ignore')
    st.bar_chart(top_cast)

with colB:
    st.subheader("Réalisateurs les plus présents")
    directors_no_na = df['director'].dropna()

    all_directors = directors_no_na.str.split(', ').explode()

    # Supprimer les chaînes "nan" (texte)
    all_directors = all_directors[all_directors.str.lower() != "nan"]
    top_directors = all_directors.value_counts().head(15).drop('Unknown', errors='ignore')
    st.bar_chart(top_directors)

# ----------------------- 5. ANALYSE TEMPORELLE -----------------------
st.header("📅 5. Analyse temporelle (date_added)")

df_date = df.dropna(subset=["date_added"])
ajouts_par_annee = df_date["date_added"].dt.year.value_counts().sort_index()

st.line_chart(ajouts_par_annee)

# ----------------------- FIN -----------------------


# Pour exécuter cette application, utilisez la commande suivante dans votre terminal :
# python -m streamlit run "app.py"
# Assurez-vous que le fichier 'netflix_titles.csv' est dans le même répertoire que ce script.
# Vous pouvez installer Streamlit avec la commande : pip install streamlit
# Vous pouvez également installer pandas avec la commande : pip install pandas
# Si vous n'avez pas matplotlib et seaborn, vous pouvez les installer avec :
# pip install matplotlib seaborn
# Pour arrêter l'application, utilisez Ctrl+C dans le terminal.
