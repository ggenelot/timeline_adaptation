import csv, json

CSV_INPUT = "data/timeline.csv"
JSON_OUTPUT = "build/timeline.json"

def to_int(value):
    return int(value) if value and value.isdigit() else None

events = []

with open(CSV_INPUT, newline='', encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        if row.get("display", "1") not in ("1", "true", "TRUE"):
            continue  # skip hidden rows

        event = {
            "start_date": {
                "year": to_int(row["start_year"]),
                "month": to_int(row["start_month"]),
                "day": to_int(row["start_day"])
            },
            "end_date": {
                "year": to_int(row["end_year"]),
                "month": to_int(row["end_month"]),
                "day": to_int(row["end_day"])
            },
            "text": {
                "headline": row["headline"],
                "text": row["text"]
            },
            "media": {
                "url": row["media_url"],
                "caption": row["media_caption"],
                "credit": row["media_credit"],
                "thumbnail": row["media_thumbnail"]
            }
        }

        events.append(event)

timeline = {
    "title": {
        "text": {
            "headline": "Ma Timeline",
            "text": ""
        }
    },
    "events": events
}

with open(JSON_OUTPUT, "w", encoding="utf-8") as f:
    json.dump(timeline, f, indent=2, ensure_ascii=False)

print("✔ timeline.json généré !")
