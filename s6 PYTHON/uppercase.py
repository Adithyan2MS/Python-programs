from unittest import result
from breezypythongui import EasyFrame



class exmp(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="exmp",resizable="false")
        self.addLabel(text="enter text",row=0,column=0,sticky="NSEW")
        self.inputfield=self.addTextField(text="",row=0,column=1)
        self.addLabel(text="uppercase",row=1,column=0,sticky="NSEW")
        self.outputfield=self.addTextField(text="",row=1,column=1,state="readonly")
        self.button=self.addButton(text="convert",command=self.convert,row=2,column=0,columnspan=2,)
    def convert(self):
        ch=self.inputfield.getText()
        result=ch.upper()
        self.outputfield.setText(result)




        

def main():
    exmp().mainloop()

if __name__=="__main__":
    
    main()