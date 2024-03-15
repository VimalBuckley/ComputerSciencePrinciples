import os
import matplotlib.pyplot as plt

class Person:
    def __init__(self, name: str):
        self.name = name
        self.map = dict()
        years = range(1880, 2021)
        for year in years:
            self.map[year] = 0
            reader = open("yob" + str(year) + ".txt", "r")
            for line in reader:
                if (line.split(",")[1] == self.name):
                    self.addData(year, int(line.split(",")[2]))
            reader.close()
    def getName(self):
        return self.name
    def addData(self, year:int, count:int):
        self.map[year] += count
    def getTotal(self):
        count = 0
        for year in self.map:
            count += self.map.get(year)
        return count
    def getCount(self, year:int):
        return self.map.get(year)
    def getData(self):
        return list(self.map.values())

os.chdir("NameCounting")
os.system("cls")
totalCount = 0
person = Person("M")
plt.plot(range(1880, 2021), person.getData(), "b-")
person = Person("F")
plt.plot(range(1880, 2021), person.getData(), "r-")
plt.title("Number of People Born in Each Year Since 1880\n Male (Blue) | Female (Red)")
plt.xlabel("Year")
plt.ylabel("Frequency")
plt.show()
