import matplotlib.pyplot as plt
from datetime import datetime

def get_data():
    FILENAME = "НИАД_120s_80d_60bpm.txt"

    FREQUENCY = None
    OFFSET = None
    SCALE = None

    VALUES = []

    time_start = datetime.now()

    with open(FILENAME, mode="r", encoding="utf-8") as f:
        isValue = False

        for line in f:
            if isValue is True:
                value = line.strip()
                if value != "":
                    try:
                        value = int(value)
                    except: 
                        continue
                    VALUES.append(value)
                continue 

            if line.find("RawPress") >= 0 and len(line.strip()) == len("RawPress"):
                isValue = True
                continue 
            
            if FREQUENCY is None:
                frq_s = line.find("Гц")
                if frq_s > 0:
                    FREQUENCY = int(line[:frq_s].strip())
                    continue
            
            if OFFSET is None:
                ofs_s = line.find("offset =")
                if ofs_s == 0:
                    OFFSET = int(line[ofs_s + len("offset") :].replace("=", "").strip())
                    continue

            if SCALE is None:
                scl_s = line.find("scale =")
                if scl_s == 0:
                    SCALE = int(line[scl_s + len("scale") :].replace("=", "").strip())
                    continue

    if FREQUENCY is None:
        raise ValueError(
            'Не могу найти значение частоты в техстовом файле. Укажите это значение в первой строке файла, например: "163 Гц"'
        )
    if OFFSET is None:
        raise ValueError(
            'Не могу найти значение OFFSET в техстовом файле. Укажите это значение в первой строке файла, например: "offset = 26948"'
        )
    if SCALE is None:
        raise ValueError(
            'Не могу найти значение смещения в техстовом файле. Укажите это значение в первой строке файла, например: "scale = 5619"'
        )
    
    time_end = datetime.now()
    delta = time_end - time_start
    milliseconds = delta.total_seconds() * 1000
    print("Data loaded in {:.0f} ms".format(milliseconds))

    return {"FREQUENCY": FREQUENCY, "OFFSET": OFFSET, "SCALE": SCALE, "VALUES": VALUES}

def get_axes(data):
    x_arr = []
    y_arr = []

    y = 1 / data["FREQUENCY"]
    for value in data["VALUES"]:
        x = (value + data["OFFSET"]) / data["SCALE"]
        y += 1 / data["FREQUENCY"]
        
        x_arr.append(x)
        y_arr.append(y)

    return x_arr, y_arr

def draw(x_arr, y_arr):
    plt.figure()
    plt.plot(y_arr, x_arr)
    plt.xlabel("Время (с)")
    plt.ylabel("Давление (мм рт. ст.)")
    plt.grid(True)
    plt.savefig("graph.jpg", format = "jpg")


data = get_data()
x, y = get_axes(data)
# draw(x, y)

def process(x, y):
    Pmax = max(x)
    Pmax_index = x.index(Pmax)
    Pmax_y = y[Pmax_index]

    x_new = x[Pmax_index:]
    y_new =  y[Pmax_index:]

    print("Pmax_y", Pmax_y)
    a1_y_index = y_new.index(min(y_new, key = lambda val: abs(val - (Pmax_y +  1 / 3 * Pmax_y))))
    a2_y_index = y_new.index(min(y_new, key = lambda val: abs(val - (Pmax_y +  2 / 3 * Pmax_y))))
    A1 = x_new[a1_y_index]
    A2 = x_new[a2_y_index]

    print("Диастолическое давление:", A1)
    print("Систолическое давление", A2)

process(x, y)