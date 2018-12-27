from PIL import Image, ImageTk
import tkinter,math,os

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
    filenum=input("What file do you want?: ")
    try: filenum=int(filenum)
    except: return ""
    while 1>filenum or filenum>len(files):
        print("That is an invalid entry.")
        filenum=input("What file do you want?: ")
        try: filenum=int(filenum)
        except: return ""
    return files[filenum-1]

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
	
image=getImageFile()
try: original_image=Image.open(image).convert("RGB")
except: 
	print("nope")
	system.exit()
image=original_image.copy()

fps=int(input("what is the fps?: "))
trans_time=int(input("what is the time?: "))

newpath = "output/" 
if not os.path.exists(newpath): os.makedirs(newpath)

for i in range((trans_time//8)*fps):
	img=dessaturate(image,1-i/((trans_time//8)*fps))
	img.save("output/"+str(fps-i).zfill(3)+".png")
	img.save("output/"+str(i+fps).zfill(3)+".png")
for i in range((trans_time//8)*fps):
	img=tint(image,(255,0,0),1-i/((trans_time//8)*fps))
	img.save("output/"+str(fps*3-i).zfill(3)+".png")
	img.save("output/"+str(i+fps*3).zfill(3)+".png")
for i in range((trans_time//8)*fps):
	img=tint(image,(0,255,0),1-i/((trans_time//8)*fps))
	img.save("output/"+str(fps*5-i).zfill(3)+".png")
	img.save("output/"+str(i+fps*5).zfill(3)+".png")
for i in range((trans_time//8)*fps):
	img=tint(image,(0,0,255),1-i/((trans_time//8)*fps))
	img.save("output/"+str(fps*7-i).zfill(3)+".png")
	img.save("output/"+str(i+fps*7).zfill(3)+".png")
for i in range(trans_time//2+1):
	original_image.save("output/"+str(i*fps*2).zfill(3)+".png")
