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
def flag(img,shift):
    w,h=img.size
    pixIn=img.load()
    imgOut=Image.new("RGB",(w,h))
    topMarg=40
    sideMarg=20
    fHeight=h-topMarg*2
    fWidth=w-sideMarg*2
    pixOut=imgOut.load()
    for y in range(h):
        for x in range(w):
            px=(x-sideMarg)/fWidth
            py=(y-sideMarg*math.sin((x-sideMarg)/fWidth*2*math.pi+shift)-topMarg)/fHeight
            if 0<px<1 and 0<py<1:
                xp,yp=px*w,py*h
                pixOut[x,y]=pixIn[xp,yp]
    return imgOut
img=getImageFile()
newpath = "output/" 
if not os.path.exists(newpath): os.makedirs(newpath)
frames=120
for i in range(frames):
        if i<95: flag(img,(i/15)).save("output/"+str(i).zfill(3)+".png")
        else: pass
