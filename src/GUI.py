from flask import Flask
import folium
from AdjacencyList import AdjacencyListGraph
from Matrix import MatrixGraph
from src.CityData import City

#Code below is referenced from Folium's Github documentation/user guide and Flask's website/documentation

app = Flask(__name__) #creates application instance

#Function to add a market at a specific latitude and longitude (pass in an array of the cities similiar cities)
def addMarkers(map, cities):
    for city in cities:
        folium.Marker(location=[city.latitude, city.longitude]).add_to(map)

#Function that creates an interactive map using Folium
def map():

    map = folium.Map(location=[30,-102], zoom_start=3) #creates map object that looks over the US
    return map._repr_html_()

@app.route('/')

def output():
    return map()

#current selection method, if we have time we can make something fancier that isn't in the command line
if __name__ == '__main__':

    print("Select 1 or 2:")
    print("1. Matrix Representation")
    print("2. Adjacency List Representation")
    selection = int(input())

    if selection == 1:
        app.run(port=8001)

    elif selection == 2:
        app.run(port=8001)
