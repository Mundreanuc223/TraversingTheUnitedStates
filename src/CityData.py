import csv

class City:

    def __init__(self, name, state, latitude, longitude, population, density, incorporated, id, medianAge, malePop, femalePop,
                 marriedPop, familySize, medianIncome, incomeOverSix, homeOwnership, homeValue, medianRent, education, laborPop, unemployment, whitePop, blackPop, asianPop, nativePop, pacificPop, otherPop):
        self.name = name
        self.state = state
        self.population = population
        self.density = density
        self.incorporated = incorporated
        self.medianAge = medianAge
        self.malePop = malePop
        self.femalePop = femalePop
        self.marriedPop = marriedPop
        self.familySize = familySize
        self.medianIncome = medianIncome
        self.incomeOverSix = incomeOverSix
        self.homeOwnership = homeOwnership
        self.homeValue = homeValue
        self.medianRent = medianRent
        self.education = education
        self.laborPop = laborPop
        self.unemployment = unemployment
        self.whitePop = whitePop
        self.blackPop = blackPop
        self.asianPop = asianPop
        self.nativePop = nativePop
        self.pacificPop = pacificPop
        self.otherPop = otherPop
        self.latitude = latitude
        self.longitude = longitude
        self.id = id

def readCSV(file):
    with open(file, 'r') as csvFile:
        read = csv.reader(csvFile)  #turns the csv into an object that can be iterated
    for line in read: #each loop gets a line from the CSV as an array
        print(line[0])
        print(line[1])