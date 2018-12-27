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
    
def avgpix(pixs,pers,size):
    sumr=sumg=sumb=case=0
    for pix in pixs:
        sumr+=pix[0]*pers[case]
        sumg+=pix[1]*pers[case]
        sumb+=pix[2]*pers[case]
        case+=1
    sumr=sumr/size
    sumg=sumg/size
    sumb=sumb/size
    #print(len(pixs))
    #print(int(sumr),int(sumg),int(sumb))
    return(int(sumr),int(sumg),int(sumb))
    
def scale(img_old,numx,numy):
    w,h=img_old.size
    w*=numx
    h*=numy
    w=int(w)
    h=int(h)
    scale=img_old.size[0]/w
    #print(scale)
    img=Image.new("RGB",(w,h),(0,0,0))
    pixin=img_old.load()
    img_h=img_old.copy().resize((w, h), Image.LINEAR)
    pixout=img.load()
    for y in range(h): #Loop through new image
        for x in range(w):
            pixs=[]
            pers=[]
            start=math.floor(x+1*scale)
            end=math.ceil(x+1*scale+scale+0.0)
            #print(start,end)
            start=end=0
            for z in range(start,end):#cant use floats
                #print(z)
                pixs.append(pixin[z,y])
                pers.append((z*scale)%1)
                #print(z*scale)
            #print(len(pixs),len(pers))
            pixout[x,y]=avgpix(pixs,pers,len(pixs)+1)
    return img_h
    
while True:
    prompt=input("\n1)Scale X\n2)Scale Y\n3)Quit")
    if prompt=="1":
        img=getImageFile()
        scale(img,float(input("X factor: ")),1)
    elif prompt=="2":
        img=getImageFile()
        scale(img,1,float(input("Y factor: ")))
    else:
        sys.exit()
scale(getImageFile(),4,.75).save("test.png")

