import socket
import time
import json
import sys
import pickle

from GameController import GameController

#UDP_IP = "127.0.0.1"
UDP_IP = "192.168.42.1"
#UDP_IP = "136.24.116.120"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

sock = None

if __name__ == '__main__':
	
	myGameController=GameController()

	print("Sending to {}:{}".format(UDP_IP,UDP_PORT))

	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	except socket.error:
	    print('Failed to create socket.')
	    sys.exit()


	while(True):
		
		inputs=myGameController.poll()
		
		
		#_message = json.dumps(inputs)
		_message = pickle.dumps(inputs)

		#print(_message, end=' ', flush=True)
		#print(_message)

		try :
			#sock.sendto(_message.encode('utf-8'), (UDP_IP, UDP_PORT))

			sock.sendto(_message, (UDP_IP, UDP_PORT))


			# receive data from client (data, addr)
			#d = sock.recvfrom(1024)
			#reply = d[0]
			#addr = d[1]

			#print('Server reply : ' + reply)

		except socket.error as msg:
			print('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
			sys.exit()

		time.sleep(0.001)
