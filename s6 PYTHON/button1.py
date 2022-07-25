#breezypythongui

from breezypythongui import EasyFrame
class exmp(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="exmp",resizable="false")
        self.label=self.addLabel(text="hello daa",row=0,column=0,columnspan=2,sticky="NSEW")
        
        self.clrButton=self.addButton(text="clear",row=1,column=0,command=self.clear)
        self.rtrButton=self.addButton(text="restore",row=1,column=1,command=self.restore,state="disabled")
    def clear(self):
        self.label["text"]=""
        self.clrButton["state"]="disabled"
        self.rtrButton["state"]="normal"

    def restore(self):
        self.label["text"]="Hello daa"
        self.clrButton["state"]="normal"
        self.rtrButton["state"]="disabled"
        
def main():
    exmp().mainloop()

if __name__=="__main__":
    
    main()