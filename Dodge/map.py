import pygame
from constants import *
from math import *
from random import randint


class Basemap():
	def __init__(self, x, y, w, h, color):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.color = color
		self.shape = pygame.Rect([self.x, self.y, self.w, self.h])
		
	def draw(self, screen):
		pygame.draw.rect(screen, self.color, self.shape)

class Ornaments():
	def __init__(self, x, y, index, color):
		self.x = x
		self.y = y
		self.index = index
		self.color = color

		self.rotation = 0
		self.speed = 2
		self.size = SIZE
		self.shapes = []

		if self.index == 3: #a bit ugly
			self.x = x + (SCREEN[0]-2*BASEWIDTH)/2 - self.size
		elif self.index == 4:
			self.y = y + self.size/2
			self.x = x + (SCREEN[0] - 2 * BASEWIDTH) / 2

	def draw(self, screen):
		if self.index == 1:
			self.shapes = [pygame.Rect([self.x, self.y, self.size, self.size]), pygame.Rect([self.x+SCREEN[0]-2*BASEWIDTH-self.size, self.y, self.size, self.size])]
			for shape in self.shapes:
				pygame.draw.rect(screen, self.color, shape)
			
		elif self.index == 2:
			self.shapes = [[[self.x, self.y], [self.x + self.size, self.y + self.size/2], [self.x, self.y + self.size]],
					 [[self.x+SCREEN[0]-2*BASEWIDTH, self.y], [self.x+SCREEN[0]-2*BASEWIDTH - self.size, self.y + self.size/2], [self.x+SCREEN[0]-2*BASEWIDTH, self.y + self.size]]]
			for shape in self.shapes:
				pygame.draw.polygon(screen, self.color, shape)

		elif self.index == 3:
			self.shapes = [pygame.Rect([self.x, self.y, self.size*2, self.size])]
			pygame.draw.rect(screen, self.color, self.shapes[0])

		elif self.index == 4:
			self.shapes = [[[self.x - self.size / 2 * sin(self.rotation), self.y - self.size / 2 * cos(self.rotation)],
					   [self.x + self.size * cos(self.rotation), self.y - self.size * sin(self.rotation)],
					   [self.x + self.size / 2 * sin(self.rotation), self.y + self.size / 2 * cos(self.rotation)]],
					  [[self.x - self.size / 2 * sin(self.rotation), self.y - self.size / 2 * cos(self.rotation)],
					   [self.x - self.size * cos(self.rotation), self.y + self.size * sin(self.rotation)],
					   [self.x + self.size / 2 * sin(self.rotation), self.y + self.size / 2 * cos(self.rotation)]]]

			for shape in self.shapes:
				pygame.draw.polygon(screen, self.color, shape)

	def event_handle(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w or event.key == pygame.K_UP:
				self.speed += 5

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_w or event.key == pygame.K_UP:
				self.speed = 2

	def update(self): #look at this, a bit ugly
		if (self.index != 4 and self.y > SCREEN[1]) or (self.index == 4 and (self.y - self.size/2) > SCREEN[1]):
			self.index = randint(1, 4)
			if self.index == 3:
				self.x = BASEWIDTH + (SCREEN[0] - 2 * BASEWIDTH) / 2 - self.size
			elif self.index == 4:
				self.x = BASEWIDTH + (SCREEN[0] - 2 * BASEWIDTH) / 2
				self.rotation = 0
			else:
				self.x = BASEWIDTH

			if self.index != 4:
				self.y = 0 - self.size
			else:
				self.y = 0 - self.size/2

		self.y += self.speed
		self.rotation += 0.05