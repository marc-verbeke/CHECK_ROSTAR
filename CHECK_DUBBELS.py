import pandas as pd
import resend


def checkdubbels(bestand):
    # CSV inlezen met; als scheidingsteken
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
        # KAV
        if bestand == r"DATA\KAV.csv":
            if not dubbels.empty:
                # API key instellen
                resend.api_key = "re_6LHHsqMd_PFGBPpvoCDyBa928CsSLqhnQ"
                # Zet DataFrame om naar HTML
                # 1) Basis HTML zonder index
                html_table = dubbels.to_html(index=False, border=0)

                # 2) Inline styles injecteren (werkt in strikte e-mailclients)
                html_table = html_table.replace(
                    "<table",
                    '<table style="border-collapse:collapse;width:100%;"'
                ).replace(
                    "<th>",
                    '<th style="border:1px solid #000;padding:6px;text-align:center;" align="center">'
                ).replace(
                    "<td>",
                    '<td style="border:1px solid #000;padding:6px;text-align:center;" align="center">'
                )

                # 3) Complete e-mail body (zonder <style>-blok, puur inline)
                html_content = f"""
                <html>
                    <body>
                        <div style="text-align:center;margin-top: 20px;margin-bottom:20px;">
                            <h2 style="margin:0; font-family:Arial; font-size:20px;">
                                Overzicht ROSTAR diensten dubbel gepland
                            </h2>
                        </div>
                        {html_table}
                    </body>
                </html>
                """

                resend.Emails.send({
                    "from": "check_rostar@notifications.waaslandia.be",
                    "to": ["marc.verbeke@waaslandia.be", "ict@waaslandia.be"],
                    "subject": "KAV: Overzicht ROSTAR diensten dubbel gepland",
                    "html": html_content
                })

        # WAASLANDIA
        if bestand == r"DATA\WAASLANDIA.csv":
            if not dubbels.empty:
                # API key instellen
                resend.api_key = "re_6LHHsqMd_PFGBPpvoCDyBa928CsSLqhnQ"
                # Zet DataFrame om naar HTML
                # 1) Basis HTML zonder index
                html_table = dubbels.to_html(index=False, border=0)

                # 2) Inline styles injecteren (werkt in strikte e-mailclients)
                html_table = html_table.replace(
                    "<table",
                    '<table style="border-collapse:collapse;width:100%;"'
                ).replace(
                    "<th>",
                    '<th style="border:1px solid #000;padding:6px;text-align:center;" align="center">'
                ).replace(
                    "<td>",
                    '<td style="border:1px solid #000;padding:6px;text-align:center;" align="center">'
                )

                # 3) Complete e-mail body (zonder <style>-blok, puur inline)
                html_content = f"""
                                <html>
                                    <body>
                                        <div style="text-align:center;margin-top: 20px;margin-bottom:20px;">
                                            <h2 style="margin:0; font-family:Arial; font-size:20px;">
                                                Overzicht ROSTAR diensten dubbel gepland
                                            </h2>
                                        </div>
                                        {html_table}
                                    </body>
                                </html>
                                """
                resend.Emails.send({
                    "from": "check_rostar@notifications.waaslandia.be",
                    "to": ["marc.verbeke@waaslandia.be"],
                    "subject": "WAASLANDIA: Overzicht ROSTAR diensten dubbel gepland",
                    "html": html_content
                })

        # KRUGER
        if bestand == r"DATA\KRUGER.csv":
            if not dubbels.empty:
                # API key instellen
                resend.api_key = "re_6LHHsqMd_PFGBPpvoCDyBa928CsSLqhnQ"
                # Zet DataFrame om naar HTML
                # 1) Basis HTML zonder index
                html_table = dubbels.to_html(index=False, border=0)

                # 2) Inline styles injecteren (werkt in strikte e-mailclients)
                html_table = html_table.replace(
                    "<table",
                    '<table style="border-collapse:collapse;width:100%;"'
                ).replace(
                    "<th>",
                    '<th style="border:1px solid #000;padding:6px;text-align:center;" align="center">'
                ).replace(
                    "<td>",
                    '<td style="border:1px solid #000;padding:6px;text-align:center;" align="center">'
                )

                # 3) Complete e-mail body (zonder <style>-blok, puur inline)
                html_content = f"""
                                <html>
                                    <body>
                                        <div style="text-align:center;margin-top: 20px;margin-bottom:20px;">
                                            <h2 style="margin:0; font-family:Arial; font-size:20px;">
                                                Overzicht ROSTAR diensten dubbel gepland
                                            </h2>
                                        </div>
                                        {html_table}
                                    </body>
                                </html>
                                """
                resend.Emails.send({
                    "from": "check_rostar@notifications.waaslandia.be",
                    "to": ["marc.verbeke@waaslandia.be"],
                    "subject": "KRUGER: Overzicht ROSTAR diensten dubbel gepland",
                    "html": html_content
                })


checkdubbels(r"DATA\KAV.csv")
checkdubbels(r"DATA\WAASLANDIA.csv")
checkdubbels(r"DATA\KRUGER.csv")
