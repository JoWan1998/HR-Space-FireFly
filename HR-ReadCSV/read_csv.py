
import pandas
import impyute as impy
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
url = "/home/port-sagp2705/Escritorio/Fireball_And_Bolide_Reports.csv"
names = ['a','b','c','d','e','f','g','h','i','j']
dataset = pandas.read_csv(url, names=names)
#print(impy.mean(dataset))
print(dataset.head(20))
print(dataset.describe())
