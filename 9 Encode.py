from PIL import Image

def getImageFile(prompt):
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
    filenum=-1
    try:
        filenum = int(input(prompt))
    except ValueError:
        pass
     
    while filenum<1 or filenum>len(files):
        print("Invalid entry\n")
        try:
            filenum = int(input(prompt))
        except ValueError:
            pass
    return Image.open(files[filenum-1])
    
def encodeImage(img, text):
    pix = img.load()
    w,h = img.size
    for y in range(h):
        for x in range(w):
            if h*y+x>=len(text):
                r,g,b=pix[x,y]
                if r%10!=0:
                   r-=r%10
                if g%10!=0:
                    g-=g%10
                if b%10!=3:
                    b+=3-b%10   
                pix[x,y]=r,g,b
                return img
            num = ord(text[h*y + x])
            hundred = num//100%10
            ten = num//10%10
            one = num%10
            r,g,b = pix[x,y]
            if r%10 != hundred:
               r += hundred - r%10
            if g%10 != ten:
                g += ten - g%10
            if b%10 != one:
                b += one - b%10   
            pix[x,y] = r,g,b
    return img

img = getImageFile("Input Image: ")    
text = input("\nText to encode: ")
imgout = encodeImage(img.copy(), text)
imgout.save("i.png")
