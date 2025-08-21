# List: Mutable (the values can be modified)
# List digunakan untuk menyimpan nilai lebih dari 1 (multiple value)
myFavoriteFruit = ["Apple","Banana","Grape"]
print(type(myFavoriteFruit))
print(myFavoriteFruit) # Call all variable
print(myFavoriteFruit[0]) # Call spesific index (urutan)
print(myFavoriteFruit[0:2]) # Call within a range
print(myFavoriteFruit[-2:]) # Call last x values
# Update list value
myFavoriteFruit[0] = "Strawberry"
print(myFavoriteFruit)


# Tuple: Immutable (the values can't be modified)
myFavoriteFruit = ("Apple","Banana","Grape")
print(type(myFavoriteFruit))
print(myFavoriteFruit) # Call all variable
print(myFavoriteFruit[0]) # Call spesific index (urutan)
print(myFavoriteFruit[0:2]) # Call within a range
print(myFavoriteFruit[-2:]) # Call last x values
# Update tuple value-> Error: 'tuple' object does not support item assignment
# myFavoriteFruit[0] = "Strawberry"
# print(myFavoriteFruit)


# Dictionary: Mutable collection with custom index
# List yang bisa kita cutom indexnya, selanjutnya indeks ini kita sebut "key"
myDictionary = {
    "nama": "Zauvik",
    "asal": "Solo"
}
print(type(myDictionary))
print(myDictionary)
print(myDictionary['asal'])
print(myDictionary.keys()) # Call all available keys
print(myDictionary.values()) # Call all available values
myDictionary["nama"] = "Raihan"
print(myDictionary)


# Complex/compound collection untuk implementasi data 2 sumbu
# | brand                 | year  |
# ---------------------------------
# | Toyota Inova Zenix    | 2025  |
# | Tesla                 | 2024  |
myCar = [
    {
        "brand":"Toyota Inova Zenix",
        "year": 2025
    },
    {
        "brand": "Tesla",
        "year": 2024
    }
    ]

print(type(myCar)) # List
print(type(myCar[0])) # Dict
print(myCar[0]["brand"]) # Toyota Inova Zenix

# Usman's question
myCar = [
    ["Toyota Inova Zenix", 2025],
    ["Tesla", 2024]
    ]
print(myCar[0][1])