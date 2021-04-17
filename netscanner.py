import scapy.all as scapy
import optparse
import os

os.system("apt install figlet")
os.system("clear")
os.system("figlet Sphinx")
def get_user_input():
	parse_object = optparse.OptionParser()
	parse_object.add_option("-i","--ip",dest="ip_adress",help="Enter Ip Adress")

	(user_input,arguments) = parse_object.parse_args()

	if not user_input.ip_adress:
		print("Enter Ip Adress")
	return user_input

def scan_my_network(ip):
	arp_request_packet = scapy.ARP(pdst="192.168.38.128/24")
	broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	combined_packet = broadcast_packet/arp_request_packet
	(answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1)
	answered_list.summary()

user_ip_adress = get_user_input()
scan_my_network(user_ip_adress.ip_adress)
