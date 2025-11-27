import csv, json, os

# Script that converts the CSV to JSON

CSV_INPUT = "data/timeline.csv"
JSON_OUTPUT = "build/timeline.json"

def to_int(v):
    """Convertit proprement en entier ou None."""
    try:
        return int(v)
    except:
        return None

events = []

with open(CSV_INPUT, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:

        # Ne conserver que les lignes marquées Show == True (insensible à la casse)
        if str(row.get("Show", "")).strip().lower() != "true":
            continue

        # Ignorer les lignes sans Headline (souvent des lignes vides)
        if not row.get("Headline"):
            continue

        event = {
            "start_date": {
                "year": to_int(row.get("Year")),
                "month": to_int(row.get("Month")),
                "day": to_int(row.get("Day"))
            },
            "end_date": {
                "year": to_int(row.get("End Year")),
                "month": to_int(row.get("End Month")),
                "day": to_int(row.get("End Day"))
            },
            "text": {
                "headline": row.get("Headline", ""),
                "text": row.get("Text", "")
            },
            "media": {
                # Ton CSV dit "Media" pour l’URL → OK
                "url": row.get("Media", ""),
                "caption": row.get("Media Caption", ""),
                "credit": row.get("Media Credit", ""),
                "thumbnail": row.get("Media Thumbnail", "")
            }
        }

        # Ajout du Group si présent
        if row.get("Group"):
            event["group"] = row["Group"]

        events.append(event)

# Structure finale du JSON Timeline.js
timeline = {
    "title": {
        "text": {
            "headline": "Ma Timeline",
            "text": ""
        }
    },
    "events": events
}

# Création du dossier build/ si besoin
os.makedirs(os.path.dirname(JSON_OUTPUT), exist_ok=True)

with open(JSON_OUTPUT, "w", encoding="utf-8") as f:
    json.dump(timeline, f, indent=2, ensure_ascii=False)

print("✔ timeline.json généré à partir de TON CSV !")
