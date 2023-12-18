import streamlit as st
import requests

def fetch_data(table_name, column_names):
    url = f'https://apex.oracle.com/pls/apex/fatima_zahra/{table_name}/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if response.status_code == 200:
            if data['items']:
                st.markdown(f"### Voici toutes les données de la table {table_name}:")
                table_data = [column_names]  # En-têtes du tableau

                for item in data['items']:
                    table_data.append([item.get(col) for col in column_names])

                st.markdown("""
                    <style>
                        table {
                            width: 100%;
                            border-collapse: collapse;
                            margin: 1em 0;
                            font-size: 16px;
                        }
                        th, td {
                            padding: 10px;
                            text-align: left;
                            border-bottom: 1px solid #ddd;
                        }
                        th {
                            background-color: #f2f2f2;
                        }
                    </style>
                    """, unsafe_allow_html=True)

                st.table(table_data)
            else:
                st.info(f"Aucune donnée disponible dans la table {table_name}.")

            st.success(f'Données de la table {table_name} récupérées avec succès.')

        else:
            st.warning(f'La requête a réussi, mais le statut était {response.status_code}.')

    except requests.exceptions.RequestException as e:
        st.error(f'Erreur lors de la requête HTTP : {e}')

def app():
    st.title("Séances disponibles")

    # Utilisation de la fonction fetch_data pour récupérer les données de la table 'seance'
    fetch_data('SEANCE', ['NOM', 'TYPIQUE', 'NIVEAU'])

# Ajoutez d'autres fonctionnalités spécifiques à la page de séances si nécessaire
