import pygame
from bisect import bisect
from pygame.locals import*
from classes.renderedObj import RenderedObject
from classes.gameIntVector import GVector
from classes.commonConsts import (artefactsTypes, WIDTHSCREEN, HEIGHTSCREEN, 
	artefactSize, artTypesTuple, artProbsTuple)
from random import random
from classes.appFunctions import generateRandomInJaggedArea

class Artefact(RenderedObject):
	"""Артефакты, которые можно собирать в инвентарь"""
	def __init__(self, focus, artType='grayball'):
		RenderedObject.__init__(self, GVector(), focus=focus)
		self.artType = artType
		if not artType in artTypesTuple:
			self.artType ='grayball'
		self.color = artefactsTypes[self.artType]['color']
		self.radius = artefactSize

	def move(self, dt):
		#если игрок слишком далеко отошел от артефакта
		if not self.initPoint.inRectangle(self.focus - GVector(WIDTHSCREEN, HEIGHTSCREEN),
			self.focus + GVector(WIDTHSCREEN, HEIGHTSCREEN) * 2):
			#переместим за пределы видимости игрока
			self.relocate()

	def draw(self, screen):
		""""""
		pygame.draw.circle(screen, self.color, self.initPoint - self.focus, self.radius)

	def relocate(self):
		"""
		Перемещает артефакт за пределы видимости игрока в случае, 
		если игрок слишком далеко отойдет или заберет артефакт в инвентарь
		"""
		self.initPoint.x = generateRandomInJaggedArea(-WIDTHSCREEN, -self.radius, 
			WIDTHSCREEN, WIDTHSCREEN * 2)
		self.initPoint.y = generateRandomInJaggedArea(-HEIGHTSCREEN, -self.radius, 
			HEIGHTSCREEN, HEIGHTSCREEN * 2)
		self.initPoint += self.focus
		self.setTypeRandomly()

	def setTypeRandomly(self):
		"""
		меняет тип артефакта на случайный, в зависимости от цены: чем дороже,
		тем ниже вероятность
		"""
		posArr = []
		curPos = 0
		for posb in artProbsTuple:
			curPos += posb
			posArr.append(curPos)

		self.artType = artTypesTuple[bisect(posArr, random())]
		self.color = artefactsTypes[self.artType]['color']