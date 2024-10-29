from scapy.all import sniff, ICMP

def process_packet(packet):
    if packet.haslayer(ICMP):
        packet.show()

def receive_icmp():
    sniff(filter="icmp", prn=process_packet)

if __name__ == "__main__":
    receive_icmp()
