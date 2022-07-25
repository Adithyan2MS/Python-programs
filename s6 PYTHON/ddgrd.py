

from breezypythongui import EasyFrame
class LabelDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="adda",width=300,height=400,background="black",resizable="false")
        self.addLabel(text="hdhdh",row=0,column=0,sticky="NSEW")
        self.addLabel(text="hdhdh",row=0,column=1,sticky="NSEW")
        self.addLabel(text="hdhdh",row=1,column=0,columnspan=2,sticky="NSEW")
        self.setSize(500,500)
        self.setBackground("red")
        self.setTitle("monnneee")

def main():
    LabelDemo().mainloop()

if __name__=="__main__":
    main()
