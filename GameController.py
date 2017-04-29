import pygame
from pygame.locals import QUIT, JOYBUTTONUP, JOYBUTTONDOWN, JOYAXISMOTION, JOYHATMOTION


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

	AXIS_NAMES=_AXIS_NAMES_PS4
	BUTTON_NAMES=_BUTTON_NAMES_PS4

	axis={
		0: '',
		1: '',
		2: '',
		3: '',
		4: '',
		5: ''
	}
	button={
		0: '',
		1: '',
		2: '',
		3: '',
		4: '',
		5: '',
		6: '',
		7: '',
		8: '',
		9: '',
		10: '',
		11: '',
		12: ''
	}
	hat=(0,0)

	inputs={}

	joystick=None
	joysticks=None

	axis_offset=0.05

	def init_controller(self,index):
		
		self.joystick=pygame.joystick.Joystick(index)
		self.joystick.init()
		print("'{}' selected.".format(self.joystick.get_name()))

	def poll(self):
		
		#event = pygame.event.wait()
		events = pygame.event.get()
		for event in events:
			self.process_event(event)
		return self.inputs

	def process_event(self,event):

		if event.type == JOYAXISMOTION:
			if (abs(event.value)>self.axis_offset):
				self.axis[event.axis] = round(event.value,2)
			else:
				self.axis[event.axis] = 0.0
				#print("{} = {}".format(event.axis,axis[event.axis]))
		elif event.type == JOYBUTTONDOWN:
			#print("button {} down.".format(event.button))
			self.button[event.button]=True
		elif event.type == JOYBUTTONUP:
			#print("button {} up.".format(event.button))
			self.button[event.button]=False
		elif event.type == pygame.JOYHATMOTION:
			#print("hat {}".format(event.value))
			self.hat=event.value

		self.inputs={
			'axis' : self.axis,
			'buttons' : self.button,
			'hat' : self.hat
		}

		#print(self.inputs)

	def __init__(self):
		pygame.init()
		pygame.joystick.init()
		self.joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
		print('Controllers Detected:')
		for (index,j) in enumerate(self.joysticks):
			print("{}- '{}'".format(index,j.get_name()))

		self.init_controller(0)