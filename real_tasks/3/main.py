import csv
import numpy
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
    plt.title("{}_COEFF_{}".format(name.upper(), DOWNSAMPLING_COEFF) if name != "default" else "NO DOWNSAMPLING")
    plt.grid(True)
    plt.savefig("{}_coeff_{}.png".format(name, DOWNSAMPLING_COEFF) if name != "default" else "no_dwnsmp.png")
    plt.close()
        
        
# METHOD 1 

def dwnsmp_semiwindows(data):
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
        new_data.append(max(window))
        
    return new_data


# METHOD 2

def dwnsmp_prev_diff(data):
    new_data = []
    window_size = DOWNSAMPLING_COEFF

    i = 0
    while len(new_data) < len(data) // DOWNSAMPLING_COEFF:      
        window = data[i : i + window_size ]
        i += window_size
        
        prev = sum(window) / len(window) if i > 0 else new_data[-1]
        
        max_diff_val = max(window, key = lambda cur : abs(cur - prev))
        new_data.append(max_diff_val)
    
    i -= window_size
    if len(data) % DOWNSAMPLING_COEFF > 0:
        window = data[i : ]
        max_diff_val = window.sort(key = lambda cur : abs(cur - new_data[-1]))
        new_data.append(max_diff_val)
        
    return new_data
        
def dwnsmp_avrg_diff(data):
    average = sum(data) / len(data)
    sorted_data = sorted(enumerate(data), key = lambda x : abs(x[1] - average), reverse=True)
    sorted_data_length = len(data) // DOWNSAMPLING_COEFF + 1
    
    new_data_enum = []
    i = 0
    for item in sorted_data:
        if (i >= sorted_data_length):
            break
        if i == 0:
            new_data_enum.append(item)
            i += 1
            continue
        
        if abs(new_data_enum[-1][0] / FREQUENCY - item[0] / FREQUENCY) > (DOWNSAMPLING_COEFF / FREQUENCY):
            new_data_enum.append(item)
            i += 1
    
    new_data_enum_sorted = sorted(new_data_enum, key = lambda x : x[0]) 
    new_data = [d[1] for d in new_data_enum_sorted]
    return new_data



voltage = read_data(FILENAME)

vltg_dwnsmp_mtd_1 = dwnsmp_semiwindows(data=voltage)
vltg_dwnsmp_mtd_2 = dwnsmp_prev_diff(data=voltage)
vltg_dwnsmp_mtd_3 = dwnsmp_avrg_diff(data=voltage)

# Default data
draw(voltage=voltage[:GRAPH_SAMPLE_LENGTH], time_coeff=1, name="default")

# Nethod 1 (not recommended)
draw(voltage=vltg_dwnsmp_mtd_1[:GRAPH_SAMPLE_LENGTH // DOWNSAMPLING_COEFF + 1], time_coeff=DOWNSAMPLING_COEFF, name="dwnsmp_mtd_1")
# Method 2 (not recommended)
draw(voltage=vltg_dwnsmp_mtd_2[:GRAPH_SAMPLE_LENGTH // DOWNSAMPLING_COEFF + 1], time_coeff=DOWNSAMPLING_COEFF, name="dwnsmp_mtd_2")
# Method 3 (recommended)
draw(voltage=vltg_dwnsmp_mtd_3[:GRAPH_SAMPLE_LENGTH // DOWNSAMPLING_COEFF + 1], time_coeff=DOWNSAMPLING_COEFF, name="dwnsmp_mtd_3")

print("Before: length = %s" % len(voltage),"and", "frequency = %s Hz." % (FREQUENCY))
print("After: length = %s" % len(vltg_dwnsmp_mtd_1 or vltg_dwnsmp_mtd_2),"and", "frequency = %s Hz." % (FREQUENCY / DOWNSAMPLING_COEFF))
print('Completed! Check the files "no_dwnsmp.png", "dwnsmp_mtd_1_coeff_{}.png", "dwnsmp_mtd_2_coeff_{}.png" and "dwnsmp_mtd_3_coeff_{}.png" to see the result.'.format(DOWNSAMPLING_COEFF, DOWNSAMPLING_COEFF, DOWNSAMPLING_COEFF))