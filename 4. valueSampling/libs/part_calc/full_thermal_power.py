import math
import sys

def full_thermal_power(K, temperature, tube, delta_l):
    t_mid = (temperature.end - temperature.start) / 2
    delta_t = temperature.vapor - t_mid
    F = math.pi * (tube.outer_diameter / 1000 - tube.wall_width / 1000) * delta_l / 1000
    
    Q = K * F * delta_t
    
    return Q
    
sys.modules[__name__] = full_thermal_power