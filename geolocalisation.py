from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import csv



def without_quote(my_list):
    verbose = False
    for i in range(0, len(my_list)):
        try:
            my_list[i] = float(my_list[i].strip('"').strip("'"))
        except:
            if verbose:
                print("vide")

    return my_list

def trace_map():
    # Creation des listes
    list_countries = []
    list_population = []

    # Ouverture du fichier des populations par pays .csv
    with open('populationbycountry.csv', mode='r', encoding='utf8') as population_file:
        all_file = csv.reader(population_file, delimiter = ',') # Creation d'une liste des lignes du fichier
        for colonne in all_file:
            list_countries.append(colonne[0]) # Recuperation de la liste des pays
            list_population.append(colonne[60]) # Recuperation de la liste des populations

    # Creation des listes
    list_lat = []
    list_lon = []

    # Ouverture du fichier des latitudes et longitudes par pays .csv
    with open('positionbycountry.csv', mode='r', encoding='utf8') as position_file:
        all_file = csv.reader(position_file, delimiter = ',') # Creation d'une liste des lignes du fichier
        for colonne in all_file:
            list_lat.append(colonne[4]) # Recuperation de la liste des latitudes
            list_lon.append(colonne[5]) # Recuperation de la liste des longitudes


    # On enleve les quotes
    list_lat = without_quote(list_lat)
    list_lon = without_quote(list_lon)
    list_population = without_quote(list_population)



    print(list_lat)

    # llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
    # are the lat/lon values of the lower left and upper right corners of the map.
    # lat_ts is the latitude of true scale.
    # resolution = 'c' means use crude resolution coastlines.
    MY_MAP = Basemap(projection='cyl', resolution=None,
            llcrnrlat=-90, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180, )
    MY_MAP.shadedrelief()

    MY_MAP.drawmapboundary(fill_color='aqua')
    plt.title("Proportion de la population par pays")


    #MIN_TEMP = min(TEMPS)
    # setup mercator map projection.
    #MY_MAP.bluemarble()
    #MY_MAP.drawcoastlines()
    #MY_MAP.drawmapboundary(fill_color='aqua')
    #MY_MAP.drawcountries()
    #MY_MAP.drawparallels(np.arange(40, 60, 5), labels=[1, 1, 0, 1])
    #MY_MAP.drawmeridians(np.arange(-5, 15, 5), labels=[1, 1, 0, 1])
    # Conversion des coordonnées géographiques en coordonnées graphiques
    #X_COORD, Y_COORD = MY_MAP(LONGS, LATS)
    # Get a color map
    #CMAP = plt.cm.get_cmap('Oranges')
    # Construction d'un tableau de taille des points affichés
    #SIZE = (np.array(TEMPS)-MIN_TEMP+1)*20
    # scatter plot des températures
    #SCA = MY_MAP.scatter(X_COORD, Y_COORD, s=SIZE, marker='o', c=TEMPS, cmap=CMAP)
    #plt.colorbar(SCA)
    plt.show()
    get_list()
