# task-4 (Task search & filtering by status)
d=[
      {"title": "Buy milk", "status": "pending"},
    {"title": "Call mom", "status": "done"},
    {"title": "Finish homework", "status": "pending"},

]
    

newdict = [ b for b in d  if b["status"]=="pending"]
print(newdict)


# Other method using for loop

l=[]

for i in d:
    if i["status"]=="pending":
        l.append(i)

print(l)        
