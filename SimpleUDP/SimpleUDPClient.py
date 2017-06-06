import socket
import sys
import time
# Python 2.x-3.x compatibility
try:
	import cPickle as pickle
except ImportError:
	import pickle

class SimpleUDPClient(object):
	
	UDP_IP = "127.0.0.1"
	#UDP_IP = "192.168.42.1"
	#UDP_IP = "136.24.116.120"
	UDP_PORT = 5005

	sock=None

	def __init__(self, UDP_IP, UDP_PORT,pickle_protocol=3):
		self.UDP_IP=UDP_IP
		self.UDP_PORT=UDP_PORT
		self.pickle_protocol=pickle_protocol

		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
		except socket.error:
			print('Failed to create socket.')
			sys.exit()

	def send(self,data,verbose=False):

		if (int(time.time()*1000)%2==1):
			star=' '
		else:
			star='*'	
		print("\r[{}] Sending to {}:{} ".format(star,self.UDP_IP,self.UDP_PORT), end="")

		if verbose:
			print(data)

		try :
			
			# inject timestamp in milliseconds
			data['timestamp']=time.time() * 1000


			#Downgrade protocol to be compatible to python 2.x
			_message = pickle.dumps(data,protocol=self.pickle_protocol)
			#_message = str(data['buttons'][0]).encode('utf-8')

			self.sock.sendto(_message, (self.UDP_IP, self.UDP_PORT))

			# receive data from client (data, addr)
			#d = sock.recvfrom(1024)
			#reply = d[0]
			#addr = d[1]

			#print('Server reply : ' + reply)

		except socket.error as msg:
			print("Socket Error: %s" % msg)
			sys.exit()
