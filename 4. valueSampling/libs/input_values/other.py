import sys
from types import SimpleNamespace


def input_other(lang):
    other = SimpleNamespace()

    other.consumption = float(
        input("Consumption [m3 / h]: " if lang == "EN" else "Расход [м3 / ч]: "))
    other.difference = int(
        input(
            'Limiting float points\' difference between two values of heat transfer coefficient (for example,"2" will stop loop if (K2 - K1) < 0.01): '
            if lang == "EN"
            else 'Количество знаков после запятой (например, "2" будет означать окончание цикла, если (K2 - K1) < 0.01): '
        ))
    other.amount = int(
        input(
            "Amount of calculating heat transfer coefficient: "
            if lang == "EN"
            else "Максимальное количество циклов для рассчета: "
        ))
    return other



sys.modules[__name__] = input_other