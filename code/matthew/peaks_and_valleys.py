# filename: peaks_and_valleys.py

# checks if the number at the current index position is greater than the numbers to the left and right positions; if so, appends to list
def peaks(data):
    peaks = []
    for i in range(1, len(data)-1): # avoids being out of range
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append(i)
    return peaks

# checks if the number at the current index position is less than the numbers to the left and right positions; if so, appends to list
def valleys(data):
    valleys = []
    for i in range(1, len(data)-1): # avoids being out of range
        if data[i] < data[i-1] and data[i] < data[i+1]:
            valleys.append(i)
    return valleys

# combines two lists into one list, then sorts in order of appearance
def peaks_and_valleys(peaks, valleys):
    peaks_and_valleys = peaks + valleys
    peaks_and_valleys.sort()
    return peaks_and_valleys

# input data
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# stores results of the functions into their respective variables
peaks = peaks(data)
valleys = valleys(data)
peaks_and_valleys = peaks_and_valleys(peaks, valleys)

# prints the results back to the user
print(peaks)
print(valleys)
print(peaks_and_valleys)
