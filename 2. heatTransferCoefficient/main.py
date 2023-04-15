
import sys

sys.path.append("./libs")
sys.path.append("./libs/init")
sys.path.append("./libs/input_values")
sys.path.append("./libs/loop")
sys.path.append("./libs/utils")


from libs.input_values import input_values
from libs import interpolation
from libs.loop import loop
from libs.init import outer_init
from libs.init import custom_cond
import config

tube, vapor, condensate = config()
coefficients, temperature, other = input_values()

user_condensate = custom_cond(condensate, coefficients)
user_vapor = interpolation.calc_vapor(vapor, temperature.vapor)
init = outer_init(tube, user_vapor, user_condensate, temperature, other)


K, i = loop(init, tube, user_vapor, user_condensate, temperature, other) 

print("The resulting value is: " + str(K))
print("The amount of loops is " + str(i))
