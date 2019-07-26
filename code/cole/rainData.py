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
    i = 0
    highestDay = {}
    for item in list:
        if item["Total"] > i:
            i = item["Total"]
            highestDay = item
    return highestDay


def yearlyAverage(list, year):
    yearlyData = []
    total = 0
    for item in list:
        if item["Year"] == year:
            yearlyData.append(item)
    for item in yearlyData:
        total += item["Total"]
    yearAvg = total/len(yearlyData)
    return yearAvg


dataList = loadData()
dataList = organizeData(dataList)
averageRain = averageCalc(dataList)
highest = highestCalc(dataList)

highestYearAvg = 0
highestYear = 0
i = 2000
while i < 2020:
    yearAvg = yearlyAverage(dataList, i)
    if yearAvg > highestYearAvg:
        highestYearAvg = yearAvg
        highestYear = i

    i += 1


print(f"The average daily rainfall is {averageRain} inches")
print(f"The highest daily rainfall was {highest['Total']} inches, on {highest['Month']}/{highest['Day']}/{highest['Year']}")
print(f"The year with the most rainfall was {highestYear} with a daily average of {highestYearAvg} inches")
