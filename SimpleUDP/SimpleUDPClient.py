import socket
import sys
import time
# Python 2.x-3.x compatibility
try:
	import cPickle as pickle
except ImportError:
	import pickle


class SimpleUDPClient(object):

	sock = None

	def __init__(self, UDP_IP="127.0.0.1", UDP_PORT=5005, pickle_protocol=pickle.HIGHEST_PROTOCOL):
		self.UDP_IP = UDP_IP
		self.UDP_PORT = UDP_PORT
		self.pickle_protocol = pickle_protocol

		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
		except socket.error:
			print('Failed to create socket.')
			sys.exit()

	def send(self, data, verbose=False):

		if (int(time.time()*1000)%2==1):
			star = ' '
		else:
			star = '*'
		print("\r[{}] Sending to {}:{} ".format(star, self.UDP_IP, self.UDP_PORT), end="")

		if verbose:
			print(data)

		try:
			
			# inject timestamp in milliseconds
			data['timestamp'] = int(time.time() * 1000)

			_message = pickle.dumps(data, protocol=self.pickle_protocol)

			self.sock.sendto(_message, (self.UDP_IP, self.UDP_PORT))

		except socket.error as msg:
			print("Socket Error: %s" % msg)
			sys.exit()
