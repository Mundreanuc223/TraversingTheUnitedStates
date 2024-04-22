from flask import Flask
import folium
import os
from AdjacencyList import AdjacencyListGraph
from Matrix import MatrixGraph
import CityData
import time

#Code below is referenced from Folium's Github documentation/user guide and Flask's website/documentation

app = Flask(__name__) #creates application instance

#Function to add a market at a specific latitude and longitude (pass in an array of the cities similiar cities)
#References guide on OS module from GeeksforGeeks
def addTop5Markers(map, cities):
    icons = {1: os.path.join('..', 'resources', 'Icons', 'one.png'),
             2: os.path.join('..', 'resources', 'Icons', 'two.png'),
             3: os.path.join('..', 'resources', 'Icons', 'three.png'),
             4: os.path.join('..', 'resources', 'Icons', 'four.png'),
             5: os.path.join('..', 'resources', 'Icons', 'five.png')}

    for i, city in enumerate(cities, start=1):
        cityPopup = folium.Popup(city.name, auto_open=True)
        folium.Marker(location=[city.latitude, city.longitude], popup=cityPopup, icon=folium.CustomIcon(icon_image=icons[i]), icon_size=(32, 32)).add_to(map)

#Function that creates an interactive map using Folium
def map():
    map = folium.Map(max_bounds=True,location=[30,-102], zoom_start=3) #creates map object that looks over the US
    #folium.Marker(location=[30,-102], popup="Gainesville", icon=folium.CustomIcon(icon_image=os.path.join('..', 'resources', 'Icons', 'one.png'), icon_size=(32, 32))).add_to(map)
    return map._repr_html_()

#determines what graph type user wants
def graphSelection():

    while True:
        print("Insert the state where the city you want to compare is located:")
        stateName = input()
        print()

        print("Insert the name of the city you want to compare:")
        cityName = input()
        print()

        print("Select which graph implementation to test from the options below:")
        print("1. Matrix Representation")
        print("2. Adjacency List Representation")
        selection = input()

        if(selection == '1'):
            print("Loading...")
            startTime = time.time()
            CityData.readMatrix(cityName, stateName)
            print()
            print("Matrix Graph Execution Time: ", time.time() - startTime, " seconds")
            print()
            break

        elif (selection == '2'):
            print("Loading...")
            startTime = time.time()
            CityData.readAdj(cityName, stateName)
            print()
            print("Adjacency-List Graph Execution Time: ", time.time() - startTime, " seconds")
            print()
            break

        else:
            print("Invalid input: Please Try Again")

def parseInput():
    while True:
        print("Insert the state where the city you want to compare is located:")
        stateName = input().lower()
        print()

        print("Insert the name of the city you want to compare:")
        cityName = input().lower()
        print()

        print("Select which graph implementation to test from the options below:")
        print("1. Matrix Representation")
        print("2. Adjacency List Representation")
        selection = input()
        print()

        if (selection == '1'):
            print("Loading...")
            print()
            startTime = time.time()
            CityData.readMatrix()
            print("Matrix Graph Execution Time: ", time.time() - startTime, " seconds")
            print()
            break

        elif (selection == '2'):
            print("Loading...")
            print()
            startTime = time.time()
            CityData.readAdj(cityName, stateName)
            print("Adjacency-List Graph Execution Time: ", time.time() - startTime, " seconds")
            print()
            break

        else:
            print("Invalid input: Please Try Again")

@app.route('/')

def output():
    return map()


#current selection method, if we have time we can make something fancier that isn't in the command line
if __name__ == '__main__':

    app.run(port=8001)