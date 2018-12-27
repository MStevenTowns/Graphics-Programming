"""
8B "SQUIRREL"
2B width
2B height


PIXEL 0
1B RED
1B GREEN
1B BLUE"""

from PIL import Image

f=open("test.sqr","wb")
f.write(bytes("SQUIRREL","ascii"))
image=Image.open("wolf.jpg").convert("RGB")

w,h=image.size
size=bytes([w//256,w%256,h//256,h%256])
f.write(size)
pix=image.load()
for y in range(h):
    for x in range(w):
        f.write(bytes(pix[x,y]))
f.close()


##DECODER:
f=open("test.sqr","rb")
ext=f.read(8).decode("ascii")
if ext=="SQUIRREL":
    w=(int.from_bytes(f.read(2),byteorder='big'))
    h=(int.from_bytes(f.read(2),byteorder='big'))
    img=Image.new("RGB",(w,h),0)
    pix=img.load()
    for y in range(h):
        for x in range(w):
            r=f.read(1)
            r=int.from_bytes(r,byteorder='big')
            g=f.read(1)
            g=int.from_bytes(g,byteorder='big')
            b=f.read(1)
            b=int.from_bytes(b,byteorder='big')
            pix[x,y]=(r,g,b)
    img.show()
else: print("Invalid Image format")
