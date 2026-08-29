# IMDB-data-pipeline-dashboard

Ein kleines End-to-End Data-Engineering-Projekt: Extrahieren, Bereinigen und 
Laden von IMDb-Filmdaten in eine SQLite-Datenbank, mit interaktivem 
Streamlit-Dashboard zur Analyse.

## Was macht das Projekt?
- **Extract:** Liest die IMDb Top 1000 Filme aus einer CSV-Datei
- **Transform:** Bereinigt Formatierungsfehler (z.B. Einnahmen-Strings zu Zahlen, 
  Laufzeit-Text zu Integer), behandelt fehlende Werte
- **Load:** Speichert die bereinigten Daten in einer SQLite-Datenbank
- **Dashboard:** Streamlit-App zur interaktiven Filterung nach Regisseur, 
  mit Kennzahlen (Anzahl Filme, Ø Rating, Gesamteinnahmen) und Visualisierungen

## Tech Stack
Python, Pandas, SQLite, Streamlit

## Ausführen
```bash
pip install pandas streamlit
python main.py        # Pipeline ausführen
streamlit run app.py  # Dashboard starten
```

## Screenshot
<img width="1920" height="956" alt="image" src="https://github.com/user-attachments/assets/5afb6023-1885-4d6c-92b0-0983bcedaf85" />
<img width="1918" height="577" alt="image" src="https://github.com/user-attachments/assets/8138956d-d95b-4e35-9e4c-328e02d0466b" />
