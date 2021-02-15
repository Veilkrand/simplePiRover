from SimpleUDP.SimpleUDPServer_python2 import SimpleUDPServer

server=SimpleUDPServer("",5005)

while True:
    data=server.listen(True) #True for verbose
