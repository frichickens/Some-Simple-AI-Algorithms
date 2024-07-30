import pygame	
import numpy as np
import sys	

#data	
points = []	
sketch = 0	

res = (950,600)	
pygame.init()	
pygame.font.init()	
screen = pygame.display.set_mode(res)	


#colors
green = (144,238,144)	
blue = (45,100,245)	
red = (202,0,42)	
black = (0,0,0)	
white = (245,245,245)	
grey = (64,64,64)	
orange = (255,165,0)	

#fonts	
word_font = pygame.font.SysFont('Comic Sans MS', 25)	
number_font = pygame.font.SysFont('Arial', 10)	


# calculation

def coefficients(points):	
    x_cord = []	
    y_cord = []	
   
   	# number of points	
    n = len(points)	
    for i in range(n):	
        x_cord.append(points[i][0])	
        y_cord.append(points[i][1])	
    
    x_cord = np.array(x_cord)	
    y_cord = np.array(y_cord)
    
    # First method
    X = np.array([x_cord]).T
    Y = np.array([y_cord]).T
    
    one = np.ones((X.shape[0],1))
    Xbar = np.concatenate((one, X), axis = 1)
    a = np.dot(Xbar.T, Xbar)
    b = np.dot(Xbar.T, Y)
    w = np.dot(np.linalg.pinv(a), b)
    
    # Second Method
 	# mean x and mean y	
    mean_x = np.mean(x_cord)	
    mean_y = np.mean(y_cord)	

 	# cross-deviation and deviation of x	
    xy = np.sum(y_cord*x_cord) - n*mean_x*mean_y	
    xx = np.sum(x_cord*x_cord) - n*mean_x*mean_x	


 	# y = ax + b	
    a = xy/xx	
    b = mean_y - a*mean_x	
    
    #return(a,b)
    return(w[1][0],w[0][0])	




# sketch_line	
# because pygame dont support sketching graph 	
# so i will calculate where the line cut x axis and y axis 
# then decide how to sketch the line	

def sketch_linear(a,b):	
	if(100<=(100-b)/a<=650) and (100<=a*100+b<=500):	
		pygame.draw.line(screen,(red),(100,100*a+b),((100-b)/a,100),width=2)	
	elif(100<=(500-b)/a<=650) and (100<=a*100+b<=500):	
		pygame.draw.line(screen,(red),(100,100*a+b),((500-b)/a,500),width=2)	
	elif(100<=(500-b)/a<=650) and (100<=650*a+b<=500):	
		pygame.draw.line(screen,(red),(650,650*a+b),((500-b)/a,500),width=2)	
	elif(100<=(100-b)/a<=650) and (100<=650*a+b<=500):	
		pygame.draw.line(screen,(red),((100-b)/a,100),(650,650*a+b),width=2)	
	elif(100<=(100-b)/a<=650) and (100<=(500-b)/a<=650):	
		pygame.draw.line(screen,(red),((100-b)/a,100),((500-b)/a,500),width=2)	
	else:	
		pygame.draw.line(screen,(red),(100,100*a+b),(650,650*a+b),width=2)	


while True:	

	screen.fill(white)	


	#get mouse position	
	mouse_pos=(pygame.mouse.get_pos())	
	x_pos= mouse_pos[0]	
	y_pos= mouse_pos[1]	


	#sketch x-axis	
	for x in range(0,6):	
		screen.blit((number_font.render(str(x*20), False, (0, 0, 0))),(30,500-83*x))	
		pygame.draw.line(screen,(black),(50,500-83*x),(45,500-83*x),width=1)	
	pygame.draw.line(screen,(black),(50,550),(700,550),width=1)	
	screen.blit((word_font.render('X', False, (0, 0, 0))),(380,550))	



	pygame.draw.line(screen,(black),(50,50),(700,50),width=1)	
	pygame.draw.line(screen,(black),(700,50),(700,550),width=1)	



	#sketch y-axis	
	for x in range(0,8):	
		screen.blit((number_font.render(str(x*20), False, (0, 0, 0))),(100+83*x,560))	
		pygame.draw.line(screen,(black),(100+83*x,550),(100+83*x,555),width=1)	
	pygame.draw.line(screen,(black),(50,550),(50,50),width=1)	
	screen.blit((word_font.render('Y', False, (0, 0, 0))),(25,275))	



	#button area	
	pygame.draw.rect(screen,(grey),(750,0,200,600))	


	#random	
	pygame.draw.rect(screen,(green),(775,350,150,50))	
	screen.blit((word_font.render('Clear', False, (0, 0, 0))),(810,350))	

	#sketch	
	pygame.draw.rect(screen,(green),(775,450,150,50))	
	screen.blit((word_font.render('Sketch', False, (0, 0, 0))),(800,450))	

	#words	
	screen.blit((word_font.render('"Left click ', False, (0, 0, 0))),(775,50))	
	screen.blit((word_font.render('to create ', False, (0, 0, 0))),(785,100))	
	screen.blit((word_font.render('points"', False, (0, 0, 0))),(800,150))	
	screen.blit((word_font.render('"Right click ', False, (0, 0, 0))),(775,200))	
	screen.blit((word_font.render('to remove ', False, (0, 0, 0))),(785,250))	
	screen.blit((word_font.render('lastest"', False, (0, 0, 0))),(800,300))	



	#draw points	
	for x in points:	
		pygame.draw.circle(screen,black,x,4)	
		pygame.draw.circle(screen,blue,x,3)	

	#draw graph	
	if sketch!=0:	
		sketch_linear(a,b)


	for event in pygame.event.get():	


		#quit	
		if event.type == pygame.QUIT:	
			pygame.quit()	
			sys.exit()	

		#mouse click	
		if event.type == pygame.MOUSEBUTTONDOWN:	

			#left click	
			if event.button ==1:	

				#add points	
				if 50<x_pos<700 and 50<y_pos<550 and sketch==0:	
					points.append((x_pos,y_pos))	

				#clear	
				elif 775<x_pos<925 and 350<y_pos<400:	
					points = []	
					sketch = 0	

				#sketch	
				elif 775<x_pos<925 and 450<y_pos<500 and sketch==0 and len(points)>1:	
					a,b = coefficients(points)	
					sketch += 1	


			elif event.button == 3 and len(points)>0 and sketch==0:	
				points.pop()	



	pygame.display.flip()	
pygame.quit()	