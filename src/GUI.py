from flask import Flask
import folium
import os
from AdjacencyList import AdjacencyListGraph
from Matrix import MatrixGraph
from src.CityData import City

#Code below is referenced from Folium's Github documentation/user guide and Flask's website/documentation

app = Flask(__name__) #creates application instance

#Function to add a market at a specific latitude and longitude (pass in an array of the cities similiar cities)
#References guide on OS module from GeeksforGeeks
def addTop5Markers(map, cities):
    currentDir = os.path.dirname(__file__)
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
    matrix = False
    retrieved = False
    while True:
        print("Select which graph implementation to test from the options below:")
        print("1. Matrix Representation")
        print("2. Adjacency List Representation")
        selection = input()
        print()

        if(selection == '1'):
            matrix = True
            return matrix

        elif(selection == '2'):
            return matrix

        else:
            print("Invalid input: Please Try Again")

def functionSelection():

    while True:
        print("Insert the name of the city you want to compare:")
        cityName = input()
        print()
        print("Select an operation from below:")
        break

@app.route('/')

def output():
    return map()


#current selection method, if we have time we can make something fancier that isn't in the command line
if __name__ == '__main__':

    app.run(port=8001)