#task-3 (Parse task data into structured dicts)

data= "Buy milk, 13-06-25, Pending"

dataArr=data.split(",")
title=dataArr[0]
date=dataArr[1]
status=dataArr[2]


dataDict={"title": title, "date": date, "status":status}
print(dataDict)