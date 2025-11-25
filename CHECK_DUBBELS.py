import pandas as pd

def checkdubbels(bestand):
    # CSV inlezen met ; als scheidingsteken
    df = pd.read_csv(bestand, sep=";")
    # Verwijder rijen die volledig NaN zijn
    df = df.dropna(how="all")

    if not df.empty:
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

        # Toon resultaat
        print(dubbels)
    else:
        print("geen gegevens")

print("CTRL KAV")
checkdubbels(r"DATA\KAV.csv")
print("--------------------------------------------------------------------------------------------------------------")
print("CTRL WAASLANDIA")
checkdubbels(r"DATA\WAASLANDIA.csv")
print("--------------------------------------------------------------------------------------------------------------")
print("CTRL KRUGER")
checkdubbels(r"DATA\KRUGER.csv")
print("--------------------------------------------------------------------------------------------------------------")