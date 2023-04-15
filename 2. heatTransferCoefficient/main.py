
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
import config

tube, vapor, condensate = config
coefficients, temperature, other = input_values()



user_vapor = interpolation.calc_vapor(vapor, temperature.vapor)
init = outer_init(tube, user_vapor, condensate, temperature, other)


K, i = loop(init, tube, user_vapor, condensate, temperature, other) 

print("The resulting value is: " + str(K))
print("The amount of loops is " + str(i))
