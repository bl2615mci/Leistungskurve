import os
import matplotlib.pyplot as plt

from load_data import load_data
from sort import bubble_sort


def main():
    #csv
    data = load_data("activity.csv")
    power_values = data["PowerOriginal"]
    power_values = list(power_values)

    #sort
    sorted_values = bubble_sort(power_values)
    sorted_values = sorted_values[::-1]

    #figures
    os.makedirs("figures", exist_ok=True)

    #graph
    plt.figure(figsize=(10, 5))
    plt.plot(sorted_values)

    plt.xlabel("Sortierte Messpunkte")
    plt.ylabel("Leistung (W)")
    plt.title("Power Curve")
    plt.grid(True)
    
    plt.savefig("figures/power_curve.png")

    print("Grafik gespeichert unter figures/power_curve.png")


if __name__ == "__main__":
    main()
