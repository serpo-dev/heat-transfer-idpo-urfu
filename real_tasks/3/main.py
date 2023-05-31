import csv

import matplotlib.pyplot as plt

#   o Интерполяция – повышение частоты дискретизации в целое число раз;
#   o Прореживание (децимация) – понижение частоты дискретизации в целое число раз;
#   o Передискретизация – изменение частоты дискретизации в произвольное (в общем случае дробное) число раз.

VOLT_COEFF = 0.153269
FILENAME = "tv_paced.csv"
FREQUENCY = 250

DOWNSAMPLING_COEFF = int(input("Enter the downsampling ratio (must be an integer and between 2 and 10): "))
if (DOWNSAMPLING_COEFF > 10 or DOWNSAMPLING_COEFF < 2): 
    raise ValueError("Downsampling ratio must be between 2 and 10")
GRAPH_SAMPLE_LENGTH = 1000


def read_data(path):
    with open(path) as csvfile:
        data = [int(row[0].strip()) * VOLT_COEFF for row in csv.reader(csvfile)]
    return data

def draw(voltage, time_coeff, name):
    time = [i * time_coeff / FREQUENCY for i in range(len(voltage))]

    plt.figure(figsize=[19.2, 10.8])
    plt.plot(time, voltage)
    plt.xlabel("Время (с)")
    plt.ylabel("мкВ")
    plt.title("DOWNSAMPLING_COEFF = {}".format(DOWNSAMPLING_COEFF) if name == "downsampling" else "NO DOWNSAMPLING")
    plt.grid(True)
    plt.savefig("downsampling_{}.png".format(DOWNSAMPLING_COEFF) if name == "downsampling" else "no_downsampling.png")
    plt.close()
        
def downsampling(data):
    new_data = []
    window_size = 2 * DOWNSAMPLING_COEFF

    i = 0
    while len(new_data) < len(data) // DOWNSAMPLING_COEFF:
        window = data[i : i + window_size ]
        i += window_size
        
        left = window[0:DOWNSAMPLING_COEFF]
        right = window[DOWNSAMPLING_COEFF:window_size]
        
        max_r = max(right)
        max_l = max(left)
        min_r = min(right)
        min_l = min(left) 

        if max_r > max_l:
            new_data.append(min_l)
            new_data.append(max_r)
        else:
            new_data.append(min_r)
            new_data.append(max_l)

    i -= window_size
    if len(data) % DOWNSAMPLING_COEFF > 0:
        window = data[i : ]
        average = sum(window)  / len(window)
        new_data.append(average)
        
    return new_data


voltage = read_data(FILENAME)
voltage_dwnsmp = downsampling(data=voltage)

draw(voltage=voltage[:GRAPH_SAMPLE_LENGTH], time_coeff=1, name="default")
draw(voltage=voltage_dwnsmp[:GRAPH_SAMPLE_LENGTH // DOWNSAMPLING_COEFF], time_coeff=DOWNSAMPLING_COEFF, name="downsampling")

print("Before: length = %s" % len(voltage),"and", "frequency = %s Hz." % (FREQUENCY))
print("After: length = %s" % len(voltage_dwnsmp),"and", "frequency = %s Hz." % (FREQUENCY / DOWNSAMPLING_COEFF))
print('Completed! Check the files "no_downsampling.png" and "downsampling_{}.png" to see the result.'.format(DOWNSAMPLING_COEFF))