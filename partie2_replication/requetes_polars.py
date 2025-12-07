from pymongo import MongoClient
import polars as pl

# Connexion 
client = MongoClient("mongodb://localhost:27017/?directConnection=true")

db = client["noscites"]
collection = db["listings"]

# charger seulement les champs utiles
champs = {
    "_id": 0,
    "room_type": 1,
    "neighbourhood_cleansed": 1,
    "host_is_superhost": 1,
    "number_of_reviews": 1,
    "availability_30": 1
}

data = list(collection.find({}, champs))
df = pl.DataFrame(data)
print(f"{len(df)} documents chargés")

# Requête 1 : Médiane des avis
print("\n--- Médiane des avis ---")
print(df["number_of_reviews"].median())

# Requête 2: Médiane des avis par type d'hôte
print("\n--- Médiane avis : Super hôte vs Normal ---")
print(df.group_by("host_is_superhost").agg(pl.col("number_of_reviews").median()))

# Requête 3: Disponibilité moyenne par type de logement
print("\n--- Disponibilité moyenne par type ---")
print(df.group_by("room_type").agg(pl.col("availability_30").mean()))

# Requête 4: Logements par quartier
print("\n--- Top 10 quartiers ---")
print(df.group_by("neighbourhood_cleansed").agg(pl.count()).sort("count", descending=True).head(10))

# Requête 5: Quartiers les plus réservés
print("\n--- Quartiers les plus réservés ---")
print(df.group_by("neighbourhood_cleansed").agg(pl.col("availability_30").mean()).sort("availability_30").head(10))
