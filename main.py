import pandas as pd
import sqlite3

# Liest die CSV-Datei ein und gibt sie als DataFrame zurück
def extract_data(filepath):
    print("Lese Daten ein...")
    df = pd.read_csv(filepath)
    return df


def transform_data(df):
    # Daten bereinigen: Formate korrigieren, damit man damit rechnen kann
    print("Bereinige Daten...")

    # Gross ist als Text mit Kommas gespeichert (z.B. "28,341,469") -> zu Zahl umwandeln
    df['Gross'] = df['Gross'].str.replace(',', '').astype(float)

    # Runtime hat " min" am Ende (z.B. "142 min") -> Text entfernen, nur die Zahl behalten
    df['Runtime'] = df['Runtime'].str.replace(' min', '').astype(int)

    # Manche Filme haben keine Angabe bei Gross -> mit 0 auffüllen, damit später nichts crasht
    df['Gross'] = df['Gross'].fillna(0)

    return df


def load_data(df, db_name, table_name):
    # Speichert die bereinigten Daten in einer SQLite-Datenbank
    print(f"Speichere in {db_name}...")
    conn = sqlite3.connect(db_name)

    # replace = Tabelle wird jedes Mal neu geschrieben, keine doppelten Einträge bei erneutem Ausführen
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    conn.close()
    print("Fertig!")


if __name__ == "__main__":
    # Ablauf: erst Daten holen, dann bereinigen, dann speichern
    rohdaten = extract_data("imdb_top_1000.csv")
    saubere_daten = transform_data(rohdaten)
    load_data(saubere_daten, "movies_database.db", "top_movies")