import pygame, random, sys, pydoc
from pygame.locals import *

def collide(x1, x2, y1, y2, w1, w2, h1, h2):
	"""
	This is used to test if the snake is touching something
	@type x1: number
	@param x1: x cord of snake
	@type x2: number
	@param x2: x cord of snake
	@type y1: number
	@param y1: y cord of snake
	@type y2: number
	@param y2: y cord of snake
	@type w1: number
	@param w1: width of snake
	@type w2: number
	@param w2: width of snake
	@type h1: number
	@param h1: height of snake
	@type h2: number
	@param h2: height of snake
	"""
	if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:
		return True
	else:
		return False
def die(screen, score):
	"""
	Ends the game and close all windows.
	
	@type screen: pygame window
	@param screen: pygame window information
	@type score: number
	@param score: the total points aquired
	"""
	t=f.render('Your final score: '+str(score), True, (0, 0, 0))
	screen.blit(t, (10, 270))
	pygame.display.update()
	pygame.time.wait(1000)
	pygame.quit()
	sys.exit(0)

#Ininialize all starting values	
xs = [290, 290, 290, 290, 290]
ys = [290, 270, 250, 230, 210]
dirs = 0 #Direction the snake is facing: 0-down 1-right 2-up 3-left
score = 0
applepos = (random.randint(10, 580), random.randint(10, 580))
pygame.init() #Initializes pygame
s=pygame.display.set_mode((600, 600))
appleimage = pygame.Surface((10, 10))
appleimage.fill((0, 255, 0))
img = pygame.Surface((20, 20))
img.fill((255, 0, 0))
f = pygame.font.SysFont('Arial', 20)

#Clock allows the game to update smoothly
clock = pygame.time.Clock()
while True:
	clock.tick(10) #Higher = Faster
	for e in pygame.event.get():
        #Use keyevents to move the snake or quit
		#Prevents the snake from moving left if facing right
		if e.type == KEYDOWN: 
			if e.key==K_ESCAPE:
				die(s,score)
			elif e.key == K_UP and dirs != 0:
				dirs = 2
			elif e.key == K_DOWN and dirs != 2:
				dirs = 0
			elif e.key == K_LEFT and dirs != 1:
				dirs = 3
			elif e.key == K_RIGHT and dirs != 3:
				dirs = 1
	i = len(xs)-1
	#This tests if the snake runs over itself 
	while i >= 2:
		if collide(xs[0], xs[i], ys[0], ys[i], 20, 20, 20, 20):
			die(s, score)
		i-= 1
        #This tests if the snake is on the piece of food
	if collide(xs[0], applepos[0], ys[0], applepos[1], 20, 10, 20, 10):
		score+=1
		xs.append(290) #Add length to the snake
		ys.append(290) #Add length to the snake
		applepos=(random.randint(10,580),random.randint(10,580)) #Resets the apple to a new location in the screen
        #This test if the snake is out of the screen
	if xs[0] < 0 or xs[0] > 580 or ys[0] < 0 or ys[0] > 580: 
		die(s, score)
	i = len(xs)-1
	
	#Keeps the snake together
	while i >= 1:
		xs[i]=xs[i-1] #Keeps the snake head with the body in the x direction
		ys[i]=ys[i-1] #Keeps the snake head with the body in the y direction
		i-=1
		
        #moves turtle down if facing down
	if dirs==0:ys[0] += 20
        #Moves Snake right if facing right
	elif dirs==1:xs[0] += 20
	#Moves Snake up if facing up
	elif dirs==2:ys[0] -= 20
	#Moves Snake left if facing left
	elif dirs==3:xs[0] -= 20

	#Fills the snake with red coloring
	s.fill((255, 255, 255))	
	for i in range(0, len(xs)):
		s.blit(img,(xs[i],ys[i])) #Displays the snake
	s.blit(appleimage,applepos) #Displays apple at set location
	t=f.render(str(score),True,(0,0,0)) #Setup for score display
	s.blit(t, (10, 10)) #Displays the score in real time
	pygame.display.update()
