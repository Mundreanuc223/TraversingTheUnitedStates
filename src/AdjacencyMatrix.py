
class AdjacencyMatrixGraph:

    def __init__(self, numCities):
        self.numCities = numCities
        self.simThreshold = 0
        self.matrix = [[0]*numCities for _ in range(numCities)] # 2d matrix, size being numCities * numcCities, initialized to 0s
        self.cityIndex = {}  # dictionary that maps each city to its index in the matrix
        self.indexToCity = {}  # dictionary that maps each index to its city
        self.cityToObject = {}  # dictionary that maps each city name + state appended to its object

    def addCity(self, city):
        index = len(self.cityIndex)
        self.cityIndex[city.id] = index  # maps city to the next open index in the matrix
        self.indexToCity[index] = city  # maps index to city object

    def getCity(self, city, state):
        key = (city + state).lower()
        if key not in self.cityToObject:
            return False
        else:
            return self.cityToObject[key]

    def insertEdge(self, city1, city2):

        if city1.id not in self.cityIndex:  # creates city's index if it isn't in the graph yet
            self.addCity(city1)
        if city2.id not in self.cityIndex:
            self.addCity(city2)

        simScore = self.calculateSimilarity(city1, city2)

        if simScore > self.simThreshold:
            city1Index = self.cityIndex[city1.id]
            city2Index = self.cityIndex[city2.id]
            self.matrix[city1Index][city2Index] = simScore
            self.matrix[city2Index][city1Index] = simScore

    # array of city's neighbors (tuple of object and simscore)
    def getAdjacentSim(self, city):
        neighbors = []
        index = self.cityIndex[city.id]
        for i in range(self.numCities):
            if self.matrix[index][i] > 0:
                neighbors.append((self.indexToCity[i], self.matrix[index][i]))
        return neighbors

    def getAdjacent(self, city):
        neighbors = []
        index = self.cityIndex[city.id]
        for i in range(self.numCities):
            if self.matrix[index][i] > 0:
                neighbors.append(self.indexToCity[i])
        return neighbors

    # scales values and finds the difference between them
    def calculateDifference(self, city1Val, city2Val, maxVal):
        x = city1Val / maxVal
        y = city2Val / maxVal
        return abs(x - y)

    # calculates similarity using root mean squared error (RMSE)
    def calculateSimilarity(self, city1, city2):
        maxPop = 18908608
        maxDensity = 28653.9
        maxMedianAge = 76.4
        maxMalePercent = 84.3
        maxFemalePercent = 65.4
        maxMarriedPercent = 86
        maxMedianIncome = 250001
        maxIncomeOverSix = 93.1
        maxHomeOwnership = 100
        maxHomeValue = 2000001
        maxMedianRent = 3501
        maxEducationPercent = 96.9
        maxLaborPercent = 94.9
        maxUnemploymentPercent = 34.2
        maxWhitePercent = 100
        maxBlackPercent = 99.1
        maxAsianPercent = 70.2
        maxNativePercent = 97.8
        maxPacificPercent = 54.6
        maxOtherPercent = 77.1

        numComparisons = 20

        differences = []

        differences.append(self.calculateDifference(city1.population, city2.population, maxPop))
        differences.append(self.calculateDifference(city1.density, city2.density, maxDensity))
        differences.append(self.calculateDifference(city1.medianAge, city2.medianAge, maxMedianAge))
        differences.append(self.calculateDifference(city1.malePercent, city2.malePercent, maxMalePercent))
        differences.append(self.calculateDifference(city1.femalePercent, city2.femalePercent, maxFemalePercent))
        differences.append(self.calculateDifference(city1.marriedPercent, city2.marriedPercent, maxMarriedPercent))
        differences.append(self.calculateDifference(city1.medianIncome, city2.medianIncome, maxMedianIncome))
        differences.append(self.calculateDifference(city1.incomeOverSix, city2.incomeOverSix, maxIncomeOverSix))
        differences.append(self.calculateDifference(city1.homeOwnership, city2.homeOwnership, maxHomeOwnership))
        differences.append(self.calculateDifference(city1.homeValue, city2.homeValue, maxHomeValue))
        differences.append(self.calculateDifference(city1.medianRent, city2.medianRent, maxMedianRent))
        differences.append(self.calculateDifference(city1.educationPercent, city2.educationPercent, maxEducationPercent))
        differences.append(self.calculateDifference(city1.laborPercent, city2.laborPercent, maxLaborPercent))
        differences.append(self.calculateDifference(city1.unemploymentPercent, city2.unemploymentPercent, maxUnemploymentPercent))
        differences.append(self.calculateDifference(city1.whitePercent, city2.whitePercent, maxWhitePercent))
        differences.append(self.calculateDifference(city1.blackPercent, city2.blackPercent, maxBlackPercent))
        differences.append(self.calculateDifference(city1.asianPercent, city2.asianPercent, maxAsianPercent))
        differences.append(self.calculateDifference(city1.nativePercent, city2.nativePercent, maxNativePercent))
        differences.append(self.calculateDifference(city1.pacificPercent, city2.pacificPercent, maxPacificPercent))
        differences.append(self.calculateDifference(city1.otherPercent, city2.otherPercent, maxOtherPercent))

        sum = 0
        for diff in differences:
            sum += diff**2
        simScore = 1 - ((sum/numComparisons)**0.5)

        return float("{:.4f}".format(simScore))

    # returns top 5 most similiar cities (as tuple of objects and simscore)
    def topFive(self, city):
        temp = self.getAdjacentSim(city)
        temp.sort(key=lambda x: x[1], reverse=True)
        five = []
        for idx, city in enumerate(temp):
            five.append(city[0])
            if idx == 4:
                return five
