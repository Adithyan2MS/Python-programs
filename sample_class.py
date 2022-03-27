class MySampleClass:
    year=2021
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

    
    def add_age(self):
        self.age=self.age+1
    def relocate(self,place):
        self.place=place
    def display(self):
        print("year :"+str(MySampleClass.year))
        print("name :"+self.name)
        print("Age :"+str(self.age))
        print("place :"+self.place)

    @classmethod
    def add_year(hai):
        hai.year=hai.year+1

    @staticmethod
    def display_welcome():
        print("welcome")

MySampleClass.display_welcome()
x=MySampleClass("Anjana",20,"kannamangalam")
y=MySampleClass("Adithyan",20,"kunnom")

x.display()
y.display()
print("----------")
MySampleClass.year=MySampleClass.year+1
x.add_age()
y.add_age()

x.display()
y.display()

print("----------")
MySampleClass.add_year()
x.add_age()
y.add_age()
x.relocate("Gujarat")
y.relocate("Chennai")

x.display()
y.display()
