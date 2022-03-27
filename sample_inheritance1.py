class First:
    def display(self):
        print("first")

class Second:
    def display(self):
        print("second")

class Third(First,Second):
    def display(self):
        print("Third")

x=Third()
#x.display_third()
x.display()
print(Third.mro())