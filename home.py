# home.py

import streamlit as st
from streamlit_option_menu import option_menu

from acceuil import app1_app as app1_app
from sessions import page2_app as page2_app
from inserer_seance import page5_app as page5_app  # Mettez à jour l'import
from insert_weekly_session import page6_app as page6_app

st.set_page_config(
    page_title="Pondering",
)

class MultiApp:
    def _init_(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='GYM ',
                options=['Home', 'Séances', 'Entraineurs', 'Graphiques', 'Insertion Séance', 'Insertion Séance Hebdomadaire'],
                icons=['house-fill', 'person-circle', 'trophy-fill', 'chat-fill', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if app == "Home":
            acceuil_app()
        elif app == "Séances":
            sessions_app()
        elif app == "Entraineurs":
            coaches_app()
        elif app == "Graphiques":
            charts_app()
        elif app == "Insertion Séance":
            inserer_seance_app()  # Mettez à jour la fonction appelée
        elif app == "Insertion Séance Hebdomadaire":
            insert_weekly_session_app()

# Créez une instance de MultiApp et ajoutez vos pages
multi_app = MultiApp()
multi_app.add_app("Home", app1_app)
multi_app.add_app("Séances", page2_app)
multi_app.add_app("Graphiques", page4_app)
multi_app.add_app("Insertion Séance", page5_app)
multi_app.add_app("Insertion Séance Hebdomadaire", page6_app)

# Exécutez l'application
multi_app.run()