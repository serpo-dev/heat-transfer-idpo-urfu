import sys

from libs.input_values import coefficients
from libs.input_values import temperature
from libs.input_values import other 

def input_values():
    lang = "RU" if not (input("Продолжить на русском? (Любая клавиша - Русский; N - English)") == "N") else "EN"
    print("Hello! This programm has been made for calculating heat transfer coefficient." if lang == "EN" else "Привет, данная программа была создана для подсчета коэффециента теплопередачи.")
    if (lang == "RU"):
        print("Авторы программы - студенты гр. Х-300007, а именно Власова А., Глебова Д., Дернина Д., Лежнева Ю., Потапов С.")
    print("For more information read file README.md in the root catalog." if lang == "EN" else "Больше информации о том, как ей пользоваться, можно найти в файле README.md")
    print("Please enter some input data you need to calculate." if lang == "EN" else "Пожалуйста, далее появятся поля для ввода данных для расчета.")

    c = coefficients(lang)
    t = temperature(lang)
    o = other(lang)

    return c, t, o

    

sys.modules[__name__] = input_values

