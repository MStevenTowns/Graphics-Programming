import pygame,pygame.camera,sys,numpy,math

def distance(x1,x2,y1,y2):
    part1=(x1-x2)*(x1-x2);
    part2=(y1-y2)*(y1-y2);
    dist=math.sqrt(part1+part2);
    return dist;

pygame.init()
pygame.camera.init()
cameras = pygame.camera.list_cameras()
w,h=640,480
try:
    cam = pygame.camera.Camera(cameras[0],(w,h))
except:
    sys.exit("No webcam found.")

cam.start()
screen = pygame.display.set_mode((w,h))
snapshot = pygame.surface.Surface((w,h))
pygame.surfarray.use_arraytype("numpy")

lastr,lastb,lastg=0,0,0
oldx,oldy=w//2-50,h-50

eye1=(w//2-50,h-50)
eye2=(w//2+50,h-50)

while 1:
    #HANDLE EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    pygame.time.wait(10)
    snapshot=cam.get_image(snapshot)
    snapshot=pygame.transform.flip(snapshot, True,False)
    snapArray = pygame.surfarray.array2d(snapshot)

    b=snapArray%256
    snapArray/=256
    g=snapArray%256
    snapArray/=256
    r=snapArray
    
    diff=numpy.abs(r-lastr)+numpy.abs(g-lastg)+numpy.abs(b-lastb)
    diff/=3
    lastb=b*1
    lastg=g*1
    lastr=r*1
    newArray=0*256**2+0*256+diff
   
    movementnum=numpy.average(diff)

    snapArray = pygame.surfarray.array2d(snapshot)
    pygame.surfarray.blit_array(snapshot, snapArray)

    m=pygame.mask.from_threshold(snapshot, (0,0,255), (30,30,210))
    masks=m.connected_components()
    holdx=[]
    holdy=[]
    for mask in masks:
        holdx+=[mask.centroid()[0]]
        holdy+=[mask.centroid()[1]]
    if len(holdx)>1:        
        holdx=int(numpy.mean(holdx))
        holdy=int(numpy.mean(holdy))
    #dist=int(distance(holdx,oldx,holdy,oldy))
    centroid=[holdx,holdy]
    try:
        pupil1=(centroid[0]-320)//10+eye1[0],(centroid[1]-240)//10+eye1[1]
        pygame.draw.circle(snapshot,(255,0,0),eye1,50)
        pygame.draw.circle(snapshot,(255,0,0),eye2,50)
        pygame.draw.circle(snapshot,(0,0,0),pupil1,15)
        pygame.draw.circle(snapshot,(0,0,0),(pupil1[0]+100,pupil1[1]),15)
    except:
        #print("bug")
        pupil1=eye1
        pygame.draw.circle(snapshot,(255,0,0),eye1,50)
        pygame.draw.circle(snapshot,(255,0,0),eye2,50)
        pygame.draw.circle(snapshot,(0,0,0),pupil1,15)
        pygame.draw.circle(snapshot,(0,0,0),(pupil1[0]+100,pupil1[1]),15)
   
    screen.blit(snapshot,(0,0))
    pygame.display.flip()
