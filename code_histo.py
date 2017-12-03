import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statistics import mean


verbose = False

class histo():
	def __init__(self): #creation de l'objet histogramme avec deux listes vides en attributs
		self.population = list()
		self.pays = list()

	def filtre_fichier(self): #methode qui remplis les listes de l'objet en partant du fichier .csv

		liste_population = [] # liste contenant la population de chaque pays
		liste_pays = [] # liste contenant les pays

		with open('population.csv', mode='r', encoding='utf8') as f:
			listfichier = f.readlines() #lecture du fichier et creation d'une liste des lignes
		liste_elem = list()
		d = dict()
		 # Pays = namedtuple('Pays', ['Population, Total']) #creation nametuple

		for i in listfichier:
			elem = i.split(';') #split des différentes informations
			liste_elem.append(elem) #creation d'une liste dans les lignes pour separer les données

		for elem in liste_elem:
			liste_pays.append(elem[0])
			liste_population.append(elem[5])

		for elem in liste_population:
			if (elem == '""'):
				liste_population.remove(elem)

		#On transforme tous les string en int
		for i in range(0,len(liste_population)):
			try:
				liste_population[i] = float(liste_population[i].strip('"').strip("'"))
				if verbose: print('info:', i,  liste_population[i], type(liste_population[i]))
			except:
				if verbose: print("vide")

		self.population=liste_population[:]

	def traceHisto(self): #creation de l'histogramme
		liste_nombrePopulation = self.population

		#print('\n')
		#print(liste_nombrePopulation)
		#print('\n')
		#print(max(liste_nombrePopulation))
		#print('\n')

		x = list(range(0, 1500000000, 20000000))

		#creation des titres des axes

		values = np.array(liste_nombrePopulation)
		nombre_de_population = np.array(x)

		n, bins, patches = plt.hist(liste_nombrePopulation, bins=x, color='green') #on trace l'histogramme

		cm = plt.cm.get_cmap('RdYlBu_r') #mapping de la couleur


		bin_centers = 0.5 * (bins[0:]) # scale values to interval [0:]
		col = bin_centers - min(bin_centers) #on définit la couleur sur une barre
		col /= max(col) #définition de la limite de la barre

		for c, p in zip(col, patches): #boucle pour parcourir toutes les barres
			plt.setp(p, 'facecolor', cm(c)) #setup le gradient de couleur

		plt.xlabel('Population')
		plt.ylabel('Nombres de pays')
		plt.title('Nombre de Pays en fonction des tranches du nombre de Population')
		plt.grid()

		fig = plt.gcf()
		fig.canvas.set_window_title('Histogramme') #On change le nom de la figure

		Size = fig.get_size_inches() # obtient la taille par défaut de la figure
		fig.set_size_inches(Size[0]*3, Size[1]*2, forward=True) # et met en plein écran la figure

		plt.show()

	def traceHistoZoom(self):
		liste_nombrePopulation = self.population
		#print('\n')
		#print(liste_nombrePopulation)
		#print('\n')
		#print(max(liste_nombrePopulation))
		#print('\n')
		x = list(range(0, 1500000000, 20000000))
		#creation des titres des axes
		values = np.array(liste_nombrePopulation)
		nombre_de_population = np.array(x)



		plt.ylim(0,25)
		n, bins, patches = plt.hist(liste_nombrePopulation, bins=x, color='green') #on trace l'histogramme

		cm = plt.cm.get_cmap('RdYlBu_r') #mapping de la couleur


		bin_centers = 0.5 * (bins[0:]) # scale values to interval [0:]
		col = bin_centers - min(bin_centers) #on définit la couleur sur une barre
		col /= max(col) #définition de la limite de la barre

		for c, p in zip(col, patches): #boucle pour parcourir toutes les barres
			plt.setp(p, 'facecolor', cm(c)) #setup le gradient de couleur

		plt.xlabel('Population')
		plt.ylabel('Nombres de pays')
		plt.title('Nombre de Pays en fonction des tranches du nombre de Population')
		plt.grid()

		fig = plt.gcf()
		fig.canvas.set_window_title('Histogramme Zoom') #On change le nom de la figure

		Size = fig.get_size_inches() # obtient la taille par défaut de la figure
		fig.set_size_inches(Size[0]*3, Size[1]*2, forward=True) # et met en plein écran la figure

		plt.show()



def main(): #permet d'executer le programme de creation de l'histogramme dans le bon ordre
	h = histo()
	h.filtre_fichier()
	print('\n')
	print("veuillez patientez svp... une fois que le premier histogramme est affiché, fermer celui-ci pour charger le deuxieme et patientez...")
	print('\n')
	print("Veuillez lire le rapport pour plus d'information.")
	print('\n')
	h.traceHisto()
	h.traceHistoZoom()

if __name__ == '__main__':
	main()
