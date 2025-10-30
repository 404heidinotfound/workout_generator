import csv
import os

# Absoluten Pfad angeben (kein Rätselraten mehr)
filename = r"C:\Users\Administrator\Documents\Programmieren mit Python\06_Project\exercises.csv"

# Prüfen, ob Datei existiert
if not os.path.exists(filename):
    print("Datei nicht gefunden:", filename)
else:
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        print("Datei gefunden!")
        print("Gefundene Spaltennamen:", reader.fieldnames)

        import csv
import os

def load_exercises_from_csv(filename):
    exercises = {}

    # Debug: Zeige, wo Python sucht
    print("Arbeitsverzeichnis:", os.getcwd())

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row["exercise"]

            # Gewicht, falls angegeben
            weight = row["weight"] if row["weight"] else None

            # Scaling, falls angegeben
            scaling = row["scaling"] if row["scaling"] else None

            # Kategorien (alle Spalten mit "x")
            categories = []
            if row["classic"] == "x":
                categories.append("classic")
            if row["conditioning"] == "x":
                categories.append("condi")
            if row["gymnastics"] == "x":
                categories.append("gym")
            if row["oly"] == "x":
                categories.append("oly")

            # Benchmark (Boolean)
            benchmark = True if row["benchmark"] == "x" else False

            # Dictionary für jede Übung aufbauen
            exercises[name] = {
                "weight": weight,
                "scaling": scaling,
                "category": categories,
                "benchmark": benchmark
            }

    return exercises


# Einlesen (Datei muss im gleichen Ordner wie dieses Script liegen!)
exercises = load_exercises_from_csv(r"C:\Users\Administrator\Documents\Programmieren mit Python\06_Project\exercises.csv")

# Testausgabe
for name, info in exercises.items():
    print(name, "->", info)

