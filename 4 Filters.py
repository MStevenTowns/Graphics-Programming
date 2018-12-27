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

def greyscale(image):
	return dessaturate(image,1)
def b_w(image_old,a=128):
	image=image_old.copy()
	pix=image.load()
	w,h=image.size
	for y in range(h):
		for x in range(w):
			r,g,b=pix[x,y]
			if (.2*r+.7*g+.1*b)<=(a):
				r=0
				g=0
				b=0
			else:
				r=255
				g=255
				b=255
			pix[x,y]=r,g,b
	return image
	
#% from 0-1
def dessaturate(image_old,per):
	image=image_old.copy()
	pix=image.load()
	w,h=image.size
	for y in range(h):
		for x in range(w):
			r,g,b=pix[x,y]
			grey=(.2*r+.7*g+.1*b)
			newr=int((r*(1-per))+(grey*(per)))
			newg=int((g*(1-per))+(grey*(per)))
			newb=int((b*(1-per))+(grey*(per)))
			pix[x,y]=newr,newg,newb
	return image

def lighten(image,per):
	return tint(image,(255,255,255),per)

def darken(image,per):
	return tint(image,(0,0,0),per)

#per is 0-1
def tint(image_old,color=(0,0,0),per=0.5):
	image=image_old.copy()
	pix=image.load()
	w,h=image.size
	rc,gc,bc=color
	for y in range(h):
		for x in range(w):
			r,g,b=pix[x,y]
			newr=int(rc*per+(1-per)*r)
			newg=int(gc*per+(1-per)*g)
			newb=int(bc*per+(1-per)*b)
			pix[x,y]=newr,newg,newb
	return image

def invert(image_old):
	image=image_old.copy()
	pix=image.load()
	w,h=image.size
	for y in range(h):
		for x in range(w):
			r,g,b=pix[x,y]
			pix[x,y]=255-r,255-g,255-b 	
	return image

default_size=(500,500)
image=getImageFile()
try: original_image=Image.open(image).convert("RGB")
except: original_image=Image.new("RGB",default_size,(255,255,255))

series=[original_image.copy()]
redo=[]
pix=series[-1].load() 
w,h=series[-1].size
go=True

while go==True:
	prompt=int(input('''
0: Save and Exit
1: Lighten
2: Darken
3: Tint
4: Greyscale
5: Dessaturate
6: Invert
7: Black and White
8: Display
9: Undo Change
10: Redo Change
11: Revert to Original
	
What do you wish to do?: '''))
	if prompt==0:
		name=input("what do what to call the file?: ")
		image.save(name+".png","PNG")
		go=False
	elif prompt==1:
		per=float(input("how much should it be lightened by?(0 - 1): "))
		series.append(lighten(series[-1],per))
		display(series[-1])
		redo=[]
	elif prompt==2:
		per=float(input("how much should it be darkened by?(0 - 1): "))
		series.append(darken(series[-1],per))
		display(series[-1])
		redo=[]
	elif prompt==3:
		color=[int(elem) for elem in input("give me a color(ex. 0,0,0 for white): ").split(",")]
		per=float(input("how much should it be tinted by?(0 - 1): "))
		series.append(tint(series[-1],color,per))
		display(series[-1])
		redo=[]
	elif prompt==4:
		series.append(greyscale(series[-1]))
		display(series[-1])
		redo=[]
	elif prompt==5:
		per=float(input("how much should it be dessaturated by?(0 - 1): "))
		series.append(dessaturate(series[-1],per))
		display(series[-1])
		redo=[]
	elif prompt==6:
		series.append(invert(series[-1]))
		display(series[-1])
		redo=[]
	elif prompt==7:
		a=int(input("What do you want the threshold to be?(0-255): "))
		series.append(b_w(series[-1],a))
		display(series[-1])	
		redo=[]
	elif prompt==8:
		display(series[-1])
	elif prompt==9:
		if(len(series)>1): 
			redo.append(series[-1].copy())
			series.pop()
		else: print("no undo")
		display(series[-1])
	elif prompt==10:
		if len(redo)>0: 
			series.append(redo[0])
			redo.pop(0)
		else: print("There is nothing to redo")
		display(series[-1])
	elif prompt==11:
		redo.append(series[-1].copy())
		series=[series[0]]
		display(series[-1])
	
	else:
		print("That is an invalid comand")
'''	
filters=[]
filters.append(b_w)

f=lambda image:dessaturate(image,20)
'''
