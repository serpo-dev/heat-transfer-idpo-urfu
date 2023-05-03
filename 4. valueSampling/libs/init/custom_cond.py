import sys


def custom_cond(condensate, coefficients):
    condensate.density = [coefficients.density * x for x in condensate.density]
    condensate.viscosity = [coefficients.viscosity * x for x in condensate.viscosity]
    condensate.heat_capacity = [coefficients.heat_capacity * x for x in condensate.heat_capacity]
    condensate.heat_conductivity = [
        coefficients.heat_conductivity * x for x in condensate.heat_conductivity
    ]
    return condensate


sys.modules[__name__] = custom_cond