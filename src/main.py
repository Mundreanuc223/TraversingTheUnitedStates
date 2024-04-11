import time
from AdjacencyList import AdjacencyListGraph
from Matrix import MatrixGraph
from CityData import City

#main file that showcases some of the function/class implementations (can be replaced entirely)
if __name__ == '__main__':

    #start time for adjacency list method
    startTime1 = time.time()

    #testing creating city objects manually
    city1 = City("Gainesville", 15000)
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

    print("Adjacency List Excecution Time: ", time.time() - startTime1, " seconds", end='\n')

    #start time for matrix method
    startTime2 = time.time()

    print('\n')

    #creates a matrix graph
    sim2 = MatrixGraph()
    sim2.insertEdge(city1, city2)
    sim2.insertEdge(city1, city3)

    print(city1.name + "'s", "Neighbors:")
    arr2 = sim2.getAdjacent(city1)
    for city in arr2:
        print(city.name)



    print("Matrix Execution Time: ", time.time() - startTime2, " seconds")
