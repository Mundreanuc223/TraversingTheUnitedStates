from flask import Flask
import GUI

app = Flask(__name__)  # creates application instance
mapUS = -1

@app.route('/')
def output():
    return mapUS

#main file that showcases some of the function/class implementations (can be replaced entirely)
if __name__ == '__main__':
    paramters = GUI.parseInput() #returns an array, index 0 determines if output is least/most similiar, index 1 are the cities
    mapUS = GUI.createMap(paramters[0], paramters[1])
    app.run(port=8001)
