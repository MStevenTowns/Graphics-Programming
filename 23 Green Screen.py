import pygame
import pygame.camera
import sys
import numpy

#START PYGAME
pygame.init()

#START THE CAMERA MODULE OF PYGAME
pygame.camera.init()

#GET A LIST OF ALL WEBCAMS
cameras = pygame.camera.list_cameras()

#CONNECT TO A WEBCAM IF YOU CAN
try:
    cam = pygame.camera.Camera(cameras[0],(640,480))
except:
    sys.exit("No webcam found.")

#START THE WEBCAM
cam.start()



#INITIALIZE THE MAIN WINDOW OF YOUR PROGRAM
screen = pygame.display.set_mode((640,480))#,pygame.FULLSCREEN)

#INITIALIZE A SURFACE TO TAKE WEBCAM SNAPSHOTS ON
snapshot = pygame.surface.Surface((640,480))

cam.get_image(snapshot)
pygame.time.wait(2000)
cam.get_image(snapshot)
snapshot=pygame.transform.flip(snapshot, True,False)
snapArray = pygame.surfarray.array2d(snapshot)
 
b2=snapArray%256
snapArray=snapArray/256
g2=snapArray%256
snapArray/=256
r2=snapArray

#THIS LETS USE NUMPY ON OUR ARRAYS
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

    #WAIT TO KEEP FROM "SNAGGING" THE WEBCAM
    pygame.time.wait(10)

    #GRAB WEBCAM IMAGE
    cam.get_image(snapshot)

    #DO A HORIZONTAL AND/OR VERTICAL FLIP
    snapshot=pygame.transform.flip(snapshot, True,False)

    #GET ARRAY OF WEBCAM IMAGE
    snapArray = pygame.surfarray.array2d(snapshot)
 
    b=snapArray%256
    snapArray=snapArray/256
    g=snapArray%256
    snapArray/=256
    r=snapArray

    diff_map=((abs(r-r2)+abs(g-g2)+abs(b-b2))/3)>50
    
    r*=diff_map
    g*=diff_map
    b*=diff_map
    
    background_map=1-diff_map
    
    newArray=r+g+b
        
    #DRAW ARRAY ON SNAPSHOT SURFACE
    pygame.surfarray.blit_array(snapshot, newArray)

    #DRAW SNAPSHOT ON THE DISPLAY
    screen.blit(snapshot,(0,0))    

    #UPDATES THE DISPLAY
    pygame.display.flip()
