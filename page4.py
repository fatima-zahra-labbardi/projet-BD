import streamlit as st
import pandas as pd
import requests
import plotly.express as px

# URL pour vos données d'entraîneurs et d'horaire
url_eeentraineur = 'https://apex.oracle.com/pls/apex/fatima_zahra/entraineur/'
url_hhhoraire = 'https://apex.oracle.com/pls/apex/fatima_zahra/horaire/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'  # Ajoutez votre User-Agent
}

# Récupération de vos données depuis les URLs
response_eeentraineur = requests.get(url_eeentraineur, headers=headers)
response_hhhoraire = requests.get(url_hhhoraire, headers=headers)

# Vérification que la requête a réussi avant de continuer
if response_eeentraineur.status_code == 200 and response_hhhoraire.status_code == 200:
    # Conversion des données JSON en DataFrames pandas
    df_eeentraineur = pd.DataFrame(response_eeentraineur.json()["items"])
    df_hhhoraire = pd.DataFrame(response_hhhoraire.json()["items"])


    # Création des graphiques avec Plotly Express
    fig_bar = px.bar(df_hhhoraire, y="heure_de_debut", title="Nombre de séances par plage horaire", color_discrete_sequence=['pink'])
    fig_line = px.line(df_hhhoraire.groupby("jour").size().reset_index(name="nombre_seances"),
                   x="jour", y="nombre_seances", title="Nombre de séances par jour de la semaine", color_discrete_sequence=['pink'])

    fig_bar.update_layout(barmode='group', xaxis={'categoryorder': 'category ascending'})
    fig_line.update_traces(mode='markers+lines')


    # Affichage des graphiques sur la page Streamlit
    # Titre stylisé
    st.markdown(
        "<h1 style='text-align: center; color: #ff69b4;'>Graphiques sur les séances programmées</h1>",
        unsafe_allow_html=True
    )

    st.plotly_chart(fig_bar)
    st.plotly_chart(fig_line)

    st.success("Les données ont été mises à jour avec succès.")
else:
    st.error("Échec de la récupération des données depuis les URLs.")
