# 4-Wochen-Plan bearbeiten, einlesen, matplotlib - pie chart mit Verteilung der Workout Kategorien

# Module importieren
import matplotlib.pyplot as plt
import csv
import os
from collections import Counter

filename = r"C:\Users\Administrator\Documents\Programmieren mit Python\06_Project\output_workout_generator\4_week_workout_plan.csv"

if not os.path.exists(filename):
    print("Datei nicht gefunden:", filename)
else:
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        categories = [row["category"] for row in reader if "category" in row]

    # Häufigkeiten zählen
    counts = Counter(categories)

    # Pie Chart zeichnen
    plt.pie(counts.values(), labels=counts.keys(), autopct="%.1f%%")
    plt.title("Distribution of workout categories", fontsize=14)
    plt.show()

