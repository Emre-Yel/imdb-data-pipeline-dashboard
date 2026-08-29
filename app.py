import streamlit as st
import pandas as pd
import sqlite3

# Grundeinstellungen für die Seite
st.set_page_config(page_title="Movie Dashboard", layout="wide")

st.title("🎬 Meine IMDb Filmdaten-Analyse")
st.markdown("Interaktives Portfolio-Projekt zur Analyse der 1000 bestbewerteten Filme.")
st.markdown("---")

# Daten aus der Datenbank laden, die main.py erstellt hat
conn = sqlite3.connect('movies_database.db')
df = pd.read_sql_query("SELECT * FROM top_movies", conn)
conn.close()

# Auswahlmenü in der Sidebar, um nach Regisseur zu filtern
st.sidebar.header("Filter & Steuerung")
alle_regisseure = sorted(df['Director'].unique())
auswahl = st.sidebar.selectbox("Wähle einen Regisseur:", alle_regisseure)

# Nur die Filme vom ausgewählten Regisseur behalten
gefiltert = df[df['Director'] == auswahl]

# Ein paar Kennzahlen berechnen
anzahl_filme = len(gefiltert)
avg_rating = round(gefiltert['IMDB_Rating'].mean(), 2)
revenue_raw = gefiltert['Gross'].sum()

# Einnahmen je nach Größe in Mio. oder Mrd. anzeigen, damit es lesbar bleibt
if revenue_raw >= 1_000_000_000:
    revenue_formatted = f"${revenue_raw / 1_000_000_000:,.2f} Mrd."
else:
    revenue_formatted = f"${revenue_raw / 1_000_000:,.2f} Mio."

# Kennzahlen anzeigen
st.subheader(f"Kennzahlen für {auswahl}")
col1, col2, col3 = st.columns(3)
col1.metric("Anzahl der Filme", anzahl_filme)
col2.metric("Ø IMDB Rating", f"{avg_rating} / 10")
col3.metric("Gesamteinnahmen", revenue_formatted)

st.markdown("---")

# Zwei Diagramme nebeneinander: Ratings und Einnahmen
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("Ratings der Filme")
    st.bar_chart(gefiltert.set_index('Series_Title')['IMDB_Rating'])

with col_chart2:
    st.subheader("Einnahmen pro Film ($)")
    st.bar_chart(gefiltert.set_index('Series_Title')['Gross'])

# Tabelle mit den Rohdaten zum Nachschauen
st.subheader("Hintergrunddaten")
st.dataframe(gefiltert[['Series_Title', 'Released_Year', 'Genre', 'IMDB_Rating', 'Gross']])