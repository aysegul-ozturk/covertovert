from scapy.all import IP, ICMP, send

def send_icmp():
    ip_packet = IP(dst="receiver", ttl=1)
    icmp_packet = ICMP()
    packet = ip_packet / icmp_packet
    send(packet)

if __name__ == "__main__":
    send_icmp()
