import json

with open("model.json", "r") as file:
    content = json.load(file)

t_list = content["t"]
d_list = content["d"]

d_len = len(d_list)
t_len = len(t_list)

print("Определение ориентировочной плотности насыщенного водяного пара по заданному интервалу.")
input = input('Введите значение температуры, оС: ')

# краш тест на пустое / буквенное значение
try:
    t = float(input)

    # вхождение в интервал
    if (t < t_list[0]) or (t > t_list[t_len-1]):
        print('Заданное значение температуры', t,
              'оС находится за пределами интерполяции!')
        print('Интерполяция доступна в пределах значений температуры от',
              t_list[0], 'до', t_list[t_len-1], 'оС')

    # расчет температуры пара методом линейной интерполяции
    else:
        for i in range(0, t_len):
            if t == t_list[i]:
                d = d_list[i]
            else:
                if (t > t_list[i]) and (t < t_list[i+1]):
                    d = d_list[i]+((d_list[i+1]-d_list[i]) /
                                   (t_list[i+1]-t_list[i]))*(t-t_list[i])

    # вывод расчетной температуры пара
        print('Расчетная плотность пара составляет:', d, 'кг/м3')

except ValueError:
    print("Value cannot be empty or a string! Only a float number. Reload a programm to try another one.")
