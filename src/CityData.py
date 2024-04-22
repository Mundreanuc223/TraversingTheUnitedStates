import os
import pandas as pd
import openpyxl
from AdjacencyMatrix import AdjacencyMatrixGraph
from AdjacencyList import AdjacencyListGraph


class City:

    def __init__(self, name, state, latitude, longitude, population, density, id, medianAge, malePercent, femalePercent,
                 marriedPercent, medianIncome, incomeOverSix, homeOwnership, homeValue, medianRent, educationPercent, laborPercent, unemploymentPercent, whitePercent, blackPercent, asianPercent, nativePercent, pacificPercent, otherPercent):
        self.name = name
        self.state = state
        self.population = population
        self.density = density
        self.medianAge = medianAge
        self.malePercent = malePercent
        self.femalePercent = femalePercent
        self.marriedPercent = marriedPercent
        self.medianIncome = medianIncome
        self.incomeOverSix = incomeOverSix
        self.homeOwnership = homeOwnership
        self.homeValue = homeValue
        self.medianRent = medianRent
        self.educationPercent = educationPercent
        self.laborPercent = laborPercent
        self.unemploymentPercent = unemploymentPercent
        self.whitePercent = whitePercent
        self.blackPercent = blackPercent
        self.asianPercent = asianPercent
        self.nativePercent = nativePercent
        self.pacificPercent = pacificPercent
        self.otherPercent = otherPercent
        self.latitude = latitude
        self.longitude = longitude
        self.id = id

#read functions are referenced from Panda's documentation and Geeks for Geeks
def readAdj():

    cities = []
    currentPath = os.getcwd()
    filePath = os.path.join(currentPath, 'US_CityData.xlsx')
    file = pd.read_excel(filePath)
    graph = AdjacencyListGraph()

    cityComp = -1
    for index, row in file.iterrows(): #iterates through the excel file and creates a city object for each row
        newCity = City(
        name=row['city'],
        state=row['state_name'],
        latitude=row['lat'],
        longitude=row['lng'],
        population=row['population'],
        density=row['density'],
        id=row['id'],
        medianAge=row['age_median'],
        malePercent=row['male'],
        femalePercent=row['female'],
        marriedPercent=row['married'],
        medianIncome=row['income_household_median'],
        incomeOverSix=row['income_household_six_figure'],
        homeOwnership=row['home_ownership'],
        homeValue=row['home_value'],
        medianRent=row['rent_median'],
        educationPercent=row['rent_median'],
        laborPercent=row['labor_force_participation'],
        unemploymentPercent=row['unemployment_rate'],
        whitePercent=row['race_white'],
        blackPercent=row['race_black'],
        asianPercent=row['race_asian'],
        nativePercent=row['race_native'],
        pacificPercent=row['race_pacific'],
        otherPercent=row['race_other'])

        cities.append(newCity)
        key = (newCity.name+newCity.state).lower() #maps the city to its object
        graph.cityToObject[key] = newCity

    for city in cities: #inserts each city's edges
        for city2 in cities:
            if city.id != city2.id:
                graph.insertEdge(city, city2)

    return graph


def readMatrix():

    cities = []
    numCities = 0

    currentPath = os.getcwd()
    filePath = os.path.join(currentPath, 'US_CityData.xlsx')

    file = pd.read_excel(filePath)

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
        malePercent=row['male'],
        femalePercent=row['female'],
        marriedPercent=row['married'],
        medianIncome=row['income_household_median'],
        incomeOverSix=row['income_household_six_figure'],
        homeOwnership=row['home_ownership'],
        homeValue=row['home_value'],
        medianRent=row['rent_median'],
        educationPercent=row['rent_median'],
        laborPercent=row['labor_force_participation'],
        unemploymentPercent=row['unemployment_rate'],
        whitePercent=row['race_white'],
        blackPercent=row['race_black'],
        asianPercent=row['race_asian'],
        nativePercent=row['race_native'],
        pacificPercent=row['race_pacific'],
        otherPercent=row['race_other'])

        cities.append(newCity)
        numCities += 1

    graph = AdjacencyMatrixGraph(numCities)

    for city1 in cities:
        key = (city1.name + city1.state).lower() #maps the city + state to its city object
        graph.cityToObject[key] = city1
        for city2 in cities:
            if city1 != city2:
                graph.insertEdge(city1, city2)

    return graph



