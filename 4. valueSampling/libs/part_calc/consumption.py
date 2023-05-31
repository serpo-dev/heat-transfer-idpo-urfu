import sys
import math

def consumption(w, condensate, tube, coefficients):
    d_internal = tube.outer_diameter  - 2 * tube.wall_width
    A = math.pi * ((d_internal / 1000) ** 2) / 4    
    k = coefficients.density
    dens = condensate.density
    
    G = A * w * dens * k / 1000
    
    return G

sys.modules[__name__] = consumption