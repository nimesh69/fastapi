my_vechile ={
    "model": "Ford",
    "year": 2021,
    "color": "blue",
    "make": "Ford",
    "engine": {
        "type": "V8",
    }
}
# for i in my_vechile.keys():
#     if i.startswith("engine"):
#         print(f"{i}: {my_vechile[i]['type']}")
#     else:   
#         print(f"{i}: {my_vechile[i]}")

for x,y in my_vechile.items():
    print(x,y)
vehicle2=my_vechile.copy()
vehicle2["number_of_tires"]=4
print(vehicle2)

vehicle2.pop("engine")
print(vehicle2)