from PIL import Image, ImageTk
import tkinter

image=Image.open("in1.png").convert("RGB")
pix=image.load()
w,h=image.size
for y in range(h):
	for x in range(w):
		r,g,b=pix[x,y]
		r,g,b=255-r,b,g
		pix[x,y]=(r,g,b)
image.save("output1.png","PNG")


image=Image.open("in2.png").convert("RGB")
pix=image.load()
w,h=image.size
for y in range(h):
	for x in range(w):
		r,g,b=pix[x,y]
		r,g,b=255-b,g,r*2
		pix[x,y]=(r,g,b)
image.save("output2.png","PNG")

image=Image.open("in3.png").convert("RGB")
pix=image.load()
w,h=image.size
for y in range(h):
	for x in range(w):
		r,g,b=pix[x,y]
		r,g,b=g,255-b,255-r
		pix[x,y]=(r,g,b)
image.save("output3.png","PNG")

image=Image.open("in4.png").convert("RGB")
pix=image.load()
w,h=image.size
for y in range(h):
	for x in range(w):
		r,g,b=pix[x,y]
		r,g,b=255-g,b,255-r
		pix[x,y]=(r,g,b)
image.save("output4.png","PNG")

image=Image.open("in5.png").convert("RGB")
pix=image.load()
w,h=image.size
for y in range(h):
	for x in range(w):
		r,g,b=pix[x,y]
		if r*2>255: r=(255-r)*2
		else: r*=2
		if g*2>255: g=(255-g)*2
		else: g*=2
		if b*2>255: b=(255-b)*2
		else: b*=2
		pix[x,y]=(r,g,b)
image.save("output5.png","PNG")
