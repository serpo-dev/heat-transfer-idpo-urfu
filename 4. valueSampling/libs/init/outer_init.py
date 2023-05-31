import sys
from types import SimpleNamespace


from libs.init import inner_coeff
from libs.utils import formula




def outer_init(tube, vapor, condensate, temperature, other):
    t_s = formula.sol_temp(temperature)

    t_w = formula.wall_temp_init(temperature)
    t_c = formula.cond_temp(temperature, t_w)
    c = formula.cond(condensate, t_c)

    a1, w = inner_coeff(c, tube, other.consumption)
    a2 = formula.outer_coeff(t_c, t_w, tube, vapor, c)

    K = formula.heat_transfer(a1, a2, tube)
    return SimpleNamespace(t_s=t_s, t_w=t_w, a1=a1, K=K, c=c),  w

sys.modules[__name__] = outer_init