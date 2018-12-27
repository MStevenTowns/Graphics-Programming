import pygame
import pygame.camera
import sys
import numpy

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
def desaturate(r,g,b,per):
    grey=(.2*r+.7*g+.1*b)
    r=int((r*(1-per))+(grey*(per)))
    g=int((g*(1-per))+(grey*(per)))
    b=int((b*(1-per))+(grey*(per)))
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
side=True
up=False
per=.5
while 1:
    #HANDLE EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE: sys.exit()
            elif event.key==pygame.K_n: key=0
            elif event.key==pygame.K_i: key=1
            elif event.key==pygame.K_8: key=2
            elif event.key==pygame.K_l: key=3
            elif event.key==pygame.K_r: key=4
            elif event.key==pygame.K_g: key=5
            elif event.key==pygame.K_b: key=6
            elif event.key==pygame.K_p: key=7           
            elif event.key==pygame.K_y: key=8
            elif event.key==pygame.K_t: key=9
            elif event.key==pygame.K_DOWN or event.key==pygame.K_UP: up=not up
            elif event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT: side=not side
            elif event.key==pygame.K_KP_PLUS: per+=.1
            elif event.key==pygame.K_KP_MINUS: per-=.1
    
    pygame.time.wait(10)
    snapshot=cam.get_image(snapshot)
    snapshot=pygame.transform.flip(snapshot, side,up)
    snapArray = pygame.surfarray.array2d(snapshot)
 
    b=snapArray%256
    snapArray/=256
    g=snapArray%256
    snapArray/=256
    r=snapArray

    if key==1: r,g,b=invert(r,g,b)
    elif key==2: r,g,b=color8(r,g,b)
    elif key==3: r,g,b=desaturate(r,g,b,per)
    elif key==4: r,g,b=colorScale(r=r)
    elif key==5: r,g,b=colorScale(g=g)
    elif key==6: r,g,b=colorScale(b=b)
    elif key==7: r,g,b=colorScale(r=r,b=b)
    elif key==8: r,g,b=colorScale(r=r,g=g)
    elif key==9: r,g,b=colorScale(g=g,b=b)
    newArray=r*256**2+g*256+b
    
    #DRAW ARRAY ON SNAPSHOT SURFACE
    pygame.surfarray.blit_array(snapshot, newArray)
    
    screen.blit(snapshot,(0,0)) 
    previous=snapshot.copy()
    pygame.display.flip()
