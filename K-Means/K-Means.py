import pygame
import numpy as np
import random as rd
import sys

#data
centroid=[]
points=[]


res = (950,600)
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode(res)



# Colors
t = ((48, 213, 200)) 	# turquoise
o = ((255, 165, 0)) 	# orange
y = ((255, 204, 0))		# yellow
w = ((255, 255, 255))	# white
p = ((255, 192, 203))	# pink
g = ((211, 211, 211))	# grey
black = ((0, 0, 0))		# black
r = ((255, 0, 0))		# red
green = ((0, 255, 0)) 	# green
blue = ((0, 0, 255))	# blue


colors = [t,o,y,r,green,p,blue]

zero_font = pygame.font.SysFont('Comic Sans MS', 30)
number_font = pygame.font.SysFont('Comic Sans MS', 20)
zero_text = zero_font.render('0', False, (0, 0, 0))
word_font = pygame.font.SysFont('Comic Sans MS', 30)

while True:
		
	screen.fill((127,127,127))


	#get mouse pos
	mouse_pos=(pygame.mouse.get_pos())
	x_pos= mouse_pos[0]
	y_pos= mouse_pos[1]


	#right-hand area
	pygame.draw.rect(screen,(black),(600,0,350,600))


	#random points
	pygame.draw.rect(screen,(y),(625,50,300,50))
	screen.blit((word_font.render('Random Points', False, (0, 0, 0))),(670,55))
	
	#centroids
	pygame.draw.rect(screen,(y),(625,150,300,50))
	screen.blit((word_font.render('Centroids: '+str(len(centroid)), False, (0, 0, 0))),(690,155))
	

	#add
	pygame.draw.rect(screen,(y),(700,230,50,50))
	screen.blit((word_font.render('+', False, (0, 0, 0))),(717,230))
	
	#remove
	pygame.draw.rect(screen,(y),(800,230,50,50))
	screen.blit((word_font.render('-', False, (0, 0, 0))),(817,230))


	#update
	pygame.draw.rect(screen,(y),(650,350,250,50))
	screen.blit((word_font.render('Update', False, (0, 0, 0))),(725,350))


	#reset all
	pygame.draw.rect(screen,(y),(650,500,250,50))
	screen.blit((word_font.render('Reset All', False, (0, 0, 0))),(715,505))


	#sketch graph
	screen.blit(zero_text,(75,500))


	#sketch y-axis
	pygame.draw.line(screen,(black),(100,50),(100,550),width=1)
	for x in range(100,401,100):
		screen.blit((number_font.render(str(x), False, (0, 0, 0))),(45,485-x))

	pygame.draw.line(screen,(black),(85,100),(115,100),width=1)
	pygame.draw.line(screen,(black),(85,200),(115,200),width=1)
	pygame.draw.line(screen,(black),(85,300),(115,300),width=1)
	pygame.draw.line(screen,(black),(85,400),(115,400),width=1)
	pygame.draw.line(screen,(black),(550,50),(100,50),width=1)
	pygame.draw.line(screen,(black),(550,500),(550,50),width=1)


	#sketch x-axis
	for x in range(100,401,100):
		screen.blit((number_font.render(str(x), False, (0, 0, 0))),(x+85,515))
	
	pygame.draw.line(screen,(black),(50,500),(550,500),width=1)
	pygame.draw.line(screen,(black),(200,485),(200,515),width=1)	
	pygame.draw.line(screen,(black),(300,485),(300,515),width=1)
	pygame.draw.line(screen,(black),(400,485),(400,515),width=1)
	pygame.draw.line(screen,(black),(500,485),(500,515),width=1)



	#draw points
	for x in points:
		pygame.draw.circle(screen,black,x,7)
		pygame.draw.circle(screen,w,x,5)

	#draw centroids
	for x in range(len(centroid)):
		pygame.draw.circle(screen,black,centroid[x],12)
		pygame.draw.circle(screen,colors[int(x%7)],centroid[x],10)



	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:

			#left click
			if event.button ==1:
				#add points
				if 100<x_pos<550 and 50<y_pos<500:
					points.append(mouse_pos)

				#random points
				elif 625<x_pos<925 and 50<y_pos<100:
					points = []
					for x in range(0,rd.randint(1,20)):
						points.append((rd.randint(125,500),rd.randint(75,475)))

				#add/remove centroid
				#add
				elif 700<x_pos<750 and 230<y_pos<280:
					centroid.append((rd.randint(125,500),rd.randint(75,475)))
				
				#remove
				elif 800<x_pos<850 and 230<y_pos<280:
					centroid.pop()

				#update
				elif 650<x_pos<900 and 350<y_pos<400:
					print("Update")

				#reset all
				elif 650<x_pos<900 and 500<y_pos<550:
					centroid = []
					points = []

			#right click
			elif event.button == 3:
				if 100<x_pos<550 and 50<y_pos<500:
					centroid.append(mouse_pos)



	pygame.display.flip()
pygame.quit()