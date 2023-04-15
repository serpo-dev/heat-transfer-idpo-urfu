import sys
import math

def inner_coefficient(condensate, tube, consumption):
    d = tube.outer_diameter
    ww = tube.wall_width
    v = condensate.viscosity
    cap = condensate.heat_capacity
    cond = condensate.heat_conductivity
    p = condensate.density
    Q = consumption

    S = (math.pi * (((d - (2 * ww)) ** 2) / 4)) / 1000000 # mm -> m
    w = Q / S

    Re = w * d * p / v

    Pr = v * cap / cond 

    Nu = 0.021 * (Re ** 0.8) * (Pr ** 0.43)

    a1 = Nu * cond / d

    return a1


sys.modules[__name__] = inner_coefficient