from scapy.data import TCP_SERVICES
from scapy.layers.inet import TCP, IP
from scapy.sendrecv import sr1
target = input("Please specify a target: ")
for port in range(1, 1000):
    pakiet = IP(dst=target) / TCP(dport=[port], flags="S")
    rec = sr1(pakiet, timeout=2, verbose=0)
    #print("[DEBUG] port: {}".format(port))
    if rec and rec[0].getlayer(TCP).flags == "SA":
        data = "{}".format(TCP_SERVICES[rec[0].sport])
        print("Port: {} up, Protocol = TCP, Service = {}".format(port, data))
