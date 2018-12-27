from PIL import Image, ImageTk
import tkinter,math

def getImageFile():
    import os
    formats=[".bmp",".dib",".dcx",".gif",".im",
             ".jpg",".jpe",".jpeg",".pcd",".pcx",
             ".png",".pbm",".pgm",".ppm",".psd",
             ".tif",".tiff",".xbm",".xpm"]
    i=1
    files=[]
    for f in os.listdir("."):
        for ex in formats:
            if f[-len(ex):]==ex:
                print(str(i)+")",f)
                files.append(f)
                i+=1
                break
    if len(files)==0:
        print("No images are in this directory.")
        return ""
    print
    filenum=input("What file do you want?(Enter for blank): ")
    try: filenum=int(filenum)
    except: return ""
    while 1>filenum or filenum>len(files):
        print("That is an invalid entry.")
        filenum=input("What file do you want?(Enter for blank): ")
        try: filenum=int(filenum)
        except: return ""
    return files[filenum-1]
    
def display(image):
	root = tkinter.Tk()  
	# A root window for displaying objects
	# Convert the Image object into a TkPhoto 
	tkimage = ImageTk.PhotoImage(image)
	tkinter.Label(root, image=tkimage).pack()
	# Put it in the display window
	root.mainloop()
	
def distance(x1,x2,y1,y2):#distance between 2 points
		part1=(x1-x2)*(x1-x2)
		part2=(y1-y2)*(y1-y2)
		dist=math.sqrt(part1+part2)
		return dist
size1=int(input("width of image: "))
size2=int(input("height of image: "))
default_size=(size1,size2)

image=getImageFile()
try: image=Image.open(image).convert("RGB")
except: image=Image.new("RGB",default_size,(0,0,0))
pix=image.load() 
w,h=image.size
for y in range(h):
	for x in range(w):
		if (y<((((-4*h)/(w**2))*(x**2))+(((4*h)/w)*x))):
			pix[x,y]=(255,255,255)
display(image)

image=getImageFile()
try: image=Image.open(image).convert("RGB")
except: image=Image.new("RGB",default_size,(0,0,0))
pix=image.load()
w,h=image.size
radius=float(input("Give me a radius: "))
for y in range(h):
	for x in range(w):
		if (distance(w/2,x,h/2,y))<radius:
			pix[x,y]=(255,255,255)
display(image)		
	
image=getImageFile()
try: image=Image.open(image).convert("RGB")
except: image=Image.new("RGB",default_size,(0,0,0))
pix=image.load()
w,h=image.size
height=float(input("Give me a height: "))
width=float(input("Give me a width: "))
for y in range(h):
	for x in range(w):
		if x>w/2-width/2 and x<w/2+width/2:
			if y>h/2-height/2 and y<h/2+height/2:
				pix[x,y]=(255,255,255)
display(image)		
