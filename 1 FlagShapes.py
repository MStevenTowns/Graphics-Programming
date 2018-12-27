import numpy, math
from PIL import Image, ImageDraw

color0=(255,255,255)    #White
color1=(68,215,211)     #Blue
color2=(38,147,41)      #Green
color3=(237,28,36)      #Red
x=640
y=480

m=math.tan(math.radians(72))
print(m)

top=[(0,0),(x/2,y/2),(x,y/2),(x,0)]
bottom=[(0,y),(x,y),(x,y/2),(x/2,y/2)]
star=[(75,225),(110,225),(120,195),(130,225),(165,225),(135,245),(145,275),(120,255),(95,275),(105,245)]
#        left                top                 right               BR                 BL                           
image=Image.new("RGB",(x,y),color0)
draw=ImageDraw.Draw(image)


'''


'''
draw.polygon(top,color1)
draw.polygon(bottom,color2)
draw.polygon(star,color3)

image.show()
