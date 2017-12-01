### Socket Programming in Python
# https://pythontips.com/2013/08/06/python-socket-network-programming/
# Also contibuted to:
# http://www.geeksforgeeks.org/socket-programming-python/


# Here is an example of a script for connecting to Google:

import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket successfully created."
except socket.error as err:
    print "Socket creation failed with error %s." %(err)

# Default port for the socket:
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print "There was a problem resolving the host."
    sys.exit()

# Connect to the server:
s.connect((host_ip, port))

print "The socket has successfully connected to Google on port == % s." \
    %(host_ip)
