class Task:
    def __init__(self,title, status="pending"):
        self.title= title
        self.status= status
    def showStatus(self):
          print(f"{self.title}- {self.status}")

class TaskManager:
     def __init__(self):
         self.tasks =[]
     def add_task(self,title):
         task = {"title": title, "status":"pending"}
         self.tasks.append(task)
         print(f"task - {title} added ✅")
         return self.tasks
     def view_tasks(self):
          if len(self.tasks)==0:
              print("No tasks added yet")
          else:
              print("All Tasks")
              for t in range(len(self.tasks)):
                  print(f"{t} - {self.tasks[t]}")
     def Marks_Status_Done(self, number):
         if 0 <= number < len(self.tasks):
             self.tasks[number]["status"] = "done✅"
             print(f" The task : {self.tasks[number]} is  marked as done")

ts = Task("Learning Python")
print(ts.showStatus())
tm = TaskManager()

print(tm.add_task("Practicing code" ))
print(tm.view_tasks())
print(tm.Marks_Status_Done(0))
