
class AdjacencyListGraph:

    def __init__(self):
        self.adjacencyList = {}
        self.simThreshold = 0
        self.numCities = 0

    #adds edge between city 1 and 2
    def insertEdge(self, city1, city2):
        simScore = self.calculateSimilarity(city1,city2)

        if(simScore > self.simThreshold): #if the similarity between the two has substance, add an edge

            if city1.name in self.adjacencyList: #if city1 is in the dict, append city2 to its array of neighbors
                self.adjacencyList[city1.name].append((city2, simScore))
            else:
                self.adjacencyList[city1.name] = [(city2, simScore)] #initialize city1 as a key, array containing city2 as its value
                self.numCities += 1

            if city2.name in self.adjacencyList:
                self.adjacencyList[city2.name].append((city1, simScore))
            else:
                self.adjacencyList[city2.name] = [(city1, simScore)]
                self.numCities += 1
        else:
            return

    #array of city's neighbors (tuple of object and simscore)
    def getAdjacent(self, city):
        neighbors = []
        for cities in self.adjacencyList[city.name]:
            neighbors.append(cities)
        return neighbors

    #similarity of two cities (have to determine how to calculate)
    def calculateSimilarity(self, city1, city2):
        simScore = 1
        return simScore

    #returns an array of the top 5 most similiar cities (as tuple of object and simscore)
    def topFive(self, city):
        self.adjacencyList[city.name].sort(key=lambda x: x[1], reverse=True) #sorts by similarity, based on second val of tuple
        five = []
        for i in range(len(self.adjacencyList[city.name])): #avoids out of range if city has less than 5 similiar cities
            five.append(self.adjacencyList[city.name][i])
            if i == 5:
                return 5
        return five
