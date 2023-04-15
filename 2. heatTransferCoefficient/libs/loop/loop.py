import sys
from types import SimpleNamespace

import formula


def loop(prev_t_w, K, a1, tube, vapor, condensate, temperature):
    t_v, t_s, q = formula.heat_flux_density(K, temperature)
    t_c = formula.cond_temp(temperature, prev_t_w)
    c = formula.cond(condensate, t_c)
    a2 = formula.outer_coeff(t_c, prev_t_w, tube, vapor, c)
    t_w = formula.wall_temp_loop(t_v, t_s, q, a1, a2)

    k = formula.heat_transfer(a1, a2, tube)
    print("Next value: ", k)
    return SimpleNamespace(t_w=t_w, a2=a2, K=k)

sys.modules[__name__] = loop