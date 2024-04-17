import csv

class City:

    def __init__(self, name, state, population, mean_household_inc, area_water, area_land, latitude):
        self.name = name
        self.state = state
        self.population = population
        self.mean_household_inc = mean_household_inc
        self.area_water = area_water
        self.area_land = area_land
        self.latitude = latitude

def readCSV(file):
    with open(file, 'r') as csvFile:
        read = csv.reader(csvFile)  #turns the csv into an object that can be iterated
    for line in read: #each loop gets a line from the CSV as an array
        print(line[0])
        print(line[1])