from PIL import Image

def getImageFile(prompt="Image: "):
    import os,sys
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
        f=Image.open(files[filenum-1])
    except (ValueError,IndexError):
         return getImageFile()
    return f

img=getImageFile()
f=open(input("\nWhat do you want to call the .sqr file: ")+".sqr","wb")
f.write(bytes("SQUIRREL","ascii"))
w,h=img.size
size=bytes([w//256,w%256,h//256,h%256])
f.write(size)
pix=img.load()
for y in range(h):
    for x in range(w):
        f.write(bytes(pix[x,y]))
f.close()
