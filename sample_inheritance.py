class baseclass:
    def __init__(self):
        print("base init")

    def set_name(self,name):
        self.name=name
        print("base class set name")

    

class Subclass(baseclass):
    def __init__(self):
        super().__init__()
        print("Subclass init")

    def set_name(self,name):
        super().set_name(name)
        print("Subclass set name")

    def welcome(self):
        print("Welcome")
    
    def display_name(self):
        print("name :"+self.name)

y=Subclass()
y.welcome()
y.set_name("Adithyan")
y.display_name()