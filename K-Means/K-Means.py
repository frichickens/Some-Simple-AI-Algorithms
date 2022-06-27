import pygame
import numpy as np
import random as rd
import sys


data=[]

clusters=[]

points=[]
groups = 0
x= rd.randint(500,2000)
print(x)



res = (950,600)
pygame.init()
screen = pygame.display.set_mode(res)



# Colors
t = ((48, 213,200)) # turquoise
o = ((255, 165, 0)) # orange
y = ((255, 255, 0)) # yellow

w = ((255, 255, 255)) # white
p = ((255, 192, 203)) # pink
g = ((211,211,211)) #grey
black = ((0, 0, 0))

r = ((255, 0, 0)) # red
g = ((0, 255, 0)) # green
blue = ((0,0,255))


colors = [t,o,y,r,g,w,p,g,black,blue]

while True:
		
	screen.fill((127,127,127))



	mouse_pos=(pygame.mouse.get_pos())
	x_pos= mouse_pos[0]
	y_pos= mouse_pos[1]

	pygame.draw.rect(screen,(blue),(700,0,50,30))
	




	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			print(mouse_pos)
			






	pygame.display.flip()

pygame.quit()