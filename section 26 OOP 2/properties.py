class User:
    def __init__(self,name,age):
        self.name = name
        self._age= age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,value):
        self._age = value

first_user= User("Subham", 10)
print(first_user.age)
first_user.age = 23
print(first_user.age)