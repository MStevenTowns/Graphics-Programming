import pygame,pygame.camera,sys,numpy,math
def distance(x1,x2,y1,y2)
		part1=(x1-x2)*(x1-x2);
		part2=(y1-y2)*(y1-y2);
		dist=Math.sqrt(part1+part2);
		return dist; 
        
def invert(r,g,b):
    r=255-r    
    g=255-g    
    b=255-b
    return r,g,b
def color8(r,g,b):
    r=r//128*255
    g=g//128*255
    b=b//128*255
    return r,g,b
def colorScale(r=0,g=0,b=0):
    return r,g,b
def desaturate(r,g,b):
    grey=(.2*r+.7*g+.1*b)//1
    return grey,grey,grey
def tint(r,g,b,color,per):
    rc,gc,bc=color
    r=int(rc*per+(1-per)*r)
    g=int(gc*per+(1-per)*g)
    b=int(bc*per+(1-per)*b)
    return r,g,b
def lighten(r,g,b,per):
    return tint(r,g,b,(255,255,255),per)
def darken(r,g,b,per):
    return tint(r,g,b,(0,0,0),per)
def warpSplit(snap,change,counter):
    rows=[]
    for y in range(h):
        yp=y+int((25*math.sin(counter/60*2*math.pi))*math.sin(y/h*4*math.pi))
        row=snap[:,yp:yp+1]
        rows.append(row)
    snap=numpy.hstack(rows)
    cols=[]
    for x in range(w):
        xp=x+int((25*math.sin(counter/49*2*math.pi))*math.sin(x/w*4*math.pi))
        col=snap[xp:xp+1,:]
        cols.append(col)
    snap=numpy.vstack(cols)
    counter+=1
    try: square_size=factor[change]
    except: 
        change=0
        square_size=factor[change]
    
    block=snap[320-square_size:320+square_size:2,240-square_size:240+square_size:2]
    rows=[]
    for row in range(w//square_size):
        m=[]
        for col in range(h//square_size):
            temp=block[:,:]
            if col%2==1:
                temp=temp[:,::-1]
            if row%2==1:
                temp=temp[::-1]
            m.append(temp)
        row_array=numpy.hstack(m)
        rows.append(row_array)
    snap=numpy.vstack(rows)
    return snap
def warp(snap):
    rows=[]
    for y in range(h):
        yp=y+int((25*math.sin(counter/60*2*math.pi))*math.sin(y/h*4*math.pi))
        row=snap[:,yp:yp+1]
        rows.append(row)
    snap=numpy.hstack(rows)
    cols=[]
    for x in range(w):
        xp=x+int((25*math.sin(counter/49*2*math.pi))*math.sin(x/w*4*math.pi))
        col=snap[xp:xp+1,:]
        cols.append(col)
    snap=numpy.vstack(cols)
    return(snap)
def divide(snap,change):    
    try: square_size=factor[change]
    except: 
        change=0
        square_size=factor[change]
        
    block=snap[320-square_size:320+square_size:2,240-square_size:240+square_size:2]
    rows=[]
    for row in range(w//square_size):
        m=[]
        for col in range(h//square_size):
            temp=block[:,:]
            if col%2==1:
                temp=temp[:,::-1]
            if row%2==1:
                temp=temp[::-1]
            m.append(temp)
        row_array=numpy.hstack(m)
        rows.append(row_array)
    snap=numpy.vstack(rows)
    return snap
def split2(snap):
    right=snap[len(snap)//2:,:]
    left=right[::-1]
    snap=numpy.vstack((left,right))    
    return snap

pygame.init()
pygame.camera.init()
cameras = pygame.camera.list_cameras()
try: cam = pygame.camera.Camera(cameras[0],(640,480))
except: sys.exit("No webcam found.")
cam.start()
screen = pygame.display.set_mode((640,480))#,pygame.FULLSCREEN)
snapshot = pygame.surface.Surface((640,480))
pygame.surfarray.use_arraytype("numpy")
previous=snapshot.copy()

key=0
split=0
change=0
side=True
up=False
counter=0
w,h=640,480
factor=[]
for i in range(2,min(w,h)):
    if (w%i==0) and (h%i==0): factor+=[i]
while 1:
    #HANDLE EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE: sys.exit()
            elif event.key==pygame.K_n: key=0;split=0;change=0;counter=0;side=True;up=False
            elif event.key==pygame.K_i: key=1
            elif event.key==pygame.K_8: key=2
            elif event.key==pygame.K_l: key=3
            elif event.key==pygame.K_r: key=4
            elif event.key==pygame.K_g: key=5
            elif event.key==pygame.K_b: key=6
            elif event.key==pygame.K_p: key=7           
            elif event.key==pygame.K_y: key=8
            elif event.key==pygame.K_t: key=9
            elif event.key==pygame.K_s: split=1;change=10
            elif event.key==pygame.K_w: split=2
            elif event.key==pygame.K_d: split=3;change=10
            elif event.key==pygame.K_c: split=4;change=10;side=False
            elif event.key==pygame.K_x: split=5;change=10;side=False
            elif event.key==pygame.K_z: key=10;split=0;side=True;up=False
            elif event.key==pygame.K_DOWN or event.key==pygame.K_UP: up=not up
            elif event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT: side=not side
            elif event.key==pygame.K_KP_PLUS: change+=1
            elif event.key==pygame.K_KP_MINUS: change-=1
    
    pygame.time.wait(10)
    snapshot=cam.get_image(snapshot)
    snapshot=pygame.transform.flip(snapshot, side,up)
    snap= pygame.surfarray.array2d(snapshot)
 
    b=snap%256
    snap/=256
    g=snap%256
    snap/=256
    r=snap

    if key==1: r,g,b=invert(r,g,b)
    elif key==2: r,g,b=color8(r,g,b)
    elif key==3: r,g,b=desaturate(r,g,b)
    elif key==4: r,g,b=colorScale(r=r)
    elif key==5: r,g,b=colorScale(g=g)
    elif key==6: r,g,b=colorScale(b=b)
    elif key==7: r,g,b=colorScale(r=r,b=b)
    elif key==8: r,g,b=colorScale(r=r,g=g)
    elif key==9: r,g,b=colorScale(g=g,b=b)
    snap=r*256**2+g*256+b
    if split==1:
        snap=warpSplit(snap,change,counter)
    elif split==2:
        snap=warp(snap)
        counter+=1
    elif split==3:
        snap=divide(snap,change)
    elif split==4:
        snap=split2(snap)
    elif split==5:
        rows=[]
        for y in range(h):
            yp=y+int((25*math.sin(counter/60*2*math.pi))*math.sin(y/h*4*math.pi))
            row=snap[:,yp:yp+1]
            rows.append(row)
        snap=numpy.hstack(rows)
        cols=[]
        for x in range(w):
            xp=x+int((25*math.sin(counter/49*2*math.pi))*math.sin(x/w*4*math.pi))
            col=snap[xp:xp+1,:]
            cols.append(col)
        snap=numpy.vstack(cols)
        counter+=1
        right=snap[len(snap)//2:,:]
        left=right[::-1]
        snap=numpy.vstack((left,right))
    if key==10:
        
    #DRAW ARRAY ON SNAPSHOT SURFACE
    pygame.surfarray.blit_array(snapshot, snap)
    screen.blit(snapshot,(0,0)) 
    previous=snapshot.copy()
    pygame.display.flip()
