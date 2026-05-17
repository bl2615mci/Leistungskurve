import os
import matplotlib.pyplot as plt

from load_data import load_data
from sort import bubble_sort


def main():
    # Daten aus CSV laden
    data = load_data("activity.csv")

    # Leistungswerte auslesen
    power_values = data["PowerOriginal"]

    # In Liste umwandeln
    power_values = list(power_values)

    # Mit eigenem Sortieralgorithmus sortieren
    sorted_values = bubble_sort(power_values)

    # Umdrehen: größte Werte zuerst
    sorted_values = sorted_values[::-1]

    # Ordner figures erstellen
    os.makedirs("figures", exist_ok=True)

    # Grafik erstellen
    plt.figure(figsize=(10, 5))
    plt.plot(sorted_values)

    plt.xlabel("Sortierte Messpunkte")
    plt.ylabel("Leistung (W)")
    plt.title("Power Curve")
    plt.grid(True)

    # Grafik speichern
    plt.savefig("figures/power_curve.png")

    print("Grafik gespeichert unter figures/power_curve.png")


if __name__ == "__main__":
    main()