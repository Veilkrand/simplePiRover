from SimpleUDP.SimpleUDPServer import SimpleUDPServer

if __name__ == "__main__":
    server = SimpleUDPServer("", 5005)
    while True:
        # True for verbose
        data = server.listen(False)
