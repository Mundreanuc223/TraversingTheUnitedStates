import os
import pandas as pd
import openpyxl
from Matrix import MatrixGraph
from AdjacencyList import AdjacencyListGraph
class City:

    def __init__(self, name, state, latitude, longitude, population, density, id, medianAge, malePop, femalePop,
                 marriedPop, medianIncome, incomeOverSix, homeOwnership, homeValue, medianRent, education, laborPop, unemployment, whitePop, blackPop, asianPop, nativePop, pacificPop, otherPop):
        self.name = name
        self.state = state
        self.population = population
        self.density = density
        self.medianAge = medianAge
        self.malePop = malePop
        self.femalePop = femalePop
        self.marriedPop = marriedPop
        self.medianIncome = medianIncome
        self.incomeOverSix = incomeOverSix
        self.homeOwnership = homeOwnership
        self.homeValue = homeValue
        self.medianRent = medianRent
        self.education = education
        self.laborPop = laborPop
        self.unemployment = unemployment
        self.whitePop = whitePop
        self.blackPop = blackPop
        self.asianPop = asianPop
        self.nativePop = nativePop
        self.pacificPop = pacificPop
        self.otherPop = otherPop
        self.latitude = latitude
        self.longitude = longitude
        self.id = id

def readAdj():

    graph = AdjacencyListGraph()
    cities = []
    currentPath = os.getcwd()
    filePath = os.path.join(currentPath, 'src', 'US_CityData.xlsx')

    file = pd.read_excel(filePath)
    i = 0

    for index, row in file.iterrows():
        newCity = City(
        name=row['city'],
        state=row['state_name'],
        latitude=row['lat'],
        longitude=row['lng'],
        population=row['population'],
        density=row['density'],
        id=row['id'],
        medianAge=row['age_median'],
        malePop=row['male'],
        femalePop=row['female'],
        marriedPop=row['married'],
        medianIncome=row['income_household_median'],
        incomeOverSix=row['income_household_six_figure'],
        homeOwnership=row['home_ownership'],
        homeValue=row['home_value'],
        medianRent=row['rent_median'],
        education=row['rent_median'],
        laborPop=row['labor_force_participation'],
        unemployment=row['unemployment_rate'],
        whitePop=row['race_white'],
        blackPop=row['race_black'],
        asianPop=row['race_asian'],
        nativePop=row['race_native'],
        pacificPop=row['race_pacific'],
        otherPop=row['race_pacific'])

        cities.append(newCity)
        i+= 1

        if i == 100:
            for city1 in cities:
               for city2 in cities:
                   if city1.id != city2.id:
                       graph.insertEdge(city1, city2)
            help = graph.getAdjacent(cities[0])
            for j in help:
                print(j[0].name)

def readMatrix():

    graph = AdjacencyListGraph()
    cities = []

    file = pd.read_excel('CityData.xlsx')

    for index, row in file.iterrows():
        newCity = City(
        name=row['city'],
        state=row['state_name'],
        latitude=row['lat'],
        longitude=row['lng'],
        population=row['population'],
        density=row['density'],
        incorporated=row['incorporated'],
        id=row['id'],
        medianAge=row['age_median'],
        malePop=row['male'],
        femalePop=row['female'],
        marriedPop=row['married'],
        familySize=row['family_size'],
        medianIncome=row['income_household_median'],
        incomeOverSix=row['income_household_six_figure'],
        homeOwnership=row['home_ownership'],
        homeValue=row['home_value'],
        medianRent=row['rent_median'],
        education=row['rent_median'],
        laborPop=row['labor_force_participation'],
        unemployment=row['unemployment_rate'],
        whitePop=row['race_white'],
        blackPop=row['race_black'],
        asianPop=row['race_asian'],
        nativePop=row['race_native'],
        pacificPop=row['race_pacific'],
        otherPop=row['race_pacific'])

        cities.append(newCity)











