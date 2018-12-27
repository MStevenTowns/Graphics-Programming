from PIL import Image

def getImageFile(prompt="What file do you want? "):
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
    filenum=input(prompt)
    filenum=int(filenum)
    while 1>filenum or filenum>len(files):
        print("That is an invalid entry.")
        filenum=input(prompt)
        filenum=int(filenum)
    return Image.open(files[filenum-1]).convert("RGB")

image1=getImageFile("image1: ")
image2=getImageFile("image2: ")
pix1=image1.load()
pix2=image2.load()
w,h=image1.size
c=0
image3=Image.new("RGB",(w,h),(255,255,255))
pix3=image3.load()
for y in range(h):
    for x in range(w):
        r1,g1,b1=pix1[x,y]
        r2,g2,b2=pix2[x,y]
        if abs(r1-r2)>20 or abs(g1-g2)>20 or abs(b1-b2)>20:
            pix3[x,y]=255,0,0
            c+=1
print(str(round((1-c/(w*h))*100,2))+"%")
image3.show()
            
        
