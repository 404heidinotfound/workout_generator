# Testumgebung Workoutgenerator

def generate_wod(exercises): # Kategorie wählen
    categories = ["classic", "conditioning", "gymnastics", "oly"]
    category = random.choice(categories)
    rules = wod_rules[category]

    filtered = filter_exercises_by_category(exercises, category) # Übung aus der Kategorie ziehen
    if not filtered:
        return "no exercise in this category"
    exercise_name, exercise_info = random.choice(filtered)

    min_ex, max_ex = rules["exercises"] # Anzahl Übungen bestimmen
    num_ex = random.randint(min_ex, max_ex)
    chosen = random.sample(filtered, num_ex)

    fmt = random.choice(formats[category])  # Format und Dauer
    duration = None
    if rules["duration"]:
        duration = random.randint(*rules["duration"])

    specs_list = [] # workout Spezifika
    for exercise_name, exercise_info in chosen:
        specs = generate_exercise_specs(exercise_name, exercise_info, category, level="rx")
        specs["weight"] = exercise_info["weight"] or "n. a."
        specs["scaling"] = exercise_info["scaling"] or "nach Bedarf anpassen"
        specs_list.append(specs)

    wod_text = f"\nYour Workout of the day: " # Ausgabe
    wod_text += f"Format: {fmt}\n"
    if duration:
        wod_text += f"Duration: {duration} minutes\n"
    wod_text += "-"*40 + "\n"

    for s in specs_list:
        wod_text += f"- {s['exercise']}: {s['amount']} {s['unit']} (Gewicht: {s['weight']}, Scaling: {s['scaling']})\n"

    if "hint" in rules:     # Extra-Hinweis (falls definiert)
        wod_text += f"\nHinweis: {rules['hint']}\n"

    return wod_text


### test alt

def test_random_exercise():
    wod = random.choice(exercises)
    print("Dein zufälliges Workout:", wod["name"], "-", wod["category"])

test_random_exercise()


#Fragt den User: Einzel-WOD oder 4-Wochenplan
def get_user_choice(): 
    pass

#  Erstellt ein WOD basierend auf Level & Kategorie
def generate_single_wod(level, category):
   
    pass


# Generiert 16 Workouts (4 pro Woche, 1 pro Kategorie)

def generate_four_week_plan():
    pass


# Speichert den 4-Wochenplan als CSV-Datei

def export_csv(plan):
    pass

# Erstellt Diagramme aus dem Plan
def create_visualizations(plan):
    pass



# Funktion: filter_exercises_by_category
# --------------------------------------
# Input: Liste von Übungen (exercises), gewählte Kategorie (z. B. "classic")
# Output: neue Liste mit allen Übungen, die diese Kategorie enthalten

# Schritte:
# - Leere Liste anlegen
# - Über alle exercises iterieren
# - Wenn category in exercise["category"] drin ist -> zur Liste hinzufügen
# - Gefilterte Liste zurückgeben


# Funktion: generate_single_wod
# -----------------------------
# Input: Level (beginner, intermediate, advanced), Kategorie (classic, gymnastics, conditioning, oly)
# Output: Dictionary oder String mit allen Infos zum Workout (Format, Dauer, Übungen, Scaling, Warmup Hinweis)

# Schritte:
# - Falls classic gewählt:
#   -> fragen ob Benchmark ja/nein
#   -> wenn ja: random Benchmark zurückgeben
#   -> wenn nein: aus gefilterten classic-Übungen random Übungen auswählen
# - Falls andere Kategorie gewählt:
#   -> Übungen aus dieser Kategorie filtern
#   -> random Übungen auswählen
# - Zufälliges WOD-Format auswählen (aus dict/list formats)
# - Dauer aus Liste zufällig wählen
# - Scaling anhand Level anpassen (z. B. dict mit Optionen für beginner/intermediate/advanced)
# - Alles in ein dict packen: { "category": ..., "format": ..., "duration": ..., "exercises": ..., "scaling": ... }
# - Warmup-Hinweis anhängen
# - Am Ende dict oder String zurückgeben


import random

# -----------------------------
# 1. Datenbasis
# -----------------------------

# Übungen (kleine Auswahl zum Start)
exercises = [
    {"name": "Air Squats", "category": ["classic", "conditioning"]},
    {"name": "Burpees", "category": ["classic", "conditioning"]},
    {"name": "Pullups", "category": ["classic", "gymnastics"]},
    {"name": "Barbell Snatch", "category": ["classic", "oly"]},
    {"name": "Murph", "category": ["classic"], "type": "benchmark"},
    {"name": "Fran", "category": ["classic"], "type": "benchmark"}
]

# WOD-Formate
wod_formats = ["AMRAP", "EMOM", "For Time", "Chipper"]

# Dauer (später kannst du hier echte Minutenwerte hinterlegen)
durations = ["short", "medium", "long"]

# Scaling-Regeln
scaling = {
    "Beginner": {"reps": 0.5, "weight": 0.5, "note": "halbe Wiederholungen & halbes Gewicht"},
    "Intermediate": {"reps": 0.75, "weight": 0.75, "note": "mittleres Volumen"},
    "RX": {"reps": 1.0, "weight": 1.0, "note": "Standard - as prescribed"}
}

# -----------------------------
# 2. Funktionen
# -----------------------------

def test_random_exercise():
    #Einfach nur zufällig eine Übung ausgeben.
    wod = random.choice(exercises)
    print("Deine zufällige Übung:", wod["name"], "-", wod["category"])


def test_random_wod(level="RX"):
    #Mini-WOD bauen mit Übung, Format, Dauer und Scaling
    ex = random.choice(exercises)
    fmt = random.choice(wod_formats)
    dur = random.choice(durations)
    scale = scaling[level]["note"]

    print("\n🎯 Dein Test-WOD:")
    print(f"- Übung: {ex['name']} ({ex['category']})")
    print(f"- Format: {fmt}")
    print(f"- Dauer: {dur}")
    print(f"- Level ({level}): {scale}")
    print("Warm-up 10–15 min + Skill Practice nicht vergessen!\n")


# -----------------------------
# 3. Hauptprogramm
# -----------------------------
if __name__ == "__main__":
    print("Workout Generator Testlauf")
    test_random_exercise()
    test_random_wod("Beginner")
    test_random_wod("Intermediate")
    test_random_wod("RX")
