import time
from AdjacencyList import AdjacencyListGraph
from Matrix import MatrixGraph
from CityData import City


if __name__ == '__main__':

    startTime1 = time.time()

    #testing creating city objects manually
    city1 = City("Gainesville", 13000)
    city2 = City("Tampa", 30000)
    city3 = City("Orlando", 50000)

    #creates adjacency list graph
    sim1 = AdjacencyListGraph()
    sim1.insertEdge(city1, city2)
    sim1.insertEdge(city1, city3)

    #tests get adjacent
    arr1 = sim1.getAdjacent(city1)
    print(city1.name + "'s", "Neighbors:")
    for city in arr1:
        print(city.name)

    print("Adjacency List Excecution Time: ", time.time() - startTime1, " seconds")


    #creates a matrix graph
    startTime2 = time.time()
    sim2 = MatrixGraph()


    print("Matrix Execution Time: ", time.time() - startTime2, " seconds")
