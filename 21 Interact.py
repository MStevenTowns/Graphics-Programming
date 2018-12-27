import pygame,pygame.camera,sys,numpy,math

'''
This tracks the user and shoots them
'''

def distance(x1,x2,y1,y2):
    part1=(x1-x2)*(x1-x2);
    part2=(y1-y2)*(y1-y2);
    dist=math.sqrt(part1+part2);
    return dist;

pygame.init()
pygame.camera.init()
cameras = pygame.camera.list_cameras()
try:
    cam = pygame.camera.Camera(cameras[0],(640,480))
except:
    sys.exit("No webcam found.")

cam.start()
screen = pygame.display.set_mode((640,480))
snapshot = pygame.surface.Surface((640,480))
pygame.surfarray.use_arraytype("numpy")

lastr,lastb,lastg=0,0,0
oldx=oldy=count=num=0
font = pygame.font.SysFont('Arial', 25)

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
        pygame.draw.lines(snapshot, (0,0,0),True,((holdx-50,holdy),(holdx+50,holdy)))
        pygame.draw.lines(snapshot, (0,0,0),True,((holdx,holdy-50),(holdx,holdy+50)))
    try:
        dist=distance(holdx,oldx,holdy,oldy)
    except:
        dist=20
    if dist<=15:
        count+=1
        if 10>count>1:
            pygame.draw.circle(snapshot, (255,0,0),(holdx,holdy),15)
            num+=1
    else: count=0
   
    oldx=holdx
    oldy=holdy
   
    screen.blit(snapshot,(0,0))
    screen.blit(font.render(str(num), True, (255,0,0)), (560, 50))
    pygame.display.flip()
