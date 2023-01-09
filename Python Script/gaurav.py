import csv   #csv library

temp1=[]  #temp list
temp2=[]
with open("./input.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    temp1.append(row[0].split(".",maxsplit=3))
  for x in temp1:
      temp2.append(x[1]+"."+x[2])

final = {i:temp2.count(i) for i in temp2}    

#print(final)
print("Region, Environment, Count")
for key, value in final.items():
    d=key.split(".")
    print(d[0]+","+d[1]+","+str(value))
    

      