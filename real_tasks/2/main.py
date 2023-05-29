import time

VOLT_COEFF = 0.153269
FREQUENCY = 250
PEAK_FREQUENCY_MAX = 300
DELAY = 1
CACHE_RESULTS = 60

PEAK_DELTA = 0.05


def find_peaks(v, t):
    v_peaks = []
    t_peaks = []

    t_min_diff = 60 / PEAK_FREQUENCY_MAX

    max_peak = max(v)
    upper = max_peak * (1 + PEAK_DELTA)
    lower = max_peak * (1 - PEAK_DELTA)

    for i, val in enumerate(v):
        if lower < val and upper > val:
            if len(v_peaks) == 0 or abs(t_peaks[-1] - t[i]) > t_min_diff:
                v_peaks.append(v[i])
                t_peaks.append(t[i])

    return [[v, t_peaks[i]] for i, v in enumerate(v_peaks)]

def time_diff(t_arr):
    t_diff = []
    for i, t in enumerate(t_arr):
        if i == 0:
            continue
        t_diff.append(t - t_arr[i - 1])
    return t_diff

with open("./rr.txt", "r") as f:
    get_voltage = lambda v : int(v) * VOLT_COEFF

    lines = f.readlines()
    length = len(lines) - 1

    j = 0
    k = 0
    t_diff_arr = []
    
    while j < length:
        time.sleep(DELAY)
        j_delta = FREQUENCY if length - j > FREQUENCY else length - j
        v = [get_voltage(l.strip())  for l in lines[j : j + j_delta]]
        t = [i / FREQUENCY for (i, _) in enumerate(v)]

        peaks = find_peaks(v, t)
        peaks_t_diff = time_diff([p[1] for p in peaks])

        if (k < CACHE_RESULTS):
            t_diff_arr += peaks_t_diff
        else:
            t_diff_arr = t_diff_arr[len(peaks_t_diff):]
            t_diff_arr += peaks_t_diff

        if (k == 0):
            k += 1
            continue

        t_average = (sum(t_diff_arr) / len(t_diff_arr)) if len(t_diff_arr) > 0 else 0

        print("Average R-R interval: {} ".format("%.3f" % t_average), "|", "{} seconds in processing".format(k))
        k += 1
        j += FREQUENCY

print("Already processed")