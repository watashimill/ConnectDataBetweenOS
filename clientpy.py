#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import os

s = 58.9.133.149        # Create a socket object
host = socket.gethostname() # Get local machine name
port = 8888                # Reserve a port for your service.

print host
s.connect((host, port))
print s.recv(1024)
s.close                     # Close the socket when done
os.system("pause")