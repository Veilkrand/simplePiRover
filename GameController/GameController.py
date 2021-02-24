import time

import pygame
#from pygame.locals import QUIT, JOYBUTTONUP, JOYBUTTONDOWN, JOYAXISMOTION, JOYHATMOTION
from pygame.locals import *

class GameController:

	_AXIS_NAMES_PS4 = {
	    0 : 'LEFT_X',
	    1 : 'LEFT_Y',
	    2 : 'RIGHT_X',
	    3 : 'RIGHT_Y',
	    4 : 'L2',
	    5 : 'R2'    
	}

	_BUTTON_NAMES_PS4 = {
	    0 : 'SQUARE',
	    1 : 'CROSS',
	    2 : 'CIRCLE',
	    3 : 'TRIANGLE',
	    4 : 'L1',
	    5 : 'R2',
	    6 : 'L2',
	    7 : 'R2',
	    8 : 'SHARE',
	    9 : 'OPTIONS',
	   10 : 'L3',
	   11 : 'R4',
	   12 : 'PS'
	}

	AXIS_NAMES = _AXIS_NAMES_PS4
	BUTTON_NAMES = _BUTTON_NAMES_PS4

	axis = {
		0: 0.0,
		1: 0.0,
		2: 0.0,
		3: 0.0,
		4: 0.0,
		5: 0.0
	}
	button = {
		0: False,
		1: False,
		2: False,
		3: False,
		4: False,
		5: False,
		6: False,
		7: False,
		8: False,
		9: False,
		10: False,
		11: False,
		12: False
	}
	hat = (0, 0)

	inputs = {
			'axis': axis,
			'buttons': button,
			'hat': hat
	}

	joystick = None
	joysticks = None

	axis_offset = 0.05

	def init_controller(self, index):
		
		self.joystick = pygame.joystick.Joystick(index)
		self.joystick.init()
		print("'{}' selected.".format(self.joystick.get_name()))

	def poll(self):
		
		#event = pygame.event.wait()
		events = pygame.event.get()
		for event in events:
			self.process_event(event)
		return self.inputs

	def process_event(self, event):

		if event.type == JOYAXISMOTION:
			if abs(event.value)>self.axis_offset:
				self.axis[event.axis] = round(event.value, 2)
			else:
				self.axis[event.axis] = 0.0

		elif event.type == JOYBUTTONDOWN:

			self.button[event.button] = True
		elif event.type == JOYBUTTONUP:
			self.button[event.button]=False
		elif event.type == pygame.JOYHATMOTION:
			self.hat = event.value

		self.inputs = {
			'axis': self.axis,
			'buttons': self.button,
			'hat': self.hat,
		}

	def __init__(self):
		pygame.init()
		pygame.joystick.init()

		print('Connect your controller now...')
		while pygame.joystick.get_count() == 0:
			time.sleep(0.5)
			pygame.joystick.quit()
			pygame.joystick.init()

		self.joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

		if len(self.joysticks) > 0:
			print('Controllers Detected:')
			for (index,j) in enumerate(self.joysticks):
				print("{}: '{}'".format(index, j.get_name()))
			self.init_controller(0)
		else:
			print("No controllers detected.")

