# Task 1 - Basic Network Sniffer

Built a Python script to capture live packets and show info like IPs, 
protocol, and payload.

## Tools
- Python 3, Scapy
- Kali Linux (VirtualBox)

## Steps
1. Checked if scapy was installed using  
`python3 -c "import scapy; print(scapy.__version__)"`

2. if not, install it using
`sudo pip3 install scapy --break-system-packages`

3. Wrote sniffer.py using 
`nano sniffer.py`
after typing python code, save using ctrl+O, enter, exit using ctrl+X

4. Ran it with 
`sudo python3 sniffer.py`

5. Generated traffic in another terminal using ping, curl, and browsing
eg: `ping cylabacademy.org`

## Sample output

**DNS query**
```
[+] Packet: 10.0.2.15 -> 192.168.0.1 | Protocol: UDP
Src Port: 58127  Dst Port: 53
[DNS Query] Domain requested: google.com.
```

**ICMP (ping)**
```
[+] Packet: 10.0.2.15 -> 142.250.207.78 | Protocol: ICMP
Payload (first 50 bytes): b'r\xc9\\j\x00\x00\x00\x00...\x10\x11\x12\x13...'
```

**HTTP (plaintext, from curl)**
```
[+] Packet: 10.0.2.15 -> 104.20.23.154 | Protocol: TCP
Src Port: 40678  Dst Port: 80
Payload (first 50 bytes): b'GET / HTTP/1.1\r\nHost: example.com\r\nUser-Agent: cur'
```

**HTTPS (encrypted, from browsing)**
```
[+] Packet: 10.0.2.15 -> 160.79.104.10 | Protocol: TCP
Src Port: 37208  Dst Port: 443
Payload (first 50 bytes): b'\x17\x03\x03\x00"\xf53v\xf4\xf7...'
```

## My Takeaways
- Domain name only shows up in the DNS packet, everything after that uses 
just the IP
- Port tells you the type of traffic - 53 = DNS, 80 = HTTP, 443 = HTTPS
- Readable payload = not encrypted, random bytes = encrypted
