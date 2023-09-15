import csv
import pandas as pd

def csvread():

    #with open("D:\Mine\python\SeleniumProjects\DemoFiles\democsv.csv", 'r') as csvread:
        #csvreadobj = csv.reader(csvread)

        #data reading row wise
        #for lines in csvreadobj:
        #   print(', '.join(lines))

    #data reading col wise
    data = pd.read_csv("D:\Mine\python\SeleniumProjects\DemoFiles\democsv.csv")
    #print(data[['Name', 'Branch', 'Year']])

    #read by iterating
    for key, value in data.iterrows():
        print(key, value)
        print("____________________________________")


if __name__ == "__main__":
    csvread()