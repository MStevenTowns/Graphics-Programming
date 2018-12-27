from PIL import Image, ImageTk
import tkinter
import math


def rotate(p,angle):
	x,y=p
	rad_ang=math.radians(angle)
	xp=x*math.cos(rad_ang)-y*math.sin(rad_ang)
	yp=x*math.sin(rad_ang)+y*math.cos(rad_ang)
	return xp,yp
	
	
color0=(255,255,255)    #White
color1=(63,72,204)    	#Blue
color2=(237,28,36)     	#Red
size=(384,256)
image=Image.new("RGB",size,color0)

for a in range(size[0]):
	for b in range(size[1]):
		if b<(size[1]/2): image.putpixel((a,b),color0)
		if b>(size[1]/2): image.putpixel((a,b),color2)
for c in range(127):
	for d in range(size[1]):
		image.putpixel((c,d),color1)
m=math.tan(math.radians(72))
h=50 #Height of star
xc=65
yc=size[1]//2
image.putpixel((xc,yc),color0)
for x in range(-h,h):
	for y in range(-h,h):
		for z in range(5):
			xp,yp=rotate((x,y),72*z)
			if yp>0 and yp<m*xp+h and yp<-m*xp+h:
				image.putpixel((x+xc,-y+yc),color0)

root = tkinter.Tk()  
# A root window for displaying objects

# Convert the Image object into a TkPhoto 
tkimage = ImageTk.PhotoImage(image)

tkinter.Label(root, image=tkimage).pack()
# Put it in the display window

root.mainloop()
