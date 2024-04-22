
class MatrixGraph:

    def __init__(self, numCities):
        self.numCities = numCities
        self.simThreshold = 0
        self.matrix = [[0]*numCities for _ in range(numCities)] # 2d matrix, size being numCities * numcCities, initialized to 0s
        self.cityIndex = {}  # dictionary that maps each city to its index in the matrix
        self.indexToCity = {}  # dictionary that maps each index to its city

    def addCity(self, city):
        index = len(self.cityIndex)
        self.cityIndex[city.id] = index  # maps city to the next open index in the matrix
        self.indexToCity[index] = city  # maps index to city object

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
    def getAdjacent(self, city):
        neighbors = []
        index = self.cityIndex[city.id]
        for i in range(self.numCities):
            if self.matrix[index][i] > 0:
                neighbors.append((self.indexToCity[i], self.matrix[index][i]))
        return neighbors

    # same as similarity calc for adjacency list
    def calculateSimilarity(self, city1, city2):
        simScore = 1
        return simScore

    # returns top 5 most similiar cities (as tuple of objects and simscore)
    def topFive(self, city):
        temp = self.getAdjacent(city)
        temp.sort(key=lambda x: x[1], reverse=True)
        five = []
        for i in range(5):
            five.append(temp[i])
        return five







