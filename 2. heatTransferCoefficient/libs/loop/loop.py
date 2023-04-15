import sys

import heat_transfer_coefficient

def loop(init, tube, vapor, condensate, temperature, other):
    i = 0
    t_w = init.t_w
    K = init.K
    print("Initial value of heat transfer coefficient: ", K)
    while (i < other.amount):
        i = i + 1
        end = heat_transfer_coefficient(t_w, K, init.a1, init.t_s, tube, vapor, condensate, temperature)
        diff = int(other.difference)
        cur_diff = round(end.K, diff) - round(K, diff)
        if (cur_diff == 0):
            break
        # print(str(i) + ") Difference: %.20f" % (end.K - K))
        t_w = end.t_w
        K = end.K

    return K, i

sys.modules[__name__] = loop