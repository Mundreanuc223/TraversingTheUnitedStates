
class MatrixGraph:

    def __init__(self):
        self.numCities = 100
        self.matrix = [[0] * self.numCities for i in range(self.numCities)] #2d matrix, size being numCities * numcCities, initialized to 0s
        self.cityIndex = {} #dictionary that maps each city to its index in the matrix



