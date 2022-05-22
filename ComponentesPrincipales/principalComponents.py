import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

#change pyplot font size
plt.rcParams['font.size'] = 20

#change figsize
plt.rcParams['figure.figsize'] = (20,10)

#loading data
dataset = pd.read_csv('europe.csv')
#print(dataset.shape)
#print(dataset.head())
#le sacamos el nombre de los paises
variable_names = dataset.iloc[:,1:].columns
#print(variable_names)
variables = dataset.iloc[:, 1:].values



#normalizamos los datos
standarized = StandardScaler().fit_transform(variables)

#print(np.std(standarized, axis=0))
#print(np.mean(standarized, axis=0))

pca = PCA()

components = pca.fit_transform(standarized)

plt.figure("biplot")
plt.scatter(components[:,0], components[:,1])
#plt.show()

print(components)

print(pca.explained_variance_ratio_)











