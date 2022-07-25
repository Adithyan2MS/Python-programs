from unittest import result
import math
from breezypythongui import EasyFrame



class exmp(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="exmp",resizable="false")
        self.addLabel(text="gross income",row=0,column=0,sticky="NSEW")
        self.gifield=self.addFloatField(value=0.0,row=0,column=1)
        self.addLabel(text="dependents",row=1,column=0,sticky="NSEW")
        self.dpfield=self.addFloatField(value=0.0,row=1,column=1,state="normal")
        self.button=self.addButton(text="compute",command=self.compute,row=2,column=0,columnspan=2,)
        self.addLabel(text="total tax",row=3,column=0,sticky="NSEW")
        self.taxfield=self.addFloatField(value=0.0,row=3,column=1)
    def compute(self):
        try:
            grossIncome=self.gifield.getNumber()
            dependents=self.dpfield.getNumber()
            tax=grossIncome/dependents
            self.taxfield.setNumber(tax)
        except ValueError:
            self.messageBox(title="ERROR",message="Input must be an integer >= 0")

        




        

def main():
    exmp().mainloop()

if __name__=="__main__":
    
    main()