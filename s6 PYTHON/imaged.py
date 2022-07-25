from sympy import O
from images import Image
i=Image(100,100)
blackPixel=(0,0,0)
whitePixel=(255,255,255)
for y in range(i.getHeight()):
    for x in range(i.getWidth()):
        (r,g,b)=i.getPixel(x,y)
        avg=(r+g+b)/3
        if avg<128:
            i.setPixel(x,y,blackPixel)
        else:
            i.setPixel(x,y,whitePixel)

i.draw()