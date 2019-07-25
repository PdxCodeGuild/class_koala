#rainData

import datetime
import matplotlib.pyplot as plt

def loadData():
    f = open("rainData.txt", "r")
    data = f.read()
    dataList = data.split("\n")

    f.close()
    return dataList

def organizeData(list):
    dates = []
    totals = []
    organizedData = []
    for x in list:
        x = x.split(" ")
        total = 0
        for item in x:
            if len(item)>8:
                dates.append(item)
            else:
                try:
                    item = int(item)
                    total += item
                except ValueError:
                    x.remove(item)
        totals.append((total/2)*.01)
    i = 0
    while i < len(dates) - 1:
        dailyData = {}
        date = datetime.datetime.strptime(dates[i], "%d-%b-%Y")
        dailyData.update({"Year": date.year})
        dailyData.update({"Month": date.month})
        dailyData.update({"Day": date.day})
        dailyData.update({"Total": totals[i]})
        organizedData.append(dailyData)
        i += 1
    return organizedData

def averageCalc(list):
    total = 0
    for x in list:
        total += x["Total"]
    average = total/len(list)
    return(average)

def highestCalc(list):
    totals = []
    for item in list:
        totals.append(item["Total"])
    totals.sort()
    totals.reverse()
    return(totals[0])



dataList = loadData()
dataList = organizeData(dataList)
averageRain = averageCalc(dataList)
highest = highestCalc(dataList)

print(averageRain)
print(highest)
