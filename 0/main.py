import numpy as np
import csv
labels=[]
with open("wine_train_set.csv") as csv_file:
    train_data = csv.reader(csv_file, delimiter=',', quotechar='|')
    labels = train_data.__next__()
print(labels)
my_data = np.loadtxt('wine_train_set.csv', delimiter=',',skiprows=1)
print(my_data)


