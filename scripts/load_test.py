import sqlite3
import pandas as pd

df = pd.read_parquet("yellow_tripdata_2023-01.parquet")
print(df.head())
print(df.shape)

""" # Connexion local BDD 
conn = sqlite3.connect("yellow_taxi.db")

# Load Dataframe in SQLITE
df.to_sql("yellow_trips", conn, if_exists="replace", index=False)

# Check SQL
cur = conn.cursor()
cur.execute("SELECT * FROM yellow_trips")
print("Nombre de lignes chargée :", cur.fetchall()[0])
conn.close() """

conn = sqlite3.connect("yellow_taxi.db")
for row in conn.execute("SELECT passenger_count, COUNT(*) FROM yellow_trips GROUP BY passenger_count LIMIT 5;"):
    print(row)
