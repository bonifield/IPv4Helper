#!/usr/bin/python3

from ipv4helper import IPv4Helper

def printGreen(x):
	return("\033[92m"+str(x)+"\033[0m")

#i = IPv4Helper("127.144.4.9/30")
#i = IPv4Helper("127.144.1.0/29")
i = IPv4Helper("127.144.4.9/28")
#i = IPv4Helper("127.144.4.9/23")
#i = IPv4Helper("192.168.1.1")
#i = IPv4Helper("192.168.1.1/0") # don't use /0 until the next release

print("="*50)
print("Attributes")
print(printGreen("blocksize\t\t"), i.blocksize)
print(printGreen("octet\t\t\t"), i.octet)
print(printGreen("octet masked\t\t"), i.mask_octet)
print(printGreen("subnet_addresses\t"), i.subnet_addresses)
print(printGreen("usable_addresses\t"), i.usable_addresses)
print(printGreen("mask\t\t\t"), i.mask)
print(printGreen("mask_binary\t\t"), i.mask_binary)
print(printGreen("wildcard\t\t"), i.wildcard)
print(printGreen("subnet_min_ip\t\t"), i.subnet_min_ip)
print(printGreen("subnet_max_ip\t\t"), i.subnet_max_ip)
print(printGreen("subnet_min_octet\t"), i.subnet_min_octet)
print(printGreen("subnet_max_octet\t"), i.subnet_max_octet)
print(printGreen("iparg\t\t\t"), i.iparg)
print(printGreen("given_ip\t\t"), i.given_ip)
print(printGreen("given_cidr\t\t"), i.given_cidr)
print(printGreen("given_ip_first_octet\t"), i.given_ip_first_octet)
print(printGreen("given_ip_second_octet\t"), i.given_ip_second_octet)
print(printGreen("given_ip_third_octet\t"), i.given_ip_third_octet)
print(printGreen("given_ip_fourth_octet\t"), i.given_ip_fourth_octet)
print(printGreen("subnet_info\t\t"), i.subnet_info)
print(printGreen("subnet_json\t\t"), i.subnet_json)
print("="*50)
print(printGreen("subnet_summary"))
print(i.subnet_summary)
print("="*50)
print(printGreen("ip_range_generator()"))
for x in i.ip_range_generator():
	print(x)
print("="*50)
#
#
#
try:
	from ipv4mutate import IPv4Mutate
	print(printGreen("ip_range_generator() with IPv4Mutate"))
	for x in i.ip_range_generator():
		z = IPv4Mutate(x)
		print(z.mutate_hex)
	print("="*50)
except:
	pass
#
#
#
print(printGreen("octet_generator()"))
for x in i.octet_generator():
	print(x)
print("="*50)
