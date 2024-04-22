from flask import Flask
import folium
import os
from AdjacencyList import AdjacencyListGraph
from AdjacencyMatrix import AdjacencyMatrixGraph
import CityData
import time

# Code below is referenced from Folium's Github documentation/user guide and Flask's website/documentation

app = Flask(__name__)  # creates application instance


# Function to add a market at a specific latitude and longitude (pass in an array of the cities similiar cities)
# References guide on OS module from GeeksforGeeks
def addTop5Markers(map, cities):
    icons = {1: os.path.join('resources', 'Icons', 'one.png'),
             2: os.path.join('resources', 'Icons', 'two.png'),
             3: os.path.join('resources', 'Icons', 'three.png'),
             4: os.path.join('resources', 'Icons', 'four.png'),
             5: os.path.join('resources', 'Icons', 'five.png')}

    for i, city in enumerate(cities, start=1):
        cityPopup = folium.Popup(city.name, auto_open=True)
        folium.Marker(location=[city.latitude, city.longitude], popup=cityPopup,
                      icon=folium.CustomIcon(icon_image=icons[i]), icon_size=(32, 32)).add_to(map)


# Function that creates an interactive map using Folium
def map():
    map = folium.Map(max_bounds=True, location=[30, -102], zoom_start=3)  # creates map object that looks over the US
    return map._repr_html_()

@app.route('/')
def output():
    return map()

def parseInput():

    while True:
        print("Select which graph implementation to test from the options below:")
        print("1. Adjacency Matrix Representation")
        print("2. Adjacency List Representation")
        selection = input()
        print()

        graph = -1
        if (selection == '1'):
            print("Loading...")
            print()
            startTime = time.time()
            graph = CityData.readMatrix()
            print("Matrix Graph Execution Time: ", time.time() - startTime, " seconds")
            print()
            break

        elif (selection == '2'):
            print("Loading...")
            print()
            startTime = time.time()
            graph = CityData.readAdj()
            print("Adjacency-List Graph Execution Time: ", time.time() - startTime, " seconds")
            print()
            break

        else:
            print("Invalid input: Please Try Again")

    while True:
        print("Insert the state where the city you want to compare is located:")
        stateName = input().lower()
        print()

        print("Insert the name of the city you want to compare:")
        cityName = input().lower()
        print()

        city = graph.getCity(cityName, stateName)
        if not city:
            print("This city is not in the graph. Try again:")
            print()
            continue

        else:
            key = graph.cityToObject[(cityName+stateName)]

        print("Select an operation from below:")
        print("1. Display city's adjacent vertices")
        print("2. Display the 5 cities most similar to your city")
        print("3. Display the 5 cities least similar to your city")
        selection = input()
        print()

        if(selection == '1'):
            startTime = time.time()
            neighbors = graph.getAdjacent(key)
            for city in neighbors:
                print(city.name, city.state, end='\n')
            print("Execution Time: ", time.time() - startTime, " seconds")
            print()

        elif(selection == '2'):
            startTime = time.time()
            neighbors = graph.topFive(key)
            for city in neighbors:
                print(city.name, city.state, end='\n')
            print("Execution Time: ", time.time() - startTime, " seconds")
            print()

            print("Select an option from below:")
            print("1. Visualize Data")
            print("2. Input a new city")
            selection = input()
            if selection == '1':
                app.run(port=8001)

            else:
                continue

        elif (selection == '3'):
            startTime = time.time()
            neighbors = graph.bottomFive(key)
            for city in neighbors:
                print(city.name, city.state, end='\n')
            print("Execution Time: ", time.time() - startTime, " seconds")
            print()

            print("Select an option from below:")
            print("1. Visualize Data")
            print("2. Input a new city")
            selection = input()
            if selection == '1':
                app.run(port=8001)

            else:
                continue

