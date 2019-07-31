# filename: peaks_and_valleys.py

def peaks(data):
    """checks if the number at the current index position is greater than the numbers to the left and right positions; if so, appends to list"""
    peaks = []
    for i in range(1, len(data)-1): # avoids being out of range
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append(i)
    return peaks

def valleys(data):
    """checks if the number at the current index position is less than the numbers to the left and right positions; if so, appends to list"""
    valleys = []
    for i in range(1, len(data)-1): # avoids being out of range
        if data[i] < data[i-1] and data[i] < data[i+1]:
            valleys.append(i)
    return valleys

def peaks_and_valleys(peaks, valleys):
    """combines two lists into one list, then sorts in order of appearance"""
    peaks_and_valleys = peaks + valleys
    peaks_and_valleys.sort()
    return peaks_and_valleys

def image(data):
    """creates a sketch of the hills. Starts from "the top" and cycles down the list until there's no more data rows. Each time through, adds an "X" if number is greater than or equal to the current row. If not, adds a blank space. After each time through, joins completed row with the overall list. At end, coverts overall list to a string with a new line between each row"""
    sketch = []
    peak = max(data)
    while peak > 0:
        row = []
        for n in data:
            if n >= peak:
                position = " X"
            else:
                position = "  "
            row.append(position)
        sketch.append(" ".join(row))
        peak -= 1
    completed_sketch = "\n".join(sketch)
    return completed_sketch

# input data
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# stores results of the functions into their respective variables
peaks = peaks(data)
valleys = valleys(data)
peaks_and_valleys = peaks_and_valleys(peaks, valleys)
image = image(data)

# prints the results back to the user
print(peaks)
print(valleys)
print(peaks_and_valleys)
print(image)
