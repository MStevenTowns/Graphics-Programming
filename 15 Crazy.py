from PIL import Image
import os,sys,math

def getImageFile(prompt="Image: "):
    formats=[".bmp",".dib",".dcx",".gif",".im",".jpg",".jpe",".jpeg",
             ".pcd",".pcx",".png",".pbm",".pgm",".ppm",".psd",".tif",
             ".tiff",".xbm",".xpm"]
    i=1
    files=[]
    print()
    for f in os.listdir("."):
        for ex in formats:
            if f[-len(ex):]==ex:
                print(str(i)+")",f)
                files+=[f]
                i+=1
    if len(files)==0:
        print("No images found")
        sys.exit()
    try:
        filenum = int(input(prompt))
        img=Image.open(files[filenum-1]).convert("RGB")
        #img.show()
    except (ValueError,IndexError):
         return getImageFile()
    return img
    
def warp(img,sides):
    w,h=img.size
    pixIn=img.load()
    imgOut=Image.new("RGB",(w,h))
    for i in range(sides):
        
        for y in range(h):
            for x in range(w):
                
                
                if 0<px<1 and 0<py<1:
                    xp,yp=px*w,py*h
                    pixOut[x,y]=pixIn[xp,yp]
    return imgOut

img=getImageFile()
newpath = "output/" 
if not os.path.exists(newpath): os.makedirs(newpath)
frames=10
for i in range(frames):
        warp(img,i+3).save("output/"+str(i).zfill(3)+".png")
        print(str((i/frames)*100)+"%")
