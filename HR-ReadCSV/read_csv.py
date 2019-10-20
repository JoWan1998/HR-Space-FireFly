import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

#Importing Dataset
dataset = pd.read_csv('/home/port-sagp2705/Escritorio/Fireball_And_Bolide_Reports.csv')

#Missing Data
imr = SimpleImputer(missing_values=np.nan, strategy='median')
imr = imr.fit(dataset[['Velocity (km/s)']])
dataset['Velocity (km/s)'] = imr.transform(dataset[['Velocity (km/s)']]).ravel()
imr = imr.fit(dataset[['Velocity Components (km/s): vx']])
dataset['Velocity Components (km/s): vx'] = imr.transform(dataset[['Velocity Components (km/s): vx']]).ravel()
imr = imr.fit(dataset[['Velocity Components (km/s): vy']])
dataset['Velocity Components (km/s): vy'] = imr.transform(dataset[['Velocity Components (km/s): vy']]).ravel()
imr = imr.fit(dataset[['Velocity Components (km/s): vz']])
dataset['Velocity Components (km/s): vz'] = imr.transform(dataset[['Velocity Components (km/s): vz']]).ravel()
imr = imr.fit(dataset[['Altitude (km)']])
dataset['Altitude (km)'] = imr.transform(dataset[['Altitude (km)']]).ravel()
print("-----")
print(dataset)
dataset.to_csv('modificado.csv')