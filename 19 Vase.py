import pygame
import pygame.camera
import sys
import numpy
import math


pygame.init()
pygame.camera.init()
cameras = pygame.camera.list_cameras()
try:
    cam = pygame.camera.Camera(cameras[0],(640,480))
except:
    sys.exit("No webcam found.")
    
cam.start()
screen = pygame.display.set_mode((640,480))#,pygame.FULLSCREEN)
snapshot = pygame.surface.Surface((640,480))
pygame.surfarray.use_arraytype("numpy")

#LOOP FOREVER
while 1:
    #HANDLE EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    pygame.time.wait(10)

    #GRAB WEBCAM IMAGE
    snapshot=cam.get_image(snapshot)

    #DO A HORIZONTAL AND/OR VERTICAL FLIP
    snapshot=pygame.transform.flip(snapshot, True,False)

    #GET ARRAY OF WEBCAM IMAGE
    snapArray = pygame.surfarray.array2d(snapshot)
    
    b=snapArray%256
    snapArray/=256
    g=snapArray%256
    snapArray/=256
    r=snapArray
    newArray=r*256**2+g*256+b
    
    pygame.surfarray.blit_array(snapshot,newArray)
    spot=pygame.mask.from_threshold(snapshot,(255,255,0),(100,100,100,255))
    blocks=spot.get_bounding_rects()
    
    sizehold=0
    sizeloc=0
    for z in range(len(blocks)):
        block=blocks[z]
        size=block.size[0]*block.size[1]
        if (size>sizehold):
            sizeloc=z
            sizehold=size
    try:
        mid=blocks[sizeloc].center
        w,h=blocks[sizeloc].size
        r=int(math.sqrt((w**2)+(h**2))*.75)
        if mid!=(0,0):
            pygame.draw.circle(snapshot,(0,0,0),mid,r,5)  
    except: pass
    #DRAW SNAPSHOT ON THE DISPLAY
    screen.blit(snapshot,(0,0))    

    #UPDATES THE DISPLAY
    pygame.display.flip()

