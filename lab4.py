import numpy as np
import matplotlib.pyplot as plt
from math import pi

variant = 24

wave_len = 0.03
distance = 0.30
length = 0.237

xi = 1 + wave_len / (2 * length)
half_power = 0.707

angle_deg = np.arange(0, 90, 0.01)
angle_rad = np.radians(angle_deg)

running_wave = np.abs(
    (
        np.sin((pi * length / wave_len) * (xi - np.cos(angle_rad)))
        / np.sin((pi * length / wave_len) * (xi - 1))
    )
    * ((xi - 1) / (xi - np.cos(angle_rad)))
)

single_E = np.abs(running_wave * np.cos(angle_rad))
single_H = np.abs(running_wave)

array_factor = np.abs(
    np.cos((pi * distance / wave_len) * np.sin(angle_rad))
)

double_E = np.abs(single_E * array_factor)
double_H = np.abs(single_H * array_factor)

single_E /= np.max(single_E)
single_H /= np.max(single_H)
double_E /= np.max(double_E)
double_H /= np.max(double_H)


def beam_width(pattern):
    for i, value in enumerate(pattern):
        if value < half_power:
            return 2 * angle_deg[i]
    return 0


def search_extremes(x, y):
    maxima_x = []
    maxima_y = []
    minima_x = []
    minima_y = []

    for i in range(1, len(y) - 1):

        if y[i] > y[i - 1] and y[i] > y[i + 1]:
            maxima_x.append(x[i])
            maxima_y.append(y[i])

        if y[i] < y[i - 1] and y[i] < y[i + 1]:
            minima_x.append(x[i])
            minima_y.append(0)

    return maxima_x, maxima_y, minima_x, minima_y


def print_results(title, pattern):

    max_x, max_y, min_x, min_y = search_extremes(
        angle_deg,
        pattern
    )

    print(f"\n--- {title} ---")

    print("Табл. 1 - Значення нульових кутів")
    print("| № |   θ   | F(θ) |")

    for num, (x, y) in enumerate(zip(min_x, min_y), start=1):
        print(f"| {num} | {x:5.2f} | {y:5.2f} |")

    print()

    print("Табл. 2 - Значення максимальних кутів")
    print("| № |   θ   | F(θ) |")

    for num, (x, y) in enumerate(zip(max_x, max_y), start=1):
        print(f"| {num} | {x:5.2f} | {y:5.2f} |")

    print(f"\nШирина головної пелюстки = {beam_width(pattern):.2f}°")


print(f"Варіант = {variant}")
print(f"Довжина хвилі = {wave_len} м")
print(f"Відстань між стрижнями h = {distance} м")
print(f"Довжина стрижня l = {length} м")
print(f"Коефіцієнт уповільнення ξ = {xi:.3f}")

print_results("Одно-стрижнева ДСА, площина E", single_E)
print_results("Одно-стрижнева ДСА, площина H", single_H)
print_results("Дво-стрижнева ДСА, площина E", double_E)
print_results("Дво-стрижнева ДСА, площина H", double_H)

plt.figure("Одно-стрижнева ДСА E", figsize=(10, 6))
plt.plot(angle_deg, single_E, label=r"$F_E(\theta)$")
plt.axhline(half_power, linestyle="--")
plt.grid()
plt.xlabel(r"$\Theta^\circ$")
plt.ylabel(r"$|F_E(\theta)|$")
plt.title("ДС одно-стрижневої ДСА у площині E")
plt.legend()

plt.figure("Одно-стрижнева ДСА H", figsize=(10, 6))
plt.plot(angle_deg, single_H, label=r"$F_H(\theta)$")
plt.axhline(half_power, linestyle="--")
plt.grid()
plt.xlabel(r"$\Theta^\circ$")
plt.ylabel(r"$|F_H(\theta)|$")
plt.title("ДС одно-стрижневої ДСА у площині H")
plt.legend()

plt.figure("Дво-стрижнева ДСА E", figsize=(10, 6))
plt.plot(angle_deg, double_E, label=r"$F_E(\theta)$")
plt.axhline(half_power, linestyle="--")
plt.grid()
plt.xlabel(r"$\Theta^\circ$")
plt.ylabel(r"$|F_E(\theta)|$")
plt.title("ДС дво-стрижневої ДСА у площині E")
plt.legend()

plt.figure("Дво-стрижнева ДСА H", figsize=(10, 6))
plt.plot(angle_deg, double_H, label=r"$F_H(\theta)$")
plt.axhline(half_power, linestyle="--")
plt.grid()
plt.xlabel(r"$\Theta^\circ$")
plt.ylabel(r"$|F_H(\theta)|$")
plt.title("ДС дво-стрижневої ДСА у площині H")
plt.legend()

plt.show()