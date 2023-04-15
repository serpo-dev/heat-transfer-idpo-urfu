import sys
from types import SimpleNamespace

tube, vapor, condensate = SimpleNamespace(),  SimpleNamespace(), SimpleNamespace()

tube.outer_diameter = 25 # mm
tube.wall_width = 2 # mm
tube.wall_heat_conduction = 42 # W / (m * K)

vapor.absolute_pressure = [1.0, 1.6, 2.0, 3.0, 4.0] # kgf / cm2
vapor.saturation_temperature = [99, 113, 120, 133, 143] # C
vapor.condensation_heat = [2264, 2227, 2208, 2171, 2141] # kJ / kg

condensate.temperature = [20, 50, 100, 120, 150] # C
condensate.density = [998, 998, 958, 943, 917] # kg / m3
condensate.viscosity = [0.0010, 0.0005, 0.0003, 0.0002, 0.0002] # Pa * s
condensate.heat_capacity = [4183, 4181, 4220, 4250, 4313]  # J / (kg * K)
condensate.heat_conductivity = [0.599, 0.648, 0.683, 0.686] # W / (m * K)

def config():
    return tube, vapor, condensate

sys.modules[__name__] = config