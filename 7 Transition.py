from PIL import Image, ImageTk
import tkinter,math,os

def getImageFile(q="What file do you want? "):
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
    filenum=input(q)
    filenum=int(filenum)
    while 1>filenum or filenum>len(files):
        print("That is an invalid entry.")
        filenum=input(q)
        filenum=int(filenum)
    return files[filenum-1]

img1=Image.open(getImageFile("First File: ")).convert("RGB")
img2=Image.open(getImageFile("\nSecond File: ")).convert("RGB")
img3=Image.open(getImageFile("\nTransition File: ")).convert("RGB")
newpath = "output/" 
if not os.path.exists(newpath): os.makedirs(newpath)

for z in range(0,257):
    output=Image.new("RGB",img1.size,(0,0,0))
    pix1=img1.load()
    pix2=img2.load()
    pixT=img3.load()
    pixOut=output.load()
    width, height= img1.size
    for y in range(height):
        for x in range(width):
            r,g,b=pixT[x,y]
            if r<z:
                pixOut[x,y]=pix1[x,y]
            else:
                pixOut[x,y]=pix2[x,y]
    output.save("output/"+str(z).zfill(3)+".png")
    print(str(z).zfill(3)+".png")
for z in range(0,257):
    output=Image.new("RGB",img1.size,(0,0,0))
    pix1=img1.load()
    pix2=img2.load()
    pixT=img3.load()
    pixOut=output.load()
    width, height= img1.size
    for y in range(height):
        for x in range(width):
            r,g,b=pixT[x,y]
            if r<z:
                pixOut[x,y]=pix2[x,y]
            else:
                pixOut[x,y]=pix1[x,y]

    output.save("output/"+str(z+256).zfill(3)+".png")
    print(str(z+256).zfill(3)+".png")
