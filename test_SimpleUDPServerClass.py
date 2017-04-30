from SimpleUDPServer import SimpleUDPServer

server=SimpleUDPServer("",5005)

while True:
    data=server.listen(True) #True for verbose
