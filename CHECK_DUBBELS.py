import pandas as pd

# CSV inlezen met ; als scheidingsteken
df = pd.read_csv("data/waaslandia.csv", sep=";")

# Schrappen van alle records waar Dienst = "OB1"
df = df[df["Dienst"] != "OB1"]

# Combineer Dienst en Deel in de kolom 'Dienst'
df["Dienst"] = df["Dienst"].astype(str) + " - " + df["Deel"].astype(int).astype(str)

# Verwijder de kolom 'Deel' & 'ID'
df = df.drop(columns=["Deel"])
df = df.drop(columns=["ID"])

# Zorg dat alle kolommen getoond worden
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

# Toon dubbels enkel op basis van Datum en Dienst
dubbels = df[df.duplicated(subset=["Datum", "Dienst"], keep=False)]
# Sorteer dubbels eerst op Datum, dan op Dienst
dubbels = dubbels.sort_values(by=["Datum", "Dienst"])

print(dubbels)
