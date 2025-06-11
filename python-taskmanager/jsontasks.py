# loading json data 

import json





with open("demo.json",'r') as f:
    students = json.load(f)
    data= students['students_data']
    print(data, type(data))
    print(" Students Name Data :")
    for l in data:
        print(f" {l['st_name']}")


# saving data into json

data = [
    {
        "prod_name": "Cooler",
        "price": 2000,
        "quantity": "5 pieces",
        "cat": "electric"
    },
    {
        "prod_name": "Mobile Phone",
        "price": 10000,
        "quantity": "10 pieces",
        "cat": "communication"
    },
    {
        "prod_name": "Double Bed",
        "price": 50000,
        "quantity": "40 pieces",
        "cat": "home furnishing"
    }
]
    


with open("data.json",'w') as t:
 t.write(json.dumps(data, indent=4))
print("Data saved to data.json successfully.")