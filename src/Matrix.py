
class MatrixGraph:

    def __init__(self):
        self.matrix = [] #2d matrix, size being numCities * numcCities, initialized to 0s
        self.cityIndex = {} #dictionary that maps each city to its index in the matrix
        self.indexToCity = {} #dictionary that maps each index to its city
        self.numCities = 0

    def addCity(self, city):
        index = len(self.cityIndex)
        self.cityIndex[city.name] = index #maps city to the next open index in the matrix
        self.indexToCity[index] = city #maps index to city object

        self.matrix.append([0] * len(self.matrix))  # adds another row to the matrix

        for i in self.matrix: #adds another column in the matrix
            i.append(0)

    def insertEdge(self, city1, city2):

        if city1.name not in self.cityIndex: #creates city's index if it isn't in the graph yet
            self.addCity(city1)
        if city2.name not in self.cityIndex:
            self.addCity(city2)

        simScore = self.calculateSimilarity(city1, city2)
        city1Index = self.cityIndex[city1.name]
        city2Index = self.cityIndex[city2.name]
        self.matrix[city1Index][city2Index] = simScore
        self.matrix[city2Index][city1Index] = simScore

    def getAdjacent(self, city):
        neighbors = []
        cityIndex = self.cityIndex[city.name]
        for i in range(len(self.cityIndex)):
            if self.matrix[cityIndex][i] > 0:
                neighbors.append(self.indexToCity[i])
        return neighbors


    #same as similarity calc for adjacency list
    def calculateSimilarity(self, city1, city2):
        simScore = 1
        return simScore






