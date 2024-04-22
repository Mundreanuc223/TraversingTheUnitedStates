from flask import Flask
from AdjacencyList import AdjacencyListGraph
from AdjacencyMatrix import AdjacencyMatrixGraph
import CityData
import GUI

app = Flask(__name__)  # creates application instance
mapUS = -1

@app.route('/')
def output():
    return mapUS

#main file that showcases some of the function/class implementations (can be replaced entirely)
if __name__ == '__main__':
    neighbors = GUI.parseInput()
    mapUS = GUI.createMap(neighbors)
    app.run(port=8001)
