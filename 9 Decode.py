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
    
def decode(img):
    pix = img.load()
    w,h = img.size
    text=""
    for y in range(h):
        for x in range(w):
            r,g,b = pix[x,y]
            hundred=r%10
            ten=g%10
            one=b%10
            c=chr(hundred*100 + ten*10 + one)
            if c==chr(3):return text
            text+=c
            
img = getImageFile("Input Image: ")
print(decode(img.copy()))
