
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

tube, vapor, condensate = config()
lang, coefficients, temperature, other = input_values()

user_condensate = custom_cond(condensate, coefficients)
user_vapor = interpolation.calc_vapor(vapor, temperature.vapor)
init, w = outer_init(tube, user_vapor, user_condensate, temperature, other)

print("Initial value of heat transfer coefficient: " if lang == "EN" else "Первое найденное значение коэффициента теплопередачи:", init.K)

K, i = loop(init, tube, user_vapor, user_condensate, temperature, other) 

print("The resulting value is: " if lang == "EN" else "Результат: " + str(K))
print("The amount of loops is " if lang == "EN" else "Количество итераций: " + str(i))

new(w, coefficients.density)

input(
    "Press Enter to close the programm."
    if lang == "EN"
    else "Нажмите Enter для закрытия программы"
)