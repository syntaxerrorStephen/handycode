#playing around with firebase
#sets up the connection to the database

from firebase import firebase
firebase = firebase.FirebaseApplication('https://cookietest-a4f79.firebaseio.com', None)
import csv



#READING all data (keys and values (the full dictionary)) on the node called /moOOARsimData
print("\n Reading this node \n")

#reads the database at the node 
fireBDatas = firebase.get('/moOOARsimData/', None)

print(fireBDatas)




#Printing ALLLLLLLLL THE DATA from a firebase node
print("\n Printing out all values \n ")

# this is a dictionary (a python database datatype so we need to pull out values into a list)
for x in fireBDatas: # go through the dictionary of keys and values eg. Temp(key):53(value)
    
  print(x) # print out the key
  print(fireBDatas[x]) # print out just the value




#READING ALLLLLLLLL THE DATA from a firebase node and writing it to a CSV

print("\n Writing all values to a csv file \n ")

f= open("dataFromFirebase.csv", "w", newline="") #give your .csv file a name
wc=csv.writer(f)

for x in fireBDatas:                   # iterate through the whole node (dictionary)
    
    wc.writerow([fireBDatas[x]])       #writes values for each key to a row in the csv, then makes a new line

f.close()                             #close the file when done to prevent data loss




