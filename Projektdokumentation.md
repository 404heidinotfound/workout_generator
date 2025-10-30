# Workout Generator
Heike Czopiak

## Projektbeschreibung
MeinProjekt erstellt zufällige CrossFit-Workouts (Workouts of the Day, WODs) auf Basis einer Excel, bzw. CSV-Datei mit Übungen 
Es kann entweder ein einzelnes WOD generieren oder einen 4-Wochen-Trainingsplan im CSV-Format speichern

Die Übungen sind in Kategorien unterteilt:
- Classic (klassisches CrossFit WOD)
- Conditioning
- Gymnastics
- Oly (Strength & Olympic Weightlifting)

Die Pläne orientieren sich an den CrossFit-Regeln und Formaten (z. B. AMRAP - as many reps as possible, EMOM - every minute on the minute, For Time)

---

## Funktionen
- CSV-Einlesen: Übungen werden mit Kategorien, Gewicht und Skalierung geladen
- Zufallsgenerator: Übungen, Wiederholungen und Formate werden mit random Modul kombiniert
- Individuelles WOD: Ein einzelnes Workout für eine Kategorie wird angezeigt
- 4-Wochen-Plan: Ein kompletter Plan mit 3 Trainingstagen pro Woche wird als CSV gespeichert 
- die CSV wird mit matplotlib als Pie Chart angezeigt, d.h. eine Verteilung der Kategorien im Plan
- Regeln: Jede Kategorie hat eigene Regeln, also Formate, Dauer und Anzahl an Übungen

---

## Aufbau des Codes
- load_exercises_from_csv(): Lädt alle Übungen aus einer CSV-Datei
- filter_exercises_by_category(): Filtert Übungen nach Kategorie
- generate_exercise_specs(): Bestimmt Wiederholungen, Einheit (z. B. Reps, Meter), Gewicht und Scaling --> Spezifika der WODs
- generate_wod(): Erstellt ein einzelnes Workout (Textausgabe)
- save_plan_to_csv(): Speichert den 4-Wochen Trainingsplan als CSV-Datei
- main(): Fragt den User, ob ein WOD oder ein Plan erstellt werden soll.

---

## Eingabedatei (CSV)
Die Eingabe-CSV (exercises_no_benchmarks.csv) enthält:
- Übungsname
- Gewicht (falls vorhanden)
- Skalierung (falls vorhanden)
- Kategorien (classic, conditioning, gymnastics, oly)

Beispiel:
exercise,weight,scaling,classic,conditioning,gymnastics,oly
Front Squats,50/35kg,,x,,,x
Burpees,,,x,x,,
Pullups,,,x,,x,

---

## Ausgabe
- Einzelnes WOD: Textausgabe in der Konsole
- Trainingsplan: 4_week_workout_plan.csv automatisch runtergeladen

---

## Nutzung
1. Python starten
2. Frage beantworten:
   - yes: Einzelnes WOD generieren (Kategorie auswählen)
   - no: 4-Wochen-Plan als CSV speichern
3. CSV-Datei im Ordner öffnen oder weiter analysieren

## Herausforderungen
- Levels (Beginner, Intermediate und Advanced konnten aus Zeit- und Skills-Gründen nicht umgesetzt werden)
- Visualisierung wurde auf ein Pie Chart begrenzt mit den Verteilungen der Kategorien über den 4-Wochenplan, weitere Visualisierungen für mich noch zu komplex
- ursprünglich waren Integration von sog. Benchmark-Workouts geplant, dies erwies sich aber als zu komplex
- derzeit erstellt der Generator noch einige "seltsame" Workout-Kombinationen, wie man in der Realtität trainieren würde
    z.B.: 
    ungerade EMONS (es gibt kein EMOM 17 Minuten), 
    random Zusammenstellung der Übungen kann dazu führen, dass in einem WOD Backsquats und Frontsquats vorkommen, das würde man nicht machen
    Gewichts- und Skalierungsanweisungen sind noch sehr rudimentär
    User muss korrekt antworten, sonst keine Ausgabe
