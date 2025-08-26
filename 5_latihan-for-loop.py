# Iteration over the list
myFavoriteFruit = ["Apple","Banana","Grape","Strawberry"]

no = 1
for d in myFavoriteFruit:
    print("{}. {}".format(no, d))
    no+=1 # equal to -> no = no+1
    

for en, d in enumerate(myFavoriteFruit):
    print("{}. {}".format(en+1, d))


# ==================================

# Iteration over the dict
myDictionary = {
    "nama": "Zauvik",
    "asal": "Solo"
}

#1 Using keys
for key in myDictionary.keys():
    print(myDictionary[key])


#2 Using values
for val in myDictionary.values():
    print("the value", val)
    
    
#3 Using members pair
for key, val in myDictionary.items():
    print(key + " : " + val)
    
    
    
# Mixed dictionary values type
d = {
    "nama": "Zauvik",
    "tahun_lahir": 2004
}
print("{} lahir pada tahun {}".format(d["nama"], str(d["tahun_lahir"])))