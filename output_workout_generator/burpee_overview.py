# 4-Wochen-Plan bearbeiten, einlesen, matplotlib - Burpee Overview
import matplotlib.pyplot as plt
import csv
import os
from collections import Counter

filename = r"C:\Users\Administrator\Documents\Programmieren mit Python\06_Project\output_workout_generator\4_week_workout_plan.csv"

burpees_per_week = defaultdict(int)

with open(filename, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        exercise = row["exercise"]
        reps = row["amount"]

        if "burpee" in exercise.lower():
            try:
                reps = int(reps)
            except:
                reps = 0
            burpees_per_week[int(row["week"])] += reps

weeks = sorted(burpees_per_week.keys())
values = [burpees_per_week[w] for w in weeks]

plt.plot(weeks, values, marker="o", linestyle="-")
plt.title("Burpees per week", fontsize=14)
plt.xlabel("Week")
plt.ylabel("Number of Burpees")
plt.grid(True)
plt.show()


import matplotlib.pyplot as plt
import csv
import os
from collections import defaultdict

filename = r"C:\Users\Administrator\Documents\Programmieren mit Python\06_Project\output_workout_generator\4_week_workout_plan.csv"

# Dictionary für Burpees pro Tag (Key = "Week-Day")
burpees_per_day = defaultdict(int)

with open(filename, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        exercise = row["exercise"]
        reps = row["amount"]

        if "burpee" in exercise.lower():   # alle Burpee-Varianten abfangen
            try:
                reps = int(reps)
            except:
                reps = 0
            key = f"Week{row['week']}-Day{row['day']}"
            burpees_per_day[key] += reps

# sortieren nach Zeit
days = sorted(burpees_per_day.keys(),
              key=lambda x: (int(x.split("-")[0][4:]), int(x.split("-")[1][3:])))
values = [burpees_per_day[d] for d in days]

# Plot
plt.plot(days, values, marker="o", linestyle="-")
plt.title("Burpees per day", fontsize=14)
plt.xlabel("Day")
plt.ylabel("Number of Burpees")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
