import math
from breezypythongui import EasyFrame



class exmp(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="exmp",resizable="false")
        self.addLabel(text="enter number",row=0,column=0,sticky="NSEW")
        self.inputfield=self.addIntegerField(value=0,row=0,column=1)
        self.addLabel(text="uppercase",row=1,column=0,sticky="NSEW")
        self.outputfield=self.addFloatField(value=0.0,row=1,column=1,state="readonly")
        self.button=self.addButton(text="convert",command=self.convert,row=2,column=0,columnspan=2,)
    def convert(self):
        try:
            num=self.inputfield.getNumber()
            result=math.sqrt(num)
            self.outputfield.setNumber(result)
        except ValueError:
            self.messageBox(title="ERROR",message="Input must be an integer >= 0")

def main():
    exmp().mainloop()

if __name__=="__main__":
    
    main()