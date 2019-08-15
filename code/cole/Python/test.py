#test.py
list1 = [70, 85, 25, 90, 97]
list2 = [80, 96, 100, 94, 72]
list3 = [73, 85, 88, 89, 94]
list4 = [86, 94, 68, 68, 90]
masterList = []

for item in list1:
    masterList.append(item)

for item in list2:
    masterList.append(item)

for item in list3:
    masterList.append(item)

for item in list4:
    masterList.append(item)


masterList.sort()
masterList.reverse()
print(masterList[0])
