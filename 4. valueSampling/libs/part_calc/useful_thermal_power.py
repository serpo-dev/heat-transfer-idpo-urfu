import sys


def useful_thermal_power(Q, coefficients):
    Q_ufl = Q * (1 - coefficients.heat_loss)
    
    return Q_ufl

sys.modules[__name__] = useful_thermal_power