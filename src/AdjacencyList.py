
class AdjacencyListGraph:

    def __init__(self):
        self.adjacencyList = {}
        self.simThreshold = 0
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

            if city2.id in self.adjacencyList:
                self.adjacencyList[city2.id].append((city1, simScore))
            else:
                self.adjacencyList[city2.id] = [(city1, simScore)]
                self.numCities += 1
        else:
            return

    #array of city's neighbors (tuple of object and simscore)
    def getAdjacent(self, city):
        neighbors = []
        if city.id in self.adjacencyList:
            for neighborTuple in self.adjacencyList[city.id]:
                neighbors.append(neighborTuple[0])  # Append the city object from the tuple
        return neighbors

    #similarity of two cities (have to determine how to calculate)
    def calculateSimilarity(self, city1, city2):
        simScore = 1
        return simScore

    #returns an array of the top 5 most similiar cities (as tuple of object and simscore)
    def topFive(self, city):
        self.adjacencyList[city.id].sort(key=lambda x: x[1], reverse=True) #sorts by similarity, based on second val of tuple
        five = []
        i = 0
        for idx, city in enumerate(self.adjacencyList[city.id]): #avoids out of range if city has less than 5 similiar cities
            five.append(city[0])
            if idx == 4:
                return five


