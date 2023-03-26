#Script for Exercise 7
import pandas as pd
import matplotlib.pyplot as plt
import scipy

dataframe = pd.read_csv("iris.csv")
x = dataframe.petal_length_cm
y = dataframe.sepal_length_cm
subsets = {}

def scatter_maker(x,y,species_name):
	'''
	This function creates the scatterplots.
	example file name:
	Iris_virginica_petal_v_sepal_length.png
	'''
	plt.figure()
	plt.scatter(x, y)
	plt.plot(color = "green")
	plt.xlabel("Petal length (cm)")
	plt.ylabel("Sepal length (cm)")
	plt.title("Petal length vd Sepal length")
	plt.savefig(f"{species_name}"+"_petal_v_sepal_length.png")

def liner_regression(x,y,species_name):
	'''
	Functinon does the linear regression and creates the linear regression image needed to complete the exercise.
	This function will also name the images like Iris_virginica_petal_v_sepal_length_regress.png.
	'''
	plt.figure()
	regression = scipy.stats.linregress(x,y)
	slope = regression.slope
	intercept = regression.intercept
	plt.scatter(x, y, label = 'Data')
	plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
	plt.xlabel("Petal length (cm)")
	plt.ylabel("Sepal length (cm)")
	plt.title("Petal length vs Sepal length (Regression)")
	plt.legend()
	plt.savefig(f"{species_name}"+"_petal_v_sepal_length_regress.png")

def spliting_dataframe():
	'''
	This function goes into the dataframe and creates subsets based on the species of Iris
	'''
#This group of code looks at the dataframe and creates a list of all the unique species in the dataframe.
	species_list = set(dataframe["species"])
	species_list = list(species_list)
	'''
	This next for loop looks at the species in the species_list created above
	and makes a subset of the data frame with any rows that contain that species
	and makes it into a dict so we can call on that subset later on.
	'''
	for species in species_list:
		#print(species)
		subset = dataframe[dataframe['species'] == species]
		subsets[f"{species.replace('subset_', '')}"] = subset
	#print(subsets)

def parsing_values():
	'''
	This is the main script that we use to create both images, this function will call all of the previous functions
	that were previously made: spliting_dataframe, linear_regression, and scatter_maker.
	'''
	spliting_dataframe()
	#This next for loop will take the species_names that are in the subsets dict we created previously
	#and we create our x and y variables we need in order to visualize the data.
	for species_name in subsets:
		subdf = subsets[species_name]
		x = subdf.petal_length_cm
		y = subdf.sepal_length_cm
		liner_regression(x,y,species_name)
		scatter_maker(x,y,species_name)
		#print(subdf
		#print("\n")

if __name__ == '__main__':
	parsing_values()
	print("Images created!")