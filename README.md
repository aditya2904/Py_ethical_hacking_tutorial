# Ethical Hacking using Python.
This tutorial will help you to learn some ethical hacking using python. As a soc analyst we need to know how an attacker will perform attacks on victim machines. 

In this module we explain about the packages used in the scripts. For this you need to know some basic knowledge on python. 
I am using Kali linux for developing the code.
Changing Mac Address in kali linux
Mac address: A media access control address (MAC address) is a unique identifier assigned to a network interface controller (NIC) for use as a network address in communications within a network segment. (simply all devices in  a LAN communicate using this MAC address).

## Why to change your MAC?

In order to get access in an intranet an attacker need to spoof his MAC address. 
Initially all devices connected to an intranet will have a same subnet IP address. When an internal user need to send the information to another user this communication is made only by mac Address.

![mac](/mac.jpg)

In above example  “A “ needs to communicate to “B” . “A” need to know the mac address of “B”, “B” will send an ARP request to know the mac address for A as B knows the IP of A since they are intranet. Now the attacker plays his role when this ARP request raises the Attacker will say that the Mac address of the IP is (00:22:33:44:55:11). Hence “A “ starts to communicate to hacker. Once the Mac is linked to IP in ARP table. A won’t send the ARP request again. 

## How to change this Mac In Linux?

	- Need the check the interface that we want to change the mac.
  
	- enter ifconfig in terminal and you can see the interface.
  
	- Make that interface down and change the Mac and up the interface. This will change the mac address
  
## Py Script to change the mac address.

	- Install package “subprocess”, The  subprocess module to span new process.
  
	- Install package “regex”, this is used to check Mac address. 
  
	- Enter the interface for which you need to change the mac .
  
	- Create a function to check the mac address entered is correct or not. 
  
	- Write a script to change the mac. For this please look in to the kali_mac    _address_change.File
  [https://github.com/aditya2904/Py_ethical_hacking_tutorial/blob/master/Kali_mac_address_change]
  
Using subprocess we call the commands the we perform manually in the terminal . we use (shell=True) because we are executing shell commands
#### Parameters that we can pas in this subprocess Module 
subprocess.<function>(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)

# Network Scanner

 In this we scan all the devices which are connected to same network.
  
This can be done in multiple ways, using Nmap, netdiscover. In this we secession we learn how to write a script and take the output in CSV format. 

## ARP:

Most of the computer programs/applications use logical address (IP address) to send/receive messages, however the actual communication happens over the physical address (MAC address) i.e from layer 2 of OSI model. So our mission is to get the destination MAC address which helps in communicating with other devices. This is where ARP comes into the picture, its functionality is to translate IP address to physical address

### ARP Request: 
When a device wants to communicate to other devices in same network it will send a ARP request. 

![ARP request](https://github.com/aditya2904/Py_ethical_hacking_tutorial/blob/master/Saved%20Pictures/ARP%20request.png)


The device having this ip address only will respond to the request and send a mac address of the device this mac address will store in ARP table for further reference 

![arp response](https://github.com/aditya2904/Py_ethical_hacking_tutorial/blob/master/Saved%20Pictures/ARP%20response.png)

**In order to write a script for ARP request you should be familiar  with scapy module.**

### About Scapy

Scapy is a Python program that enables the user to send, sniff and dissect and forge network packets. This capability allows construction of tools that can probe, scan or attack networks

[https://scapy.readthedocs.io/en/latest/introduction.html]

#### Aim of this script :

	- Creating a ARP request directed to broadcast MAC address for the IP.
	- Send packet and receive the response 
	- Parse the response
	- Print the result in required format 

#### Fields that can be parsed : 

	Import scapy 
	scapy.all.ls(scapy.ARP())
*Note: you can  parse the fields in the Arp packet 

![scapyls](https://github.com/aditya2904/Py_ethical_hacking_tutorial/blob/master/Saved%20Pictures/scapyls.jpeg)

 
### Create an Arp request:
		arp_request=scapy.ARP(psdt=ip)
		ip= range of ip we are scanning 
		set destination mac to broadcast mac:
		broadcast=scapy.Either(dst="ff:ff:ff:ff:ff:ff")
 In this we selected interface as either as all mac address will be stored in this 

Now we combine these two packets in to a single packet as an Arp request 

		arp_request_broadcast=broadcast/arp_request 
*since scapy allows us to join the packets with / 

In scapy if we received any response the data will be stored as answered and no response as unanswered
We need only answered list so we create this list.

	answered_list=scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]
		- verbose = false because this won’t print the result 
		- index Zero because as the response data is stores in first and not responded stored as second in the list 
		- timeout is to set the program to wait for the response if we didn’t receive any response with in the time then move to the second one.
In this script I created an additional output which will store the data in csv format.

	
## more scripts yet to come
	
# Note: only for etnical hacking purpose.
	




