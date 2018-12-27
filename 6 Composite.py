from PIL import Image, ImageTk,ImageOps
import tkinter,math,os,sys, random

def getImageFile():
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
    filenum=input("What file do you want?: ")
    try: filenum=int(filenum)
    except: return ""
    while 1>filenum or filenum>len(files):
        print("That is an invalid entry.")
        filenum=input("What file do you want?: ")
        try: filenum=int(filenum)
        except: return ""
    return files[filenum-1]
        
def display(image):
	root = tkinter.Tk()  
	# A root window for displaying objects
	# Convert the Image object into a TkPhoto 
	tkimage = ImageTk.PhotoImage(image)
	tkinter.Label(root, image=tkimage).pack()
	# Put it in the display window
	root.mainloop()

def distance(x1,x2,y1,y2):#distance between 2 points
		part1=(x1-x2)*(x1-x2)
		part2=(y1-y2)*(y1-y2)
		dist=math.sqrt(part1+part2)
		return dist

def composite(image_old1,image_old2,image_total,per):
	image1=image_old1.copy()
	image2=image_old2.copy()
	pix1=image1.load()
	pix2=image2.load()
	pix3=image_total.load()
	w,h=image1.size
	for y in range(h):
		for x in range(w):
			r1,g1,b1=pix1[x,y]
			r2,g2,b2=pix2[x,y]
			r=int((r1*per)+(r2*(1-per)))
			g=int((g1*per)+(g2*(1-per)))
			b=int((b1*per)+(b2*(1-per)))
			pix3[x,y]=r,g,b
	return image_total

def fadeH(image_old1,image_old2,image_total):
	image1=image_old1.copy()
	image2=image_old2.copy()
	pix1=image1.load()
	pix2=image2.load()
	pix3=image_total.load()
	w,h=image1.size
	for y in range(h):
		for x in range(w):
			r1,g1,b1=pix1[x,y]
			r2,g2,b2=pix2[x,y]
			per=x/w
			r=int((r1*per)+(r2*(1-per)))
			g=int((g1*per)+(g2*(1-per)))
			b=int((b1*per)+(b2*(1-per)))
			pix3[x,y]=r,g,b
	return image_total
def fadeV(image_old1,image_old2,image_total):
	image1=image_old1.copy()
	image2=image_old2.copy()
	pix1=image1.load()
	pix2=image2.load()
	pix3=image_total.load()
	w,h=image1.size
	for y in range(h):
		for x in range(w):
			r1,g1,b1=pix1[x,y]
			r2,g2,b2=pix2[x,y]
			per=y/h
			r=int((r1*per)+(r2*(1-per)))
			g=int((g1*per)+(g2*(1-per)))
			b=int((b1*per)+(b2*(1-per)))
			pix3[x,y]=r,g,b
	return image_total	
def rand(image_old1,image_old2,image_total):
	image1=image_old1.copy()
	image2=image_old2.copy()
	pix1=image1.load()
	pix2=image2.load()
	pix3=image_total.load()
	w,h=image1.size
	for y in range(h):
		for x in range(w):
			r1,g1,b1=pix1[x,y]
			r2,g2,b2=pix2[x,y]
			num=random.randint(1,2)
			if num==1: pix3[x,y]=r1,g1,b1
			elif num==2: pix3[x,y]=r2,g2,b2
	return image_total

def circle(image_old1,image_old2,image_total,radius,point):
    a,b=point
    image1=image_old1.copy()
    image2=image_old2.copy()
    pix1=image1.load()
    pix2=image2.load()
    pix3=image_total.load()
    w,h=image1.size
    for y in range(h):
        for x in range(w):
            r1,g1,b1=pix1[x,y]
            r2,g2,b2=pix2[x,y]
            if distance(a,x,b,y)<radius: pix3[x,y]=r1,g1,b1
            else: pix3[x,y]=r2,g2,b2
    return image_total    

go=True
while go==True:
    try: original_image1=Image.open(getImageFile()).convert("RGB")
    except: 
        print("nope")
        sys.exit(0)
    image1=original_image1.copy()
    try: original_image2=Image.open(getImageFile()).convert("RGB")
    except:
        print("nope")
        system.exit()
    image2=original_image2.copy()
    w1,h1=image1.size
    w2,h2=image2.size
    if w1<w2: w=w1
    else: w=w2
    if h1<h2: h=h1
    else: h=h2
    image1=ImageOps.fit(image1,(w,h),Image.ANTIALIAS)
    image2=ImageOps.fit(image2,(w,h),Image.ANTIALIAS)
    image_total=Image.new("RGB",(w,h),(255,255,255))
    prompt=int(input('''
0: Quit
1: Fade Horizontal
2: Fade Vertically
3: Randomize
4: Draw A Circle
5: Composite
What do you wish to do?: '''))

    if prompt==1:
        hold=fadeH(image1,image2,image_total)
        display(hold)
    elif prompt==2:
        hold=fadeV(image1,image2,image_total)
        display(hold)
    elif prompt==3:
        hold=rand(image1,image2,image_total)
        display(hold)
    elif prompt==4:
        point=[int(elem) for elem in input("give me a point ex.(50,50): ").split(",")]
        num=int(input("What is the radius of the circle: "))
        hold=circle(image1,image2,image_total,num,point)
        display(hold)
    elif prompt==5:
        per=float(input("What percent of the first image do you want to use?(0-1): "))
        hold=composite(image1,image2,image_total,per)
        display(hold)
    elif prompt==0:
        go=False
    if input("Save?: ")[0].lower()=="y":
        name=input("what do what to call the file?: ")
        hold.save(name+".png","PNG")
    print("\n\n")

