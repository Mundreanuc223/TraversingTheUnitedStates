<H1> Traversing The United States </h1>
This project compares the functionalities and efficiencies of the following two graph implementations: matrix represenation vs an adjacency-list representation .

## Instructions to Run the Code
1. Open this repository into an IDE compatible with Python
2. Install the following libraries/packages
  - Flask
  - Folium
  - Pandas
  - Openpyxl
3. Run the code from the Main file

## Outline of Functionalties
When you first run the program, you will be asked to select between the following two different graph implementations:
-  Adjacency Matrix
-  Adjacency List
The implementation chosen can have significant impacts on the programs runtime, which is why the execution time for each operation is displayed throughout the program.

Once the graph has been constructed (which requires some patience), the user is asked to input a city and the state the city is located in.
From here, the user can either display all of the selected city's neighboring vertices, or a a list of its top 5 most similiar cities.
The user can continue to input new cities and test these features until they have found the city they want to visualize. Once a city has been chosen to visualize, a Folium map will display on a local Flask server. This provides an interactive visual of the cities similiar neighbors and provides additional information on each city.



![gator_plane_1](https://github.com/Mundreanuc223/TraversingTheUnitedStates/assets/155108015/cc45ff16-9c58-4fb5-834b-e52dd9c10a4d)


