# According to the individual option

friction_coefficient = 0.03
fluid_density = 1186.4 # KOH (10%) [kg / m3]
w_user = input("Введите значение скорости своего варианта [м / с]: ")

# Standart values of external diameters 
diameters = [12, 15, 20, 25, 32, 38, 45, 57, 76, 89, 108, 133]


def main(diameters, w_user):

    # Physics constants
    g = 9.81
    H = 2.5
    n = 20.5
    l = 5

    def scan(w_min = None, d_min = None, delta_min = -1):
        for d_ex in diameters:
            d = d_in(d_ex)
            w = Bernoulli(d)

            isMin, cur_delta = delta(w, w_user, delta_min)
            if isMin: 
                w_min = w
                d_min = d_ex
                delta_min = cur_delta

        return "%.3f" % w_min, d_min

    def Bernoulli(d):
        w = (2 * g * H / (1 + n * friction_coefficient * l / (d / 1000))) ** (1 / 2)
        return w

    def d_in(d_ex):
        if (d_ex <= 32): return d_ex - (2 * 2)
        elif (d_ex <= 57): return d_ex - (3 * 2)
        else: return d_ex - (4 * 2)

    def delta(w, w_user, delta_min):
        cur_delta = abs(float(w) - float(w_user))

        if cur_delta < delta_min or delta_min == -1:
            return True, cur_delta
        else:
            return False, None


    return scan

def output(w_min, d_min): 
    print("Расчетная скорость по табличному диаметру " + str(w_min) + " м / с")
    print("Внешний диаметр трубы по таблице: " + str(d_min) + " мм")


w_min, d_min = main(diameters, w_user)()

output(w_min, d_min)