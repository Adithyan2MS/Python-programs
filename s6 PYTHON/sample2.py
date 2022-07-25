#breezypythongui image

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font

class ImageDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="image.demo",resizable="false")
        imageLabel=self.addLabel(text="",row=0,column=0,sticky="NSEW")
        textLabel=self.addLabel(text="This is image",row=1,column=0,sticky="NSEW")
        imageLabel2=self.addLabel(text="",row=2,column=0,sticky="NSEW")


        self.image=PhotoImage(file="image5.gif")
        imageLabel["image"]=self.image

        self.image2=PhotoImage(file="good.gif")
        imageLabel2["image"]=self.image2

        font=Font(family="Verdana",size=20,slant="italic")
        textLabel["font"]=font
        textLabel["foreground"]="red"

def main():
    ImageDemo().mainloop()

if __name__=="__main__":
    main()