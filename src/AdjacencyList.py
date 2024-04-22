
class AdjacencyListGraph:

    def __init__(self):
        self.adjacencyList = {}
        self.simThreshold = 0.75
        self.numCities = 0
        self.cityToObject = {} #dictionary that maps each city name + state appended to its object

    #adds edge between city 1 and 2
    def insertEdge(self, city1, city2):

        simScore = self.calculateSimilarity(city1,city2) #threshold to reduce graph density

        if(simScore > self.simThreshold): #if the similarity between the two has substance, add an edge

            if city1.id in self.adjacencyList: #if city1 is in the dict, append city2 to its array of neighbors
                self.adjacencyList[city1.id].append((city2, simScore))
            else:
                self.adjacencyList[city1.id] = [(city2, simScore)] #initialize city1 as a key, array containing city2 as its value
                self.numCities += 1

        else:
            return

    #array of city's neighbors (tuple of object and simscore)
    def getAdjacent(self, city):
        neighbors = []
        if city.id in self.adjacencyList:
            for neighborTuple in self.adjacencyList[city.id]:
                if neighborTuple[1] > self.simThreshold:
                    neighbors.append(neighborTuple[0])  # Append the city object from the tuple
        return neighbors

    def getCity(self, city, state):
        key = (city + state).lower()
        if key not in self.cityToObject:
            return False
        else:
            return self.cityToObject[key]

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
        differences.append(
            self.calculateDifference(city1.educationPercent, city2.educationPercent, maxEducationPercent))
        differences.append(self.calculateDifference(city1.laborPercent, city2.laborPercent, maxLaborPercent))
        differences.append(
            self.calculateDifference(city1.unemploymentPercent, city2.unemploymentPercent, maxUnemploymentPercent))
        differences.append(self.calculateDifference(city1.whitePercent, city2.whitePercent, maxWhitePercent))
        differences.append(self.calculateDifference(city1.blackPercent, city2.blackPercent, maxBlackPercent))
        differences.append(self.calculateDifference(city1.asianPercent, city2.asianPercent, maxAsianPercent))
        differences.append(self.calculateDifference(city1.nativePercent, city2.nativePercent, maxNativePercent))
        differences.append(self.calculateDifference(city1.pacificPercent, city2.pacificPercent, maxPacificPercent))
        differences.append(self.calculateDifference(city1.otherPercent, city2.otherPercent, maxOtherPercent))

        sum = 0
        for diff in differences:
            sum += diff ** 2
        simScore = 1 - ((sum / numComparisons) ** 0.5)

        return float("{:.4f}".format(simScore))

    #returns an array of the top 5 most similiar cities (as tuple of object and simscore)
    def topFive(self, city):
        self.adjacencyList[city.id].sort(key=lambda x: (x[1], x[0].population), reverse=True) #sorts by similarity, based on second val of tuple
        five = []
        i = 0
        for city in self.adjacencyList[city.id]: #avoids out of range if city has less than 5 similiar cities
            five.append(city[0])
            i += 1
            if i == 5:
                return five

    #returns an array of the top 5 least similar cities (as tuple of object and simscore)
    def bottomFive(self, city):
        self.adjacencyList[city.id].sort(key=lambda x: (x[1], x[0].population), reverse=False) #sorts by similarity, based on second val of tuple
        five = []
        i = 0
        for city in self.adjacencyList[city.id]: #avoids out of range if city has less than 5 similiar cities
            five.append(city[0])
            i += 1
            if i == 5:
                return five

