import sys

def change_water_temp(Q_ufl, G, condensate):
    c = condensate.heat_conductivity
    
    dt_water = Q_ufl / (G * c)
   
    return dt_water

sys.modules[__name__] = change_water_temp