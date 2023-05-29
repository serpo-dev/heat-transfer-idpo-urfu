import os
import time

import matplotlib.pyplot as plt

VOLT_COEFF = 0.153269
FREQUENCY = 250

DELAY = 1

def draw(num, v, t):
    plt.figure()
    plt.plot(t, v)
    plt.xlabel("Время (с)")
    plt.ylabel("мкВ")
    plt.grid(True)
    os.makedirs("graph", exist_ok=True)
    plt.savefig("graph/{}.jpg".format(num), format = "jpg")
    plt.close()

with open("./rr.txt", "r") as f:
    get_voltage = lambda v : int(v) * VOLT_COEFF
    
    lines = f.readlines()
    length = len(lines) - 1

    j = 0
    k = 0
    while j < length:
        j_delta = FREQUENCY if length - j > FREQUENCY else length - j
        v = [get_voltage(l.strip())  for l in lines[j : j + j_delta]]
        t = [i / FREQUENCY for (i, _) in enumerate(v)]

        draw(num=k, v=v, t=t)
        
        time.sleep(DELAY)
        print(k, "seconds in processing")
        k += 1
        j += FREQUENCY

print("Already processed")