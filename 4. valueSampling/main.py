
import sys

sys.path.append("./libs")
sys.path.append("./libs/init")
sys.path.append("./libs/input_values")
sys.path.append("./libs/loop")
sys.path.append("./libs/utils")


import config
from libs import interpolation
from libs.init import custom_cond, outer_init
from libs.input_values import input_values
from libs.loop import loop
from libs.part_calc import full_thermal_power, consumption, useful_thermal_power, change_water_temp


tube, vapor, condensate = config()
lang, coefficients, temperature, other = input_values()

amount_of_parts = int(input("На сколько частей поделить трубу для расчета?"))
tube.length /= amount_of_parts

temp_diff = temperature.end - temperature.start
temp_part = temp_diff / amount_of_parts


for j in range(amount_of_parts):
    user_condensate = custom_cond(condensate, coefficients)
    user_vapor = interpolation.calc_vapor(vapor, temperature.vapor)
    
    if j > 0:
       temperature.start += temp_part
    temperature.end = temperature.start + temp_part
    
    init, w = outer_init(tube, user_vapor, user_condensate, temperature, other)
    K, i = loop(init, tube, user_vapor, user_condensate, temperature, other) 
   
    Q = full_thermal_power(K=K, temperature=temperature, tube=tube, delta_l = tube.length)
    G = consumption(condensate=init.c, w=w, tube=tube, coefficients=coefficients)
    Q_ufl = useful_thermal_power(Q=Q, coefficients=coefficients)
    dt_water = change_water_temp(G=G, condensate=init.c, Q_ufl=Q_ufl)
    
    print("{}) K = {} Вт/(м2*K); Q = {} Вт; G = {} кг/с; Q_полезн = {} Вт; dt_воды = {} К".format(j, "%.2f" % (K), "%.2f" % (Q), "%.2f" % (G), "%.2f" % (Q_ufl), "%.2f" % (dt_water),))

input(
    "Press Enter to close the programm."
    if lang == "EN"
    else "Нажмите Enter для закрытия программы"
)