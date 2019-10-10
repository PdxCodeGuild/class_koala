data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
values = [" " for x in range(len(data))]


def peaks(data):
    peak_list = []
    for x in range(1, len(data)-1):
        if data[x-1] < data[x] > data[x+1]:
            peak_list.append(x)
    return peak_list


def valleys(data):
    valley_list = []
    for x in range(1, len(data)-1):
        if data[x-1] > data[x] < data[x+1]:
            valley_list.append(x)
    return valley_list


def peaks_valleys(data):
    peak_valley_list = []
    for x in range(1, len(data)-1):
        if data[x-1] < data[x] > data[x+1]:
            peak_valley_list.append(x)
        elif data[x-1] > data[x] < data[x+1]:
            peak_valley_list.append(x)
    return peak_valley_list


def draw(data):
    peak_list = peaks(data)
    peak = 10
    while peak > 1:

        i = 0
        peak -= 1

        while i < len(data):

            if data[i] == peak:

                values[i] = "X"
            i += 1 
            peak_index = -1

        for x in peak_list:

            
            if peak == (data[peak_list[peak_index]]):
                for x in range(peak_list[peak_index], len(data)):
                    if values[x] == " ":
                        values[x] = "o"
            peak_index -= 1
        print("  ".join(values))
print(draw(data))






print(peaks(data))
print(valleys(data))
print(peaks_valleys(data))