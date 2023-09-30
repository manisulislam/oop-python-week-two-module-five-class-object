class Student:
     
    def __init__(self, name, currenct_class, id):
        self.name= name
        self.current_class= currenct_class
        self.id= id
    
    def __repr__(self)-> str:
        return f"student is {self.name} and class {self.current_class} id {self.id}"
    
anis= Student("anis", 13, 4125)

print(anis)