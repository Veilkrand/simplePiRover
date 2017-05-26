from SimpleUDP.SimpleUDPServer import SimpleUDPServer

server=SimpleUDPServer("",5005)

while True:
    data=server.listen(False) #True for verbose
