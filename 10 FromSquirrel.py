from PIL import Image

def getTextFile(prompt="File: "):
    import os,sys
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
    
f=getTextFile()
ext=f.read(8).decode("ascii")
w=(int.from_bytes(f.read(2),byteorder='big'))
h=(int.from_bytes(f.read(2),byteorder='big'))
img=Image.new("RGB",(w,h),0)
pix=img.load()
if ext=="SQUIRREL":
    for y in range(h):
        for x in range(w):
            r=int.from_bytes(f.read(1),byteorder='big')
            g=int.from_bytes(f.read(1),byteorder='big')
            b=int.from_bytes(f.read(1),byteorder='big')
            pix[x,y]=(r,g,b)
    img.save(input("What do you want to call the image: ")+".png")
    img.show()
elif ext=="SquirRLE":
    
else: print("Invalid Image format")
