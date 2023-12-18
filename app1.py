import streamlit as st

import streamlit as st

# Fonction pour afficher la page d'accueil
def accueil():
    st.title("Bienvenue sur l'Application")
    st.markdown("---")
    st.markdown("<h2 style='color: #ff6b81;'></h2>", unsafe_allow_html=True)
    # Ajoutez ici du contenu supplémentaire ou des explications sur l'application

# Fonction pour afficher les séances disponibles
def page_seances():
    st.title("Séances disponibles")
    # Ajoutez ici le code pour afficher et filtrer les séances

# Barre de navigation / Menu latéral
selection = st.sidebar.radio("Navigation", ["Accueil", "Séances disponibles", "Autre partie de l'application"])

# Affichage de la page sélectionnée en fonction de la navigation
if selection == "Accueil":
    accueil()
elif selection == "Séances disponibles":
    page_seances()
# Ajoutez d'autres options pour d'autres parties de votre application ici












# Titre de l'application avec mise en forme de la police
st.markdown(
    "<h1 style='text-align: center; font-family: Arial, sans-serif; color: #ff6b81; font-weight: 600;'>"
    "Gestion des Séances dans la Salle de Sport  : <span style='font-family: cursive;'>   GYM for WOMEN</span>"
    "</h1>",
    unsafe_allow_html=True
)

# Présentation du projet avec mise en forme
st.markdown(
    f"""
    <div style="margin-top: 30px; padding: 20px; background-color: #f8b1bd; border-radius: 10px;">
        <p style="font-family: 'Times New Roman', Times, serif; font-size: 18px; line-height: 1.6; font-weight: 400;">
            Bienvenue Madame/Madmoiselle dans notre application de gestion des séances dans la salle de sport GYM for WOMEN ! L'objectif de notre application est de fournir une interface bien adaptée pour visualiser les informations sur les séances et les entraîneurs disponibles.
        </p>
        <hr style="border: 1px solid #ff6b81;">
        <p style="font-family: 'Arial', sans-serif; font-size: 16px; font-weight: 400;">
            Cette application permet :
        </p>
        <ul style="font-family: 'Arial', sans-serif; font-size: 16px; font-weight: 400;">
            <li>La visualisation et le filtrage des séances disponibles.</li>
            <li>L'affichage des informations sur les entraîneurs et leur filtrage par nom et date de naissance.</li>
            <li>Des graphiques illustrant les séances programmées.</li>
            <li>L'ajout de nouvelles séances .</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# Noms des réalisateurs en gras, plus grands et avec une police différente
st.markdown(
    "<p style='text-align: right; font-family: Arial, sans-serif; font-size: 16px; color: #ff6b81;'>"
    "Réalisé par : <span style='font-weight: bold; color: #ff6b81; font-size: 18px; font-family: Verdana, Geneva, sans-serif;'> Amalik Salma</span> & <span style='font-weight: bold; color: #ff6b81; font-size: 18px; font-family: Verdana, Geneva, sans-serif;'>LABBARDI Fatime Zahra</span>"
    "</p>",
    unsafe_allow_html=True
)





