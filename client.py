import time
import sys
import getopt

from GameController.GameController import GameController
from SimpleUDP.SimpleUDPClient import SimpleUDPClient

def print_help():
	print('client.py -h <host> -p <port> [--verbose]')
	sys.exit()

def main(argv):

	print("UDP Game Controller Client")

	POLL_INTERVAL = 0.03
	UDP_IP = "127.0.0.1"
	UDP_PORT = 5005
	VERBOSE = False

	try:
		opts, args = getopt.getopt(argv, "h:p:yv", ["host=", "port=", "python2", "verbose"])
	except getopt.GetoptError:
		print_help()

	for opt, arg in opts:
		if opt in ("-h", "--host"):
			UDP_IP = arg
		elif opt in ("-p", "--port"):
			UDP_PORT = arg
		elif opt in ("-v", "--verbose"):
			VERBOSE=True
	
	myGameController=GameController()

	myClient=SimpleUDPClient(UDP_IP, UDP_PORT)

	while True:

		# It will pickup the first game controller he finds
		inputs = myGameController.poll()
		
		myClient.send(inputs, VERBOSE)
		
		# Throttle down a little to avoid buffer overflown

		time.sleep(POLL_INTERVAL)


if __name__ == '__main__':
	main(sys.argv[1:])
