
# Finds the peaks
def peaks(num):
    # Keeps a list of the peaks
    peaks = []
    # needs to check if the number before and after are less than it
    for i in range(len(num) - 1):
        if num[i] > num[i - 1] and num[i] > num[i + 1]:
            peaks.append(i)
    return peaks
            
# Finds the valleys 
def valleys(num):
    # Keeps a list of the peaks
    valleys = []

    # needs to check if the number before and after are more than it
    for i in range(len(num) - 1):
        if num[i - 1] == num[-1]:
            continue
        elif num[i] < num[i - 1] and num[i] < num[i + 1]:
            valleys.append(i)
    return valleys

# Finds the peaks and valleys
def peaks_and_valleys(peaks, valleys):
   pv = peaks + valleys
   pv_sorted = sorted(pv)
   return pv_sorted
        
data = []

print('You will be entering a total of 20 digits')

for i in range(21):
    user_input = input(f'Enter digit number {i}: ')
    data.append(user_input)

peaks = peaks(data)
valleys = valleys(data)
p_and_v = peaks_and_valleys(peaks, valleys)

print(f'The peaks are at {peaks}')
print(f'The valleys are at {valleys}')
print(f'The peaks and valleys are: {p_and_v} ')

