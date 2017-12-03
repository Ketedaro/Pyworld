from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import csv

# Transforme les strings en float
def without_quote(my_list):
    verbose = False
    for i in range(0, len(my_list)):
        try:
            my_list[i] = float(my_list[i].strip('"').strip("'"))
        except:
            if verbose:
                print("vide")

    return my_list

# Création de la map
def trace_map():
    # Creation des listes
    list_countries = []
    list_population = []
    list_lat = []
    list_lon = []

    # Ouverture du fichier .csv
    with open('population.csv', mode='r', encoding='utf8') as my_file:
        all_file = csv.reader(my_file, delimiter = ';') # Creation d'une liste des lignes du fichier
        for colonne in all_file:
            list_countries.append(colonne[0]) # Recuperation de la liste des pays
            list_population.append(colonne[5]) # Recuperation de la liste des populations
            list_lat.append(colonne[3]) # Recuperation de la liste des latitudes
            list_lon.append(colonne[4]) # Recuperation de la liste des longitude

    # String to float
    without_quote(list_population)
    for i in range(0, len(list_population)):
        list_population[i] = list_population[i] / 1000000 # Améliore la visibilité sur la map

    # String to float
    list_lon = without_quote(list_lon)
    list_lat = without_quote(list_lat)

    # Trace la map avec le modèle robinson
    MY_MAP = Basemap(projection = 'robin', lon_0 = 0,resolution = 'c')
    # Couleur de fond
    MY_MAP.drawmapboundary(fill_color='#85A6D9')
    # Couleur des continents et frontières
    MY_MAP.fillcontinents(color='white',lake_color='#85A6D9')
    MY_MAP.drawcountries(color='black', linewidth=.5)

    # Associe les coordonnées des listes à celles de la map
    X_COORD, Y_COORD = MY_MAP(list_lon,list_lat)

    # Construction d'un tableau de taille des points affichés
    scale_populations = [p for p in list_population]

    # Création de la barre de gradient bleu vers rouge
    colormap = plt.cm.get_cmap('jet')

    # Scatter plot des populations par pays
    SCA = MY_MAP.scatter(
        X_COORD, # Longitudes
        Y_COORD, # Latitudes
        s = scale_populations, # Tailles
        c = scale_populations, # Couleurs
        marker = 'o', # Forme
        alpha = 0.5, # Transparence
        zorder = 2, # Ordre d'affichage
        cmap = colormap, # Couleur du gradient
        )

    # Affichage de la barre des populations
    plt.colorbar(SCA)

    # Met la figure en plein écran
    fig = plt.gcf()
    fig.canvas.set_window_title('Géolocalisation') # Changement du nom de la figure
    Size = fig.get_size_inches() # Récupèration de la taille par défaut de la figure
    fig.set_size_inches(Size[0] * 3, Size[1] * 2, forward=True) # Mise en plein écran

    # Changement du titre
    plt.title('Proportion de la population dans le monde (en million)')

    plt.show()
