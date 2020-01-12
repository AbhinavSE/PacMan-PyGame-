# Name : Abhinav Suresh Ennazhiyil
# Roll No.: 2018003
# Section : A
# Group : 3

import pygame
from pygame.locals import *
from numpy import loadtxt
import time
import random

# Constants for the game

WIDTH, HEIGHT = (32, 32)
COIN_COLOR = pygame.Color(255, 255, 0, 255) # RED
DOWN = [0,1]
RIGHT = [1,0]
TOP = [0,-1]
LEFT = [-1,0]
STILL = [0,0]

# Class for the monster or "ghost"

class Ghost:

	def __init__(self, images, pos):
		self.image = images
		self.position = pos
		self.isEdible = False
		self.direction = STILL
		self.state = 1
		self.possible_directions = [False, False, False, False]
		self.speed = 0.1

	# Draws the ghost onto the screen

	def draw(self, screen):
		pixels = pixels_from_points(self.position)
		screen.blit(self.image[self.state], pixels)

	# Checks if the ghost is in the cage

	def is_in_cage(self):
		return self.position[0]>5 and self.position[0]<15 and self.position[1]>9 and self.position[1]<12

	# What to do when ghost is chasing pacman

	def update_free(self):
		if round(self.position[0])+1==22 and self.direction==RIGHT:
					self.position = (-1.0,float(int(self.position[1])))
		if self.position[0]<0.5 and self.direction==LEFT:
					self.position = (20.5,float(int(self.position[1])))
		
		if round(self.position[0],2).is_integer() and round(self.position[1],2).is_integer() and not self.possible_directions == [(layout[currentLevel-1][round(self.position[1])-1][round(self.position[0])]!='w' and self.direction!=DOWN), (layout[currentLevel-1][round(self.position[1])+1][round(self.position[0])]!='w' and self.position!=(10.0, 8.0) and self.direction!=TOP), (layout[currentLevel-1][round(self.position[1])][round(self.position[0])+1]!='w' and self.direction!=LEFT), (layout[currentLevel-1][round(self.position[1])][round(self.position[0])-1]!='w' and self.direction!=RIGHT)]:
			if not self.is_in_cage():
				self.possible_directions = [(layout[currentLevel-1][round(self.position[1])-1][round(self.position[0])]!='w' and self.direction!=DOWN), (layout[currentLevel-1][round(self.position[1])+1][round(self.position[0])]!='w' and (round(self.position[0]),round(self.position[1]))!=(10, 8) and self.direction!=TOP), (layout[currentLevel-1][round(self.position[1])][round(self.position[0])+1]!='w' and self.direction!=LEFT), (layout[currentLevel-1][round(self.position[1])][round(self.position[0])-1]!='w' and self.direction!=RIGHT)]
				if self.possible_directions.count(True)>1:
					tempDir = []
					for i in range(len(self.possible_directions)):
						if self.possible_directions[i]:
							tempDir.append(i)
					level2_diff = False
					level3_diff = False
					if 0 in tempDir and round(Pacman_position[0]) == round(self.position[0]) and round(Pacman_position[1]) < round(self.position[1]):
						self.state = 0
						level2_diff = True
						level3_diff = True
					elif 1 in tempDir and round(Pacman_position[0]) == round(self.position[0]) and round(Pacman_position[1]) > round(self.position[1]):
						self.state = 1
						level2_diff = True
						level3_diff = True
					elif 2 in tempDir and ((round(Pacman_position[0]) > round(self.position[0]) and round(Pacman_position[1]) == round(self.position[1]) != 9) or (round(Pacman_position[0]) < round(self.position[0]) and round(Pacman_position[1]) == round(self.position[1]) == 9)):
						self.state = 2
						level2_diff = True
						level3_diff = True
					elif 3 in tempDir and ((round(Pacman_position[0]) < round(self.position[0]) and round(Pacman_position[1]) == round(self.position[1]) != 9) or (round(Pacman_position[0]) > round(self.position[0]) and round(Pacman_position[1]) == round(self.position[1]) == 9)):
						self.state = 3
						level2_diff = True
						level3_diff = True
					elif 0 in tempDir and 2 in tempDir and round(Pacman_position[0]) > round(self.position[0]) and round(Pacman_position[1]) < round(self.position[1]):
						level3_diff = True
						if Pacman_direction==LEFT or Pacman_direction==TOP or round(self.position[1])==9:
							self.state = 0
						else:
							self.state = 2
					elif 0 in tempDir and 3 in tempDir and round(Pacman_position[0]) < round(self.position[0]) and round(Pacman_position[1]) < round(self.position[1]):
						level3_diff = True
						if Pacman_direction==RIGHT or Pacman_direction==TOP or round(self.position[1])==9:
							self.state = 0
						else:
							self.state = 3
					elif 1 in tempDir and 2 in tempDir and round(Pacman_position[0]) > round(self.position[0]) and round(Pacman_position[1]) > round(self.position[1]):
						level3_diff = True
						if Pacman_direction==LEFT or Pacman_direction==DOWN or round(self.position[1])==9:
							self.state = 1
						else:
							self.state = 2
					elif 1 in tempDir and 3 in tempDir and round(Pacman_position[0]) < round(self.position[0]) and round(Pacman_position[1]) > round(self.position[1]):
						level3_diff = True
						if Pacman_direction==RIGHT or Pacman_direction==DOWN or round(self.position[1])==9:
							self.state = 1
						else:
							self.state = 3
					elif 0 in tempDir and 1 in tempDir:
						level3_diff = True
						if round(Pacman_position[1]) > round(self.position[1]):
							self.state = 1
						else:
							self.state = 0
					elif 2 in tempDir and 3 in tempDir:
						level3_diff = True
						if round(Pacman_position[0]) > round(self.position[0]):
							self.state = 2
						else:
							self.state = 3
					elif 0 in tempDir and round(Pacman_position[1]) < round(self.position[1]):
						level3_diff = True
						self.state = 0
					elif 1 in tempDir and round(Pacman_position[1]) > round(self.position[1]):
						level3_diff = True
						self.state = 1
					elif 2 in tempDir and round(Pacman_position[0]) > round(self.position[0]):
						level3_diff = True
						self.state = 2
					elif 3 in tempDir and round(Pacman_position[0]) < round(self.position[0]):
						level3_diff = True
						self.state = 3
					level2_diff = level2_diff and currentLevel==2 and not self.isEdible
					level3_diff = level3_diff and currentLevel==3 and not self.isEdible
					if not level2_diff and not level3_diff:
						randInd = random.randrange(0, len(tempDir))
						self.state = tempDir[randInd]

				elif  self.possible_directions.count(True)==1: 
					self.state = self.possible_directions.index(True)
				else:
					self.direction = STILL
			else:
				if round(self.position[0])<10:
					self.state = 2
				elif round(self.position[0])>10:
					self.state = 3
				else:
					self.state = 0

			if self.state==0:
				self.position = (round(self.position[0]),self.position[1])
				self.direction = TOP
			elif self.state==1:
				self.position = (round(self.position[0]),self.position[1])
				self.direction = DOWN
			elif self.state==2:
				self.position = (self.position[0],round(self.position[1]))
				self.direction = RIGHT
			else:
				self.position = (self.position[0],round(self.position[1]))
				self.direction = LEFT
		if self.isEdible:
			self.state = 4
			self.speed = 0.05
		self.position = add_to_pos(self.position, (self.direction[0]*self.speed, self.direction[1]*self.speed))

	# What to do when pacman is in cage 

	def update_cage(self):
		if round(self.position[0],2).is_integer() and round(self.position[1],2).is_integer():
			if round(self.position[1]) == 10:
				self.direction = DOWN
				self.state = 1
			else:
				self.direction = TOP
				self.state = 0  
		if self.isEdible:
			self.state = 4
			self.speed = 0.05
		self.position = add_to_pos(self.position, (self.direction[0]*self.speed, self.direction[1]*self.speed))

	# What to do when pacman collides with the enemy

	def collide_pacman(self):
		return (round(self.position[0]), round(self.position[1])) == (round(Pacman_position[0]), round(Pacman_position[1]))


# Draws the wall image

def draw_wall(screen, pos):
	pixels = pixels_from_points(pos)
	screen.blit(wall[currentLevel-1], pixels)

#Draws a pac-man image

def draw_Pacman(screen, pos, state1, state2): 
	pixels = pixels_from_points(pos)
	screen.blit(Pacman[state1][state2//5], pixels)

# Draws the lives remaining for the player

def draw_lives():
	for i in range(lives):
		draw_Pacman(screen, (16 + i, 19), 2, 0)

# Draws a circle for the coin

def draw_coin(screen, pos):
	pixels = pixels_from_points(pos)
	pygame.draw.circle(screen, COIN_COLOR, (pixels[0]+int(WIDTH/2),pixels[1]+int(HEIGHT/2)), int(WIDTH/10))

# Draws a circle for the pellet

def draw_pellet(screen, pos):
	pixels = pixels_from_points(pos)
	pygame.draw.circle(screen, COIN_COLOR, (pixels[0]+int(WIDTH/2),pixels[1]+int(HEIGHT/2)), int(WIDTH/4))

# Uitlity functions

def add_to_pos(pos, pos2):
	return (pos[0]+pos2[0], pos[1]+pos2[1])

def pixels_from_points(pos):
	return (pos[0]*WIDTH, pos[1]*HEIGHT)

# Shows the Main-Menu

def show_main_menu(): 
	global isVisible
	isReleased = [1, 1]
	isQuit = False
	if isVisible:
		pygame.mixer.music.load("data/Music/mainmenuOST.ogg")
		pygame.mixer.music.play(-1)
	while  isVisible:
		screen.blit(background, (0, 0))
		main_menu_text = myfont2.render("PAC-MAN", False, (255, 255, 255))
		button_text = [myfont1.render("START", False, (0, 0, 0)),myfont1.render("START", False, (255, 255, 255))]
		button_text1 = [myfont1.render("QUIT", False, (0, 0, 0)),myfont1.render("QUIT", False, (255, 255, 255))]
		mouse_pos = pygame.mouse.get_pos()
		mouse_click = pygame.mouse.get_pressed()[0]
		if isReleased[0]==0 and mouse_click==0:
			isVisible = False
			isReleased[0] = 1
			pygame.mixer.music.fadeout(1)
			pygame.mixer.music.load("data/Music/pacmanOST.ogg")
			pygame.mixer.music.play(-1)
		if isReleased[1]==0 and mouse_click==0:
			isQuit = True
			isReleased[1] = 1

		for event in pygame.event.get():
			if event.type == QUIT:
				exit()

		for col in range(cols):
			for row in range(rows):
				value = layout[0][row][col]
				pos = (col, row)
				if value == 'w':
					draw_wall(screen, pos)

		draw_transparent(220)
		screen.blit(main_menu_text, (230,280))
		screen.blit(button[isReleased[0]], (195,320))
		screen.blit(button_text[isReleased[0]], (300,327))
		screen.blit(button[isReleased[1]], (195,355))
		screen.blit(button_text1[isReleased[1]], (305,362))

		if 195 < mouse_pos[0] < 469 and 320 < mouse_pos[1] < 347 and mouse_click==1:
			isReleased[0] = 0
		if 195 < mouse_pos[0] < 469 and 355 < mouse_pos[1] < 382 and mouse_click==1:
			isReleased[1] = 0
		pygame.display.update()
		if isVisible or isQuit:
			if isQuit:
				exit()
		else:
			time.sleep(0.05)

# What to do when the game restarts

def restart(level, clives):
	global Pacman_direction, currentLevel, start_count, isVisible, paused_time , lives, layout, rows, cols, Pacman_position, background, score, PacState1, PacState2, Blinky, Pinky, Inky, Clyde, hasStarted, start_time, life_start_time
	pygame.mixer.music.play(-1)
	Pacman_direction = STILL  
	currentLevel = level
	isVisible = True
	lives = clives
	layout = [loadtxt('data/Map/layout.txt', dtype=str),loadtxt('data/Map/layout1.txt', dtype=str),loadtxt('data/Map/layout2.txt', dtype=str)]
	rows, cols = layout[currentLevel-1].shape
	Pacman_position = (10,15)
	background.fill((0,0,0))
	PacState1 = 2
	PacState2 = 0
	Blinky.__init__(blinkyImage, (11.0, 10.0))
	Pinky.__init__(pinkyImage, (9.0, 10.0))
	Inky.__init__(inkyImage, (7.0, 10.0))
	Clyde.__init__(clydeImage, (13.0, 10.0))
	hasStarted = False
	start_count = 0
	start_time = time.time()
	life_start_time = time.time()
	paused_time = 0

def draw_stuff():
	Blinky.draw(screen)
	Pinky.draw(screen)
	Inky.draw(screen)
	Clyde.draw(screen)
	draw_Pacman(screen, Pacman_position, PacState1, PacState2)

def draw_transparent(alpha):
	rect = pygame.Surface((672, 640))
	rect.set_alpha(alpha)
	rect.fill((0, 0, 0))
	screen.blit(rect, (0, 0))
#Initializing pygame

pygame.init()

#Initializing variables
screen = pygame.display.set_mode((672, 640), 0, 32)
background = pygame.surface.Surface((672, 640)).convert()
Pacman_direction = STILL
lives = 5
myfont = pygame.font.Font('data/Fonts/ARCADE_N.ttf', 18)
myfont1 = pygame.font.Font('data/Fonts/ARCADE_N.ttf', 12)
myfont2 = pygame.font.Font('data/Fonts/ARCADE_N.ttf', 30)
layout = [loadtxt('data/Map/layout.txt', dtype=str),loadtxt('data/Map/layout1.txt', dtype=str),loadtxt('data/Map/layout2.txt', dtype=str)]
rows, cols = layout[0].shape
Pacman_position = (10,15)
background.fill((0,0,0))
score = [0, 0, 0]
speed = 0.1
PacState1 = 2
PacState2 = 0
time_taken = [0, 0, 0]
isVisible = True
paused = False

currentLevel = 1

blinkyImage = [pygame.image.load('data/Sprites/Blinky/blinkyUp.png'),pygame.image.load('data/Sprites/Blinky/blinkyDown.png'),pygame.image.load('data/Sprites/Blinky/blinkyRight.png'),pygame.image.load('data/Sprites/Blinky/blinkyLeft.png'), pygame.image.load('data/Sprites/Blue.png')]
pinkyImage = [pygame.image.load('data/Sprites/Pinky/pinkyUp.png'),pygame.image.load('data/Sprites/Pinky/pinkyDown.png'),pygame.image.load('data/Sprites/Pinky/pinkyRight.png'),pygame.image.load('data/Sprites/Pinky/pinkyLeft.png'), pygame.image.load('data/Sprites/Blue.png')]
inkyImage = [pygame.image.load('data/Sprites/Inky/inkyUp.png'),pygame.image.load('data/Sprites/Inky/inkyDown.png'),pygame.image.load('data/Sprites/Inky/inkyRight.png'),pygame.image.load('data/Sprites/Inky/inkyLeft.png'), pygame.image.load('data/Sprites/Blue.png')]
clydeImage = [pygame.image.load('data/Sprites/Clyde/clydeUp.png'),pygame.image.load('data/Sprites/Clyde/clydeDown.png'),pygame.image.load('data/Sprites/Clyde/clydeRight.png'),pygame.image.load('data/Sprites/Clyde/clydeLeft.png'), pygame.image.load('data/Sprites/Blue.png')]

Blinky = Ghost(blinkyImage, (11.0, 10.0))
Pinky = Ghost(pinkyImage, (9.0, 10.0))
Inky = Ghost(inkyImage, (7.0, 10.0))
Clyde = Ghost(clydeImage, (13.0, 10.0)) 

hasStarted = False

button = [pygame.image.load('data/Sprites/Buttons/button.png'),pygame.image.load('data/Sprites/Buttons/button1.png')]
Pacman = [[pygame.image.load('data/Sprites/Pacman/PacManDown0.png'),pygame.image.load('data/Sprites/Pacman/PacManDown1.png'),pygame.image.load('data/Sprites/Pacman/PacMan2.png')],[pygame.image.load('data/Sprites/Pacman/PacManUp0.png'),pygame.image.load('data/Sprites/Pacman/PacManUp1.png'),pygame.image.load('data/Sprites/Pacman/PacMan2.png')],[pygame.image.load('data/Sprites/Pacman/PacManRight0.png'),pygame.image.load('data/Sprites/Pacman/PacManRight1.png'),pygame.image.load('data/Sprites/Pacman/PacMan2.png')],[pygame.image.load('data/Sprites/Pacman/PacManLeft0.png'),pygame.image.load('data/Sprites/Pacman/PacManLeft1.png'),pygame.image.load('data/Sprites/Pacman/PacMan2.png')]]
wall = [pygame.image.load('data/Sprites/Walls/wall.png'),pygame.image.load('data/Sprites/Walls/wall1.png'),pygame.image.load('data/Sprites/Walls/wall2.png')]
start_count = 0
start_time = time.time()
life_start_time = time.time()
paused_time = 0

pellet_sound = pygame.mixer.Sound("data/Music/pellet.ogg")
bite_sound = pygame.mixer.Sound("data/Music/bite.ogg")
game_over_sound = pygame.mixer.Sound("data/Music/lost.ogg")
life_lost_sound = pygame.mixer.Sound("data/Music/life.ogg")
level_sound = pygame.mixer.Sound("data/Music/level.ogg")

# Main game loop 

while True:

	# For the pacman animation
	
	if PacState2 == 15:
		PacState2 = 0
	coins_remaining = 0
	
	show_main_menu()	

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		elif event.type == KEYDOWN:
			hasStarted = True
				
	pygame.display.set_caption("PAC-MAN   LEVEL - " +  str(currentLevel))

	screen.blit(background, (0,0))

	#Draw board from the 2d layout[currentLevel-1] array.

  #In the board, '.' denote the empty space, 'w' are the walls, 'c' are the coins

	for col in range(cols):
		for row in range(rows):
			value = layout[currentLevel-1][row][col]
			pos = (col, row)
			if value == 'w':
				draw_wall(screen, pos)
			elif value == 'c':
				coins_remaining += 1
				draw_coin(screen, pos)
			elif value == 'p':
				draw_pellet(screen, pos)
	
	# when player presses any key
	if hasStarted:
		if start_count==0:
			start_time = time.time()
			life_start_time = time.time()
		elapsed_time = round(time.time() - start_time - paused_time,2)
		life_elapsed_time = round(time.time() - life_start_time,2)
		keys = pygame.key.get_pressed()
		if (keys[pygame.K_DOWN] or keys[pygame.K_s] or PacState1==0):
			PacState1 = 0
			Pacman_position = (round(Pacman_position[0]),Pacman_position[1])
			if layout[currentLevel-1][int(Pacman_position[1])+1][int(Pacman_position[0])]!='w' and (round(Pacman_position[0]),round(Pacman_position[1]))!=(10, 8):
				Pacman_direction = DOWN
			else:
				Pacman_direction = STILL
		if (keys[pygame.K_UP] or keys[pygame.K_w] or PacState1==1):
			PacState1 = 1
			Pacman_position = (round(Pacman_position[0]),Pacman_position[1])
			if layout[currentLevel-1][int(Pacman_position[1])][int(Pacman_position[0])]!='w':
				Pacman_direction = TOP
			else:
				Pacman_direction = STILL
		if (keys[pygame.K_RIGHT] or keys[pygame.K_d] or PacState1==2):
			PacState1 = 2
			Pacman_position = (Pacman_position[0],round(Pacman_position[1]))
			if round(Pacman_position[0])+1>=22:
				Pacman_position = (-1,int(Pacman_position[1]))
			if layout[currentLevel-1][int(Pacman_position[1])][int(Pacman_position[0])+1]!='w':
				Pacman_direction = RIGHT
			else:
				Pacman_direction = STILL
		if (keys[pygame.K_LEFT] or keys[pygame.K_a] or PacState1==3):
			PacState1 = 3
			Pacman_position = (Pacman_position[0],round(Pacman_position[1]))
			if Pacman_position[0]<-0.5:
				Pacman_position = (20.5,int(Pacman_position[1]))
			elif layout[currentLevel-1][int(Pacman_position[1])][int(Pacman_position[0])]!='w':
				Pacman_direction = LEFT
			else:
				Pacman_direction = STILL

		if (keys[pygame.K_ESCAPE]):
			paused = True
		
		if life_elapsed_time>20:
			Blinky.update_free()
			Pinky.update_free()
			Inky.update_free()
			Clyde.update_free()
		elif life_elapsed_time>15:
			Blinky.update_free()
			Pinky.update_free()
			Inky.update_free()
			Clyde.update_cage()
		elif life_elapsed_time>10:
			Blinky.update_free()
			Pinky.update_free()
			Inky.update_cage()
			Clyde.update_cage()
		elif life_elapsed_time>5:
			Blinky.update_free()
			Pinky.update_cage()
			Inky.update_cage()
			Clyde.update_cage()
		else:
			Blinky.update_cage()
			Pinky.update_cage()
			Inky.update_cage()
			Clyde.update_cage()
	else:
		elapsed_time = 0.0
	
	#Update player position based on movement.

	Pacman_position = add_to_pos(Pacman_position, (Pacman_direction[0]*speed, Pacman_direction[1]*speed) )
	
	#TODO: Check if player ate any coin, or collided with the wall by using the layout[currentLevel-1] array.

	# player should stop when colliding with a wall

	# coin should dissapear when eating, i.e update the layout[currentLevel-1] array
	if layout[currentLevel-1][round(Pacman_position[1])][round(Pacman_position[0])]=='c':
		pygame.mixer.Sound.play(bite_sound)
		score[currentLevel-1] += 10
		layout[currentLevel-1][round(Pacman_position[1])][round(Pacman_position[0])]='.'

	if layout[currentLevel-1][round(Pacman_position[1])][round(Pacman_position[0])]=='p':
		pygame.mixer.Sound.play(pellet_sound)
		draw_transparent(100)
		extra_score_text = myfont1.render("+50", False, (255, 255, 255))
		draw_stuff()
		temp = (round(Pacman_position[0])*WIDTH + 20, round(Pacman_position[1])*HEIGHT - 10)
		screen.blit(extra_score_text, temp)
		pygame.display.update()
		time.sleep(1.5)
		edible_start_time = time.time()
		Blinky.isEdible = True
		Pinky.isEdible = True
		Inky.isEdible = True
		Clyde.isEdible = True
		score[currentLevel-1] += 50
		layout[currentLevel-1][round(Pacman_position[1])][round(Pacman_position[0])]='.'

	if not (Blinky.isEdible or Pinky.isEdible or Inky.isEdible or Clyde.isEdible):
		edible_start_time = time.time()
	

	if Blinky.collide_pacman() or Pinky.collide_pacman() or Inky.collide_pacman() or Clyde.collide_pacman():
		if Blinky.collide_pacman() and Blinky.isEdible:
			pygame.mixer.Sound.play(pellet_sound)
			draw_transparent(100)
			extra_score_text = myfont1.render("+200", False, (255, 255, 255))
			draw_stuff()
			temp = (round(Pacman_position[0])*WIDTH + 20, round(Pacman_position[1])*HEIGHT - 10)
			screen.blit(extra_score_text, temp)
			pygame.display.update()
			time.sleep(1.5)
			score[currentLevel-1] += 200
			Blinky.__init__(blinkyImage, (11.0, 10.0))
			Blinky.speed = 0.05
		elif Pinky.collide_pacman() and Pinky.isEdible:
			pygame.mixer.Sound.play(pellet_sound)
			draw_transparent(100)
			extra_score_text = myfont1.render("+200", False, (255, 255, 255))
			draw_stuff()
			temp = (round(Pacman_position[0])*WIDTH + 20, round(Pacman_position[1])*HEIGHT - 10)
			screen.blit(extra_score_text, temp)
			pygame.display.update()
			time.sleep(1.5)
			score[currentLevel-1] += 200
			Pinky.__init__(pinkyImage, (9.0, 10.0))
			Pinky.speed = 0.05
		elif Inky.collide_pacman() and Inky.isEdible:
			pygame.mixer.Sound.play(pellet_sound)
			draw_transparent(100)
			extra_score_text = myfont1.render("+200", False, (255, 255, 255))
			draw_stuff()
			temp = (round(Pacman_position[0])*WIDTH + 20, round(Pacman_position[1])*HEIGHT - 10)
			screen.blit(extra_score_text, temp)
			pygame.display.update()
			time.sleep(1.5)
			score[currentLevel-1] += 200
			Inky.__init__(inkyImage, (7.0, 10.0))
			Inky.speed = 0.05
		elif Clyde.collide_pacman() and Clyde.isEdible:
			pygame.mixer.Sound.play(pellet_sound)
			draw_transparent(100)
			extra_score_text = myfont1.render("+200", False, (255, 255, 255))
			draw_stuff()
			temp = (round(Pacman_position[0])*WIDTH + 20, round(Pacman_position[1])*HEIGHT - 10)
			screen.blit(extra_score_text, temp)
			pygame.display.update()
			time.sleep(1.5)
			score[currentLevel-1] += 200
			Clyde.__init__(clydeImage, (13.0, 10.0))
			Clyde.speed = 0.05
		else:
			life_start_time = time.time()
			lives -= 1
			if lives == 0:
				pygame.mixer.Sound.play(game_over_sound)
				pygame.display.set_caption("PAC-MAN   GAME OVER!!!")
				time.sleep(2)
				restart(1, 5)
				score = [0, 0, 0]
			else:
				pygame.mixer.Sound.play(life_lost_sound)
				score[currentLevel-1] -= 100
				pygame.mixer.music.pause()
				draw_transparent(255)
				draw_stuff()
				draw_lives()
				pygame.display.update()
				time.sleep(2.3)
				extra_score_text = myfont1.render("  WASTED ( -100 )", False, (255, 255, 255))
				if Pacman_position[0]<10:
					temp = (round(Pacman_position[0])*WIDTH + 20, round(Pacman_position[1])*HEIGHT - 10)
				else:
					temp = (round(Pacman_position[0])*WIDTH - 210, round(Pacman_position[1])*HEIGHT - 10)
				screen.blit(extra_score_text, temp)
				pygame.display.update()
				time.sleep(2.7)
				pygame.mixer.music.unpause()
				Pacman_position = (10, 15)
				Pacman_direction = STILL
				draw_Pacman(screen, Pacman_position, PacState1, PacState2)
				Blinky.__init__(blinkyImage, (11.0, 10.0))
				Pinky.__init__(pinkyImage, (9.0, 10.0))
				Inky.__init__(inkyImage, (7.0, 10.0))
				Clyde.__init__(clydeImage, (13.0, 10.0))
	#Draw the player
	if time.time()-edible_start_time>10:
		draw_transparent(100)
		draw_stuff()
		extra_score_text = myfont1.render("BEWARE!", False, (255, 255, 255))
		temp = (round(Pacman_position[0])*WIDTH + 20, round(Pacman_position[1])*HEIGHT - 10)
		screen.blit(extra_score_text, temp)
		pygame.display.update()
		time.sleep(1.5)
		Blinky.__init__(blinkyImage, (float(round(Blinky.position[0])),float(round(Blinky.position[1]))))
		Pinky.__init__(pinkyImage, (float(round(Pinky.position[0])),float(round(Pinky.position[1]))))
		Inky.__init__(inkyImage, (float(round(Inky.position[0])),float(round(Inky.position[1]))))
		Clyde.__init__(clydeImage, (float(round(Clyde.position[0])),float(round(Clyde.position[1]))))

	draw_stuff()

	draw_lives()
	
	#Update the display
	
	paused_count = 0

	# While the game is paused

	while paused:
		pygame.mixer.music.pause()
		paused_text = myfont.render('PAUSED', False, (255, 255, 255))
		paused_text1 = myfont1.render("Press 'P' To Continue...", False, (255, 255, 255))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		keys = pygame.key.get_pressed()
		
		rect = pygame.Surface((672, 640))
		
		if paused_count==0:
			rect.set_alpha(180)
			current_paused_time = time.time()
		else:
			rect.set_alpha(0)

		rect.fill((0, 0, 0))
		screen.blit(rect, (0, 0))
		
		screen.blit(paused_text, (280, 300))
		screen.blit(paused_text1, (230, 330))
		pygame.display.update()
		if keys[pygame.K_p]:
			pygame.mixer.music.unpause()
			paused = False
			paused_time = time.time() + paused_time - current_paused_time
		time.sleep(0.05)
		paused_count += 1


	PacState2 += 1

	# When player wins the game

	if coins_remaining == 0:
		pygame.mixer.music.stop()
		pygame.mixer.Sound.play(level_sound)
		pygame.display.set_caption("PAC-MAN    YOU WON!!!")
		draw_Pacman(screen, Pacman_position, PacState1, 14)
		score[currentLevel-1] += round(1000*lives/elapsed_time)
		time_taken[currentLevel-1] = elapsed_time
		level_text = myfont.render('LEVEL ' + str(currentLevel) + " PASSED", False, COIN_COLOR)
		score_text = myfont.render('FINAL SCORE : ' + str(score[currentLevel-1]), False, (255, 255, 255))
		time_text = myfont.render('TIME : ' + str(elapsed_time), False, (255, 255, 255))
		draw_transparent(255)
		screen.blit(level_text, (200, 260))
		screen.blit(score_text, (200, 305))
		screen.blit(time_text, (200, 350))
		pygame.display.update()
		time.sleep(5)
		if not currentLevel==3:
			restart(currentLevel+1, lives)
			isVisible = False
		else:
			level_text = myfont.render('YOUR STATS', False, (255, 255, 255))
			score_text = myfont1.render('TOTAL SCORE : ' + str(score[0]) + " + " + str(score[1]) + " + " + str(score[2]) + " = " + str(score[0] + score[1] + score[2]), False, (255, 255, 255))
			time_text = myfont1.render('TOTAL TIME : ' + str(time_taken[0]) + " + " + str(time_taken[1]) + " + " + str(time_taken[2]) + " = " + str(time_taken[0] + time_taken[1] + time_taken[2]), False, (255, 255, 255))
			lives_text = myfont1.render('LIVES REMAINING : ' + str(lives), False, (255, 255, 255))
			draw_transparent(255)
			screen.blit(level_text, (200, 260))
			screen.blit(score_text, (100, 305))
			screen.blit(time_text, (100, 350))
			screen.blit(lives_text, (100, 395))
			pygame.display.update()
			time.sleep(5)
			restart(1, 5)
			score = [0, 0, 0]
			time_taken = [0, 0, 0]

	# Displays the score and time
	scoretime_text = myfont.render('SCORE : ' + str(score[currentLevel-1]) + '  TIME : ' + str(elapsed_time), False, (0, 255, 0))
	screen.blit(scoretime_text, (16,8))
	pygame.display.update()
	
	if hasStarted:
		start_count += 1
	#Wait for a while, computers are very fast.
	time.sleep(0.00008)