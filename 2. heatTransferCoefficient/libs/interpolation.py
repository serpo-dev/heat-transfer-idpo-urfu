import sys
from types import SimpleNamespace

import search


class TwoPoints:
    def __init__(self, t1, t2, t):
        self.t1 = t1
        self.t2 = t2
        self.t = t
    
    def find(self, v1, v2):
        return ((v2 - v1) / (self.t2 - self.t1)) * (self.t - self.t1) + v1


class Interpolation:
    def calc_vapor(vapor, vapor_temp):
        pos, is_found = search(
            vapor.saturation_temperature, vapor_temp, 0, len(vapor.saturation_temperature) - 1
        )

        saturation_temperature=vapor_temp

        if is_found is True:
            absolute_pressure=vapor.absolute_pressure[pos]
            condensation_heat=vapor.condensation_heat[pos]
        
        else:
            t1 = vapor.saturation_temperature[pos - 1]
            t2 = vapor.saturation_temperature[pos]
            t = vapor_temp
            two_points = TwoPoints(t1, t2, t)
            
            p1 = vapor.absolute_pressure[pos - 1]
            p2 = vapor.absolute_pressure[pos]
            absolute_pressure = two_points.find(p1, p2)

            h1 = vapor.condensation_heat[pos - 1]
            h2 = vapor.condensation_heat[pos]
            condensation_heat = two_points.find(h1, h2)

        return SimpleNamespace(
                saturation_temperature=saturation_temperature,
                absolute_pressure=absolute_pressure, 
                condensation_heat=condensation_heat
            )

    def calc_condensate(condensate, condensate_temp):
        pos, is_found = search(
            condensate.temperature, condensate_temp, 0, len(condensate.temperature) - 1
        )

        temperature=condensate_temp

        if is_found is True:
            density=condensate.density[pos]
            viscosity=condensate.viscosity[pos]
            heat_capacity=condensate.heat_capacity[pos]
            heat_conductivity=condensate.heat_conductivity[pos]
        
        else:
            t1 = condensate.temperature[pos - 1]
            t2 = condensate.temperature[pos]
            t = condensate_temp
            two_points = TwoPoints(t1, t2, t)
            
            d1 = condensate.density[pos - 1]
            d2 = condensate.density[pos]
            density = two_points.find(d1, d2)

            v1 = condensate.viscosity[pos - 1]
            v2 = condensate.viscosity[pos]
            viscosity = two_points.find(v1, v2)

            cap1 = condensate.heat_capacity[pos - 1]
            cap2 = condensate.heat_capacity[pos]
            heat_capacity = two_points.find(cap1, cap2)

            con1 = condensate.heat_conductivity[pos - 1]
            con2 = condensate.heat_conductivity[pos]
            heat_conductivity = two_points.find(con1, con2)

        return SimpleNamespace(
                temperature=temperature, 
                density=density, 
                viscosity=viscosity, 
                heat_capacity=heat_capacity, 
                heat_conductivity=heat_conductivity
            )

sys.modules[__name__] = Interpolation