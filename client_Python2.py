import socket
import time
import json
import sys
import pickle

from GameController import GameController
from SimpleUDPClient import SimpleUDPClient

#UDP_IP = "127.0.0.1"
UDP_IP = "192.168.42.1"
#UDP_IP = "136.24.116.120"
UDP_PORT = 5005

if __name__ == '__main__':
	
	print("UDP Game Controller Client")

	myGameController=GameController()

	myClient=SimpleUDPClient(UDP_IP, UDP_PORT,pickle_protocol=2)


	while(True):
		
		# It will pickup the first game controller he finds
		inputs=myGameController.poll()
		
		myClient.send(inputs,False)
		
		# Throttle down a little to avoid buffer overflown
		#time.sleep(0.0005)
		time.sleep(0.001)
