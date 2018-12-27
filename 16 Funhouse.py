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
    except (ValueError,IndexError):
         return getImageFile()
    return img
    
def distance(x1,x2,y1,y2):#distance between 2 points
		part1=(x1-x2)*(x1-x2)
		part2=(y1-y2)*(y1-y2)
		dist=math.sqrt(part1+part2)
		return dist
        
def wave(img,amp):
	#print(amp)
	w,h=img.size
	pixIn=img.load()
	imgOut=Image.new("RGB",(w,h))
	pixOut=imgOut.load()
	for y in range(h):
		for x in range(w):
			yp=y+amp*math.sin(y*(2*math.pi/h))
			xp=x+amp*math.sin(x*(2*math.pi/w))
			pixOut[x,y]=pixIn[xp,yp]
	return imgOut
    
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
    
img=getImageFile()
newpath = "output/" 
if not os.path.exists(newpath): os.makedirs(newpath)

maxAmp=30
frames=maxAmp*4
for i in range (frames):
    rot(wave(img,i*(maxAmp/frames)),(i*10/frames)-5).save("output/"+str(i).zfill(3)+".png")
for i in range(frames,frames*2):
	rot(wave(img,maxAmp*2-i*(maxAmp/frames)),(10*2-i*10/frames)-5).save("output/"+str(i).zfill(3)+".png")
