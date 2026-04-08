sample_dict = { 
"name": "Kelly", 
"age": 25, 
"salary": 8000, 
"city": "New york"} 

keys = ["name", "salary"]

dict2={}

for i in keys:
    dict2[i]=sample_dict.get(i)

print(dict2)