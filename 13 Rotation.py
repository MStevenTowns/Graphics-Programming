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
def distance(x1,x2,y1,y2):#distance between 2 points
		part1=(x1-x2)*(x1-x2)
		part2=(y1-y2)*(y1-y2)
		dist=math.sqrt(part1+part2)
		return dist
        
def flipX(img_old):
    w,h=img_old.size
    img=Image.new("RGB",(w,h))
    pixin=img_old.load()
    pixout=img.load()
    for y in range(h):
        for x in range(w):
            pixout[x,y]=pixin[w-x-1,y]
    return img
def flipY(img_old):
    w,h=img_old.size
    img=Image.new("RGB",(w,h))
    pixin=img_old.load()
    pixout=img.load()
    for y in range(h):
        for x in range(w):
            #print(x,y)
            pixout[x,y]=pixin[x,h-y-1]
    return img
def flipXY(img_old):
    w,h=img_old.size
    img=Image.new("RGB",(w,h))
    pixin=img_old.load()
    pixout=img.load()
    for y in range(h):
        for x in range(w):
            pixout[x,y]=pixin[y,x]
    return img
def rot(img_old,angle):
    w,h=img_old.size
    xc=w//2
    yc=h//2
    img=Image.new("RGB",(w,h))
    pixin=img_old.load()
    pixout=img.load()
    for y in range(h):
        for x in range(w):
            rad=distance(x,xc,y,yc)
            degree=math.atan2(y-yc,x-xc)
            x_old=rad*math.cos(degree+(angle*math.pi)/180)+xc
            y_old=rad*math.sin(degree+(angle*math.pi)/180)+yc
            try:pixout[x,y]=pixin[x_old,y_old]
            except:pass
    return img
    
def decide(img,angle):
    angle%=360
    #print(angle)
    if angle==0: return img.copy()
    if angle==90: return flipY(flipXY(img.copy()))
    if angle==180: return flipX(flipY(img.copy()))
    if angle==270: return flipX(flipXY(img.copy()))
    else: return rot(img.copy(),angle)
    
go=True
while go:
    img=getImageFile()
    num=None
    while num==None:
        try:
            num=float(input("how far left should it rotate?(x>0): "))
        except ValueError:
            print("Chose an actual number")
    imgNew=decide(img,num)
    imgNew.show()
    if input("Save?: ")[0].lower()!="n":
        imgNew.save(input("what do you want to call the image?: ")+".png")
    if input("Again?: ")[0].lower()=="n":
        go=False


