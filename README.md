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
	
## more scripts yet to come
	
# Note: only for etnical hacking purpose.
	




