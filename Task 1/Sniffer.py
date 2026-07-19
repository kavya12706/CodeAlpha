from scapy.all import sniff, IP, TCP, UDP, DNS, DNSQR

def process_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto  
        proto_name = {6: "TCP", 17: "UDP", 1: "ICMP"}.get(proto, str(proto))

        print(f"\n[+] Packet: {src_ip} -> {dst_ip} | Protocol: {proto_name}")

        if TCP in packet:
            print(f"    Src Port: {packet[TCP].sport}  Dst Port: {packet[TCP].dport}")
        elif UDP in packet:
            print(f"    Src Port: {packet[UDP].sport}  Dst Port: {packet[UDP].dport}")
        if packet.haslayer(DNS) and packet.haslayer(DNSQR):
            try:
                queried_domain = packet[DNSQR].qname.decode()
                print(f"    [DNS Query] Domain requested: {queried_domain}")
            except Exception:
                pass

        if packet.haslayer('Raw'):
            payload = packet['Raw'].load
            print(f"    Payload (first 50 bytes): {payload[:50]}")

sniff(prn=process_packet, count=20, store=False)
