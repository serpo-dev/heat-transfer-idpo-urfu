import sys
from types import SimpleNamespace


def input_temperature(lang):
    temperature = SimpleNamespace()
    temperature.vapor = float(input("Vapor temperature [°C]: "if lang == "EN" else "Температура пара [°C]: "))
    temperature.start = float(input("Temperature of the water at the start [°C]: " if lang == "EN" else "Температура раствора в начале [°C]: "))
    temperature.end = float(input("Temperature of the water at the end [°C]: " if lang == "EN" else "Температура подачи в конце [°C]: "))

    if temperature.end > temperature.vapor:
        raise ValueError(
            "Vapor temparature must be greater than temparature of the water at the end point."
        )

    return temperature

sys.modules[__name__] = input_temperature