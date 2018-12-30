import csv
import matplotlib.pyplot as plt
import numpy as np
from itertools import islice
data=open('data.csv', 'r')
reader = csv.reader(data)
interest = {} #Creating a new dictionary
try:
    for row in islice(reader, 1, None): #Starts reading at the second row to avoid conflicts with the floats/strings
        if row[16] in interest:
            interest[row[16]][0] += float(row[5]) #make a sum of each interest rate related to a same purpose
            interest[row[16]][1] += 1 #counter
        else :
            interest[row[16]] = [float(row[5]), 1] #Begin a new sum of the interest rates for a purpose that is not listed yet as a key in the dictionary

    for keys in interest:
        interest[keys] = interest[keys][0]/float(interest[keys][1]) #calculate the average of the interest rates and replace the value in the dictionary for each purpose.
    cmap = plt.get_cmap('spectral')
    colors = cmap(np.linspace(0, 1, len(interest))) #create an array of values between 0 and 1 with the same space between the values to associate each color to a purpose.
    plt.bar(range(len(interest)), list(interest.values()), align='center', color=colors, linewidth=0.2)
    plt.xticks(range(len(interest)), list(interest.keys()))
    plt.xlabel('Purpose')
    plt.ylabel('Mean interest rates (%)')
finally:
    data.close()
