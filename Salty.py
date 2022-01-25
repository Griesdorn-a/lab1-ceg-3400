#NOTE RUNNING THIS CODE AT THIS TIME WILL CHANGE THE SALT CURRENTLY ASSIGNED TO EACH USER IF PRESALTED HASHBROWNS ALREADY EXISTS
#This is a quick and dirty program to salt any number of unique users using the same csv format as provided in the lab. 
#Code for working with the CSV files was taken from https://www.geeksforgeeks.org/working-csv-files-python/
#This code is for potential use in the future for further labs or for personal tweaking later. 



import csv
import string
import random

infilename = "quiz_data.csv"
outfilename = "presalted_hashbrowns.csv"


fields = []
rows = []

with open(infilename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

user = rows[0][0]
letters = string.ascii_letters
expiredSalt = []
salt = ''.join(random.choice(letters) for i in range(5))
expiredSalt.append(salt)

for row in rows:
    if row[0] == user:
        row[0] = salt + user
    else:
        user = row[0]
        while salt in expiredSalt:
            salt = ''.join(random.choice(letters) for i in range(5))
        expiredSalt.append(salt)    
        row[0] = salt + user

with open (outfilename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(fields)
    csvwriter.writerows(rows)