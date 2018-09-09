class Indexes:
   def __init__(self):
       self.string=""
   def get(self):
       i = input("Enter the characters:")
       for index in range(len(i)):
           #checks the even indexes and print it
           if(index % 2 == 0):
               print(i[index], end="") 
obj = Indexes()
obj.get()
