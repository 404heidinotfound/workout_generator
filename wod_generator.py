# Projekt Workout-Generator (ohne Benchmarks)
# Mein Programm erstellt zufällige CrossFit-Workouts (WODs) aus einer CSV-Datei
# und kann daraus entweder ein einzelnes WOD oder einen kompletten 4-Wochen-Trainingsplan erstellen

import random # Zufallsauswahl
import csv # einlesen CSV Dateien
import os # Dateipfade

# Pfad zur CSV-Datei
filename = r"C:\Users\Administrator\Documents\Programmieren mit Python\06_Project\exercises_no_benchmarks.csv"

def load_exercises_from_csv(filename): # Übungen aus CSV Datei filtern
    exercises = {}
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["exercise"]
            weight = row["weight"] if row["weight"] else None
            scaling = row["scaling"] if row["scaling"] else None

            # Kategorien sammeln
            categories = []
            if row["classic"] == "x":
                categories.append("classic")
            if row["conditioning"] == "x":
                categories.append("conditioning")
            if row["gymnastics"] == "x":
                categories.append("gymnastics")
            if row["oly"] == "x":
                categories.append("oly")

            exercises[name] = {
                "weight": weight,
                "scaling": scaling,
                "category": categories
            }
    return exercises


# Einlesen
exercises = load_exercises_from_csv(filename)

# Sonderfälle
cardio = ["Bike Erg", "Row", "Ski Erg"]
running = ["Run"]

# Rep-Ranges
rep_ranges = {
    "conditioning": {"reps": [10, 15, 25, 30],
                     "meters": [200, 400, 500, 1000],
                     "calories": [10, 15, 25, 30]},
    "classic": {"reps": [7, 9, 10, 12, 15, 18, 21]},
    "gymnastics": {"reps": [3, 5, 8, 10, 12]},
    "oly": {"reps": [1, 2, 3, 5]}
}

def filter_exercises_by_category(exercises, category): # nach Kategorie filtern
    return [(name, info) for name, info in exercises.items()
            if category in info.get("category", [])]


def generate_exercise_specs(exercise_name, exercise_info, category): # Spezifika der WODs generieren
    result = {"exercise": exercise_name, "unit": "reps"}

    if category == "conditioning": # Cardio Übungen gesondert, weil es andere Einheiten gibt
        if exercise_name in cardio:
            result["unit"] = random.choice(["meters", "calories"])
            result["amount"] = random.choice(rep_ranges["conditioning"][result["unit"]])
        elif exercise_name in running:
            result["unit"] = "meters"
            result["amount"] = random.choice(rep_ranges["conditioning"]["meters"])
        else:
            result["amount"] = random.choice(rep_ranges[category]["reps"])
    else:
        result["amount"] = random.choice(rep_ranges[category]["reps"])

    # Gewicht & Scaling
    if category != "oly":
        result["weight"] = exercise_info["weight"] or "n. a."
    else:
        result["weight"] = "percentages of 1RM"

    result["scaling"] = exercise_info["scaling"] or "scale according to your level"
    return result


# Regeln für WODs und einzelnen Kategorien
wod_rules = {
    "conditioning": {"formats": ["EMOM", "AMRAP"],
                     "duration": (30, 40),
                     "exercises": (4, 5)},
    "gymnastics": {"formats": ["EMOM", "For Quality"],
                   "duration": (12, 20),
                   "exercises": (3, 4),
                   "hint": "Scale reps according to your level, rest 1-2 minutes between rounds"},
    "classic": {"formats": ["AMRAP", "EMOM", "For Time", "Rounds For Time"],
                "duration": (10, 25),
                "exercises": (2, 5)},
    "oly": {"formats": ["5x5", "3x3", "Find 1RM",
                        "Every 30s for 15min", "EMOM 15min"],
            "duration": None,
            "exercises": (1, 1),
            "hint": "Rest 1–2 minutes between sets"}
}

def generate_wod(exercises, category): # einzelnes WOD erzeugen
    rules = wod_rules[category]
    filtered = filter_exercises_by_category(exercises, category)

    if not filtered:
        return "Keine Übungen in dieser Kategorie gefunden."

    min_ex, max_ex = rules["exercises"] # Übungen random auswählen, Anzahl bestimmen
    num_ex = random.randint(min_ex, max_ex)
    chosen = random.sample(filtered, min(num_ex, len(filtered)))

    fmt = random.choice(rules["formats"]) # Übungen random auswählen, Dauer und Format bestimmen
    duration = random.randint(*rules["duration"]) if rules["duration"] else None

    # WOD-Text ausgeben
    wod_text = f"\nYour WOD – Category: {category.upper()}\n"
    wod_text += f"Format: {fmt}\n"
    if duration:
        wod_text += f"Duration: {duration} minutes\n"
    wod_text += "-"*40 + "\n"

    for exercise_name, exercise_info in chosen:
        specs = generate_exercise_specs(exercise_name, exercise_info, category)
        wod_text += f"- {specs['exercise']}: {specs['amount']} {specs['unit']} "
        wod_text += f"(weight: {specs['weight']}, scaling: {specs['scaling']})\n"

    if "hint" in rules: # falls vorhanden wird ein Hinweis gegeben
        wod_text += f"\nAdvice: {rules['hint']}\n"

    return wod_text


def save_plan_to_csv(exercises, filename="4_week_workout_plan.csv"): # 4 Wochenplan speichern, 4 Wochen mit je 3 random Trainingseinheiten
    categories = ["classic", "conditioning", "gymnastics", "oly"]

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["week", "day", "category", "format", "duration",
                      "exercise", "amount", "unit", "weight"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for week in range(1, 5):
            for day in range(1, 4):
                category = random.choice(categories)
                rules = wod_rules[category]

                filtered = filter_exercises_by_category(exercises, category)
                min_ex, max_ex = rules["exercises"]
                num_ex = random.randint(min_ex, max_ex)
                chosen = random.sample(filtered, min(num_ex, len(filtered)))

                fmt = random.choice(rules["formats"])
                duration = random.randint(*rules["duration"]) if rules["duration"] else ""

                for exercise_name, exercise_info in chosen:
                    specs = generate_exercise_specs(exercise_name, exercise_info, category)

                    writer.writerow({
                        "week": week,
                        "day": day,
                        "category": category,
                        "format": fmt,
                        "duration": duration,
                        "exercise": specs["exercise"],
                        "amount": specs["amount"],
                        "unit": specs["unit"],
                        "weight": specs["weight"]
                    })

    print(f"4 week plan saved as: {filename}") # 4-Wochenplan wird als CSV gespeichert
    return filename


def main(exercises):
    choice = input("Do you want to create a single WOD? (yes/no): ").strip().lower()
    # Frage beantworten: yes - Einzelnes WOD generieren (Kategorie auswählen), no - 4-Wochen-Plan als CSV speichern
    if choice == "yes":
        category = input("Which category? (classic, conditioning, gymnastics, oly): ").strip().lower() # Kategorie eingeben
        print(generate_wod(exercises, category)) # einzelnes WOD in der Konsole ausgeben
    else:
        save_plan_to_csv(exercises)
        print("4-week plan created and saved!") #CSV-Datei im Ordner öffnen oder weiter analysieren (z. B. mit Matplotlib).


if __name__ == "__main__":
    main(exercises)
