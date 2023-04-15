import sys

import interpolation

round_num = 20

class Formula:
    def wall_temp_init(t):
        wall_temp = (t.vapor + ((t.start + t.end) / 2)) / 2 
        rounded = round(wall_temp, round_num)
        return rounded

    def heat_flux_density(K, temperature):
        t_v = temperature.vapor
        t_s = (temperature.start + temperature.end) / 2
        q = K * (t_v - t_s)
        rounded = round(t_v, round_num), round(t_s, round_num), round(q, round_num)
        return rounded

    def wall_temp_loop(t_v, t_s, q, a1, a2):
        wall_temp = ((t_v - (q / a2)) + (t_s + (q / a1))) / 2 
        rounded = round(wall_temp, round_num)
        return rounded

    def cond_temp(t, wall_temp):
        cond_temp = 0.5 * (t.vapor + wall_temp)
        rounded = round(cond_temp, round_num)
        return rounded

    def cond(condensate, t_c):
        user_condensate = interpolation.calc_condensate(condensate, t_c)
        return user_condensate

    def outer_coeff(t_c, t_w, tube, vapor, c):
        outer_coeff = 0.72 * (((9.82 * (c.density ** 2) * (c.heat_conductivity ** 3) * vapor.condensation_heat * 1000) / (c.viscosity * (t_c - t_w) * tube.outer_diameter)) ** 0.25)
        rounded = round(outer_coeff, round_num)
        return rounded

    def heat_transfer(a1, a2, tube):
        heat_transfer_coeff = 1 / ((1 / a1) + (tube.wall_width / tube.wall_heat_conduction) + (1 / a2))
        rounded = round(heat_transfer_coeff, round_num)
        return rounded


sys.modules[__name__] = Formula