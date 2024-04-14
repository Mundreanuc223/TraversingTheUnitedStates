import csv

class City:

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def readCSV(self, file):
        with open(file, 'r') as csvFile:
            read = csv.reader(csvFile)  #turns the csv into an object that can be iterated
        for line in read: #each loop gets a line from the CSV as an array
            print(line[0])
            print(line[1])