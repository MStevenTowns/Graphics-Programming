from PIL import Image
import os,sys

def getTextFile(prompt="File: "):
    i=1
    files=[]
    for f in os.listdir("."):
        if f.endswith(".sqr"or".sqc" ):
            print(str(i)+")",f)
            files.append(f)
            i+=1
    if len(files)==0:
        print("No readable files are in this directory.")
        sys.exit()
    filenum=-1
    filenum=-1
    try:
        filenum = int(input(prompt))
        f=open(files[filenum-1],"rb")
    except (ValueError,IndexError):
         return getImageFile()
    return f

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
        img.show()
    except (ValueError,IndexError):
         return getImageFile()
    return img
    
def toRawSquirrel(img,f):
    f.write(bytes("SQUIRREL","ascii"))
    w,h=img.size
    f.write(bytes([w//256,w%256,h//256,h%256]))
    pix=img.load()
    for y in range(h):
        for x in range(w):
            f.write(bytes(pix[x,y]))
    f.close()
    
def toCompressedSquirrel(img,f):
    f.write(bytes("SquirRLE","ascii"))
    w,h=img.size
    f.write(bytes([w//256,w%256,h//256,h%256]))
    pix=img.load()
    color=pix[0,0]
    count=1
    for y in range(h):
        for x in range(w):
            newColor=pix[x,y]
            if newColor==color:
                count+=1
            else:
                r,g,b=color
                f.write(bytes([r,g,b,count]))
                color=newColor
                count=1
    f.close()
                

def toImg(f):
    header=str(f.read(8))[2:-1]
    width=int.from_bytes(f.read(2),byteorder='big')
    height=int.from_bytes(f.read(2),byteorder='big')
    img=Image.new("RGB",(width,height))
    pix = img.load()
    if header == "SQUIRREL":
        for y in range(height):
            for x in range(width):
                r=int.from_bytes(f.read(1),byteorder='big')
                g=int.from_bytes(f.read(1),byteorder='big')
                b=int.from_bytes(f.read(1),byteorder='big')
                pix[x,y]=r,g,b
    
    elif header == "SquirRLE":
        r=int.from_bytes(f.read(1),byteorder='big')
        g=int.from_bytes(f.read(1),byteorder='big')
        b=int.from_bytes(f.read(1),byteorder='big')
        count = int.from_bytes(f.read(1),byteorder='big')
        for y in range(height):
            for x in range(width):
                if count == 0:
                    r=int.from_bytes(f.read(1),byteorder='big')
                    g=int.from_bytes(f.read(1),byteorder='big')
                    b=int.from_bytes(f.read(1),byteorder='big')
                    count = int.from_bytes(f.read(1),byteorder='big')
                pix[x,y] = r,g,b
                count-=1
    return img

while True:
    prompt=input("\n1)Convert to raw .sqr\n2)Convert to compressed .sqr\n3)Convert from .sqr\nWhat do you wish to do?: ")
    if prompt=="1":
        img=getImageFile("Input image: ")
        f=open(input("\nWhat do you want to call the .sqr file: ")+".sqr","wb")
        toRawSquirrel(img,f)
        
    elif prompt=="2":
        img=getImageFile("Input image: ")
        f=open(input("\nWhat do you want to call the .sqr file: ")+".sqr","wb")
        toCompressedSquirrel(img,f)

    elif prompt=="3":
        f=getTextFile("SQR image: ")
        img=toImg(f)
        img.show()
        output=input("What do you want to call the image: ")+".png"
        img.save(output)
    else:
        sys.exit()
    
