import socket
import time
import json
import sys, getopt
import pickle

from GameController import GameController
from SimpleUDPClient import SimpleUDPClient


def print_help():
	print('client.py -h <host> -p <port> [--verbose] [--python2]')
	sys.exit()

def main(argv):

	print("UDP Game Controller Client")

	UDP_IP = "127.0.0.1"
	#UDP_IP = "192.168.42.1"
	#UDP_IP = "136.24.116.120"
	UDP_PORT = 5005
	VERBOSE=False
	PYTHON2=False

	try:
		opts, args = getopt.getopt(argv,"h:p:yv",["host=","port=","python2","verbose"])
	except getopt.GetoptError:
		print_help()
	for opt, arg in opts:
		if opt in ("-h", "--host"):
			UDP_IP = arg
		elif opt in ("-p", "--port"):
			UDP_PORT = arg
		elif opt in ("-y", "--python2"):
			PYTHON2 = True
		elif opt in ("-v", "--verbose"):
			VERBOSE=True
	
	myGameController=GameController()

	if PYTHON2:
		myClient=SimpleUDPClient(UDP_IP, UDP_PORT,pickle_protocol=2)
	else:
		myClient=SimpleUDPClient(UDP_IP, UDP_PORT)

	while(True):
		

		# It will pickup the first game controller he finds
		inputs=myGameController.poll()
		
		myClient.send(inputs,VERBOSE)
		
		# Throttle down a little to avoid buffer overflown
		#time.sleep(0.0005)
		time.sleep(0.001)


if __name__ == '__main__':
	main(sys.argv[1:])
	
