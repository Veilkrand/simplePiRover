import socket
import time
import sys
# Python 2.x-3.x compatibility
try:
	import cPickle as pickle
except ImportError:
	import pickle


UDP_IP = "" ## Accept all IPs
UDP_PORT = 5005

sock = None

class SimpleUDPServer(object):

	def __init__(self,UDP_IP,UDP_PORT):
		self.UDP_IP=UDP_IP
		self.UDP_PORT=UDP_PORT
		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			self.sock.bind((UDP_IP, UDP_PORT))
		except socket.error:
			print('Failed to create socket.')
			sys.exit()
		
		print "UDP Server listening on port %s" % UDP_PORT

	def listen(self,verbose=False):
		
		try :
			data, addr = self.sock.recvfrom(1024) # buffer size is 1024 bytes
		except socket.error as msg:
			print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
			sys.exit()

		inputs=pickle.loads(data)

		if (int(time.time()*1000)%2==1):
			star=' '
		else:
			star='*'

		if verbose:
			print "\r[%s] Receiving from %s-%s: %s" % (star,addr[1],addr[0], inputs),
		else:
			print "\r[%s] Receiving from %s-%s" % (star,addr[1],addr[0]),
		sys.stdout.flush()

		return inputs
