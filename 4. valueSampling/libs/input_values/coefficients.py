import sys
from types import SimpleNamespace

def input_coefficients(lang):
    coefficients = SimpleNamespace()

    coefficients.density = float(input("Density coefficient (>= 1): " if lang == "EN" else "Коэффициент плотности (>= 1): "))
    if (coefficients.density < 1):
        raise ValueError(
            "Density coefficient must be more or equal to 1."
        ) 

    coefficients.viscosity = float(input("Viscosity coefficient (>= 1): " if lang == "EN" else "Коэффициент вязкости (>= 1): "))
    if (coefficients.viscosity < 1):
        raise ValueError(
            "Viscosity coefficient must be more or equal to 1."
        ) 
    
    coefficients.heat_capacity = float(input("Heat capacity coefficient (=< 1): " if lang == "EN" else "Коэффициент теплоемкости (=< 1): "))
    if (coefficients.heat_capacity > 1):
        raise ValueError(
            "Heat capacity coefficient must be less or equal to 1."
        ) 

    coefficients.heat_conductivity = float(input("Heat conductivity coefficient (=< 1): " if lang == "EN" else "Коэффициент теплопроводности (=< 1): "))
    if (coefficients.heat_conductivity > 1):
        raise ValueError(
            "Heat conductivity coefficient must be less or equal to 1."
        ) 
        
    coefficients.heat_loss = float(input("Heat-loss coefficient (0.02-0.05): " if lang == "EN" else "Коэффициент потерь тепла (0.02-0.05): "))
    if (coefficients.heat_loss < 0.02 or coefficients.heat_loss > 0.05):
        raise ValueError(
            "Heat-loss coefficient must be in a range from 0.02 to 0.05."
        ) 

    return coefficients

sys.modules[__name__] = input_coefficients