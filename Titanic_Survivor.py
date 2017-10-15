# Titanic Survivor Prediction
# Source - Kaggle
import csv
csvfile=open("train.csv",'r')
reader=csv.DictReader(csvfile) # Reads content of csv into a dictionary file
header=reader.fieldnames # Reads the header row
print(header)

for row in reader:
    print row



#for row in reader:
#    print row
