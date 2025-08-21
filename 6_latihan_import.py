import csv
import copy

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

print(type(myVehicle["vin"]))
print(type(myVehicle["zeroSixty"]))


myInventoryList = []

with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    for key, row in enumerate(csvReader):
        if(key == 0):
            print("skipping the line one bcs its a column")
        else:
            # print(d)
            currentVehicle = copy.deepcopy(myVehicle)
            currentVehicle['vin'] = row[0]
            currentVehicle['make'] = row[1]
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]
            myInventoryList.append(currentVehicle)
            
print(myInventoryList)
print(myInventoryList[0])
            