

class AdjacencyListGraph:

    def __init__(self):
        self.adjacencyList = {}
        self.simThreshold = 0

    #adds edge between city 1 and 2
    def insertEdge(self, city1, city2):

        simScore = self.calculateSimilarity(city1,city2)
        if(simScore > self.simThreshold): #if the similarity between the two has substance, add an edge

            if city1.name in self.adjacencyList: #if city1 is in the dict, append city2 to its array of neighbors
                self.adjacencyList[city1.name].append((city2, simScore))
            else:
                self.adjacencyList[city1.name] = [(city2, simScore)] #initialize city1 as a key, array containing city2 as its value

            if city2.name in self.adjacencyList:
                self.adjacencyList[city2.name].append((city1, simScore))
            else:
                self.adjacencyList[city2.name] = [(city1, simScore)]

        else:
            return

    #array of city's neighbors
    def getAdjacent(self, city):
        neighbors = []
        for cities in self.adjacencyList[city.name]:
            neighbors.append(cities[0]) #extracts the city objects from the tuples
        return neighbors

    #similarity of two cities (have to determine how to calculate)
    def calculateSimilarity(self, city1, city2):
        simScore = 1
        return simScore

    #returns an array of the top 5 most similiar cities and sorts the cities neighbors by similarity
    def topFive(self, city):
        self.adjacencyList[city].sort(key=lambda x: x[1], reverse=True) #sorts the edges based on similarity, most similiar first
        five = []

        for i in range(5):
            five.append(self.adjacencyList[city][i])

        return five