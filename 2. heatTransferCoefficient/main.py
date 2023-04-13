from types import SimpleNamespace
import sys
sys.path.append("./libs")
sys.path.append("./libs/utils")

import interpolation
import inner_coefficient

tube = SimpleNamespace()
tube.outer_diameter = 25 # mm
tube.wall_width = 2 # mm
tube.wall_heat_conduction = 42 # W / (m * K)

vapor = SimpleNamespace()
vapor.absolute_pressure = [1.0, 1.6, 2.0, 3.0, 4.0] # kgf / cm2
vapor.saturation_temperature = [99, 113, 120, 133, 143] # C
vapor.condensation_heat = [2264, 2227, 2208, 2171, 2141] # kJ / kg

condensate = SimpleNamespace()
condensate.temperature = [20, 50, 100, 120, 150] # C
condensate.density = [998, 998, 958, 943, 917] # kg / m3
condensate.viscosity = [0.0010, 0.0005, 0.0003, 0.0002, 0.0002] # Pa * s
condensate.heat_capacity = [4183, 4181, 4220, 4250, 4313]  # J / (kg * K)
condensate.heat_conductivity = [0.599, 0.648, 0.683, 0.686] # W / (m * K)

lang = "EN" if not (input("Continue with English? (Any keyword - English; N - Russian)") == "N") else "RU"
print("Hello! This programm has been made for... Please enter some input data you need to calculate.")

coefficients = SimpleNamespace()
coefficients.density = float(input("Density coefficient: " if lang == "EN" else "Коэффициент плотности: "))
coefficients.viscosity = float(input("Viscosity coefficient: " if lang == "EN" else "Коэффициент вязкости: "))
coefficients.heat_capacity = float(input("Heat capacity coefficient: " if lang == "EN" else "Коэффициент теплоемкости: "))
coefficients.heat_conductivity = float(input("Heat conductivity coefficient: " if lang == "EN" else "Коэффициент теплопроводности: "))

temperature = SimpleNamespace()
temperature.vapor = float(input("Vapor temperature: "))
temperature.condensate = float(input("Condensate temperature: "))
temperature.start = float(input("Temperature of the water at the start: "))
temperature.end = float(input("Temperature of the water at the end: "))

consumption = float(input("Consumption [m3 / h]: "))
difference = float(input("Triggering difference between two values of heat transfer coefficient K: "))
amount = int(input("Amount of calculating heat transfer coefficient: "))


if (temperature.end > temperature.vapor): 
    raise ValueError("Vapor temparature must be greater than temparature of the water at the end point.")

###

user_vapor = interpolation.calc_vapor(vapor, temperature.vapor)
user_condensate = interpolation.calc_condensate(condensate, temperature.condensate)

a1 = inner_coefficient(user_condensate, tube, consumption)
print(a1)
