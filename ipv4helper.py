# usage:  from ipv4helper import IPv4Helper
# instantiate a CIDR, ex.  i = IPv4Helper("127.144.1.0/29")

import json

class IPv4Helper():
	def __init__(self, iparg=None):
		""" initialize object and set attributes """
		self.iparg = str(iparg)
		if "/" not in self.iparg:
			self.iparg = self.iparg+"/32"
		self.given_ip = str(self.iparg.split('/')[0])
		self.given_cidr = int(self.iparg.split('/')[1])
		self.given_ip_first_octet = int(self.given_ip.split('.')[0])
		self.given_ip_second_octet = int(self.given_ip.split('.')[1])
		self.given_ip_third_octet = int(self.given_ip.split('.')[2])
		self.given_ip_fourth_octet = int(self.given_ip.split('.')[3])
		self.subnets = {
			0:{"cidr":"0", "mask_binary":"00000000", "mask":"0.0.0.0", "subnet_addresses":4294967296, "usable_addresses":4294967294, "wildcard":"255.255.255.255", "blocksize":1, "octet":1, "mask_octet":4},
			1:{"cidr":"1", "mask_binary":"10000000", "mask":"128.0.0.0", "subnet_addresses":2147483648, "usable_addresses":2147483646, "wildcard":"127.255.255.255", "blocksize":128, "octet":1, "mask_octet":4},
			2:{"cidr":"2", "mask_binary":"11000000", "mask":"192.0.0.0", "subnet_addresses":1073741824, "usable_addresses":1073741822, "wildcard":"63.255.255.255", "blocksize":64, "octet":1, "mask_octet":4},
			3:{"cidr":"3", "mask_binary":"11100000", "mask":"224.0.0.0", "subnet_addresses":536870912, "usable_addresses":536870910, "wildcard":"31.255.255.255", "blocksize":32, "octet":1, "mask_octet":4},
			4:{"cidr":"4", "mask_binary":"11110000", "mask":"240.0.0.0", "subnet_addresses":268435456, "usable_addresses":268435454, "wildcard":"15.255.255.255", "blocksize":16, "octet":1, "mask_octet":4},
			5:{"cidr":"5", "mask_binary":"11111000", "mask":"248.0.0.0", "subnet_addresses":134217728, "usable_addresses":134217726, "wildcard":"7.255.255.255", "blocksize":8, "octet":1, "mask_octet":4},
			6:{"cidr":"6", "mask_binary":"11111100", "mask":"252.0.0.0", "subnet_addresses":67108864, "usable_addresses":67108862, "wildcard":"3.255.255.255", "blocksize":4, "octet":1, "mask_octet":4},
			7:{"cidr":"7", "mask_binary":"11111110", "mask":"254.0.0.0", "subnet_addresses":33554432, "usable_addresses":33554430, "wildcard":"1.255.255.255", "blocksize":2, "octet":1, "mask_octet":4},
			8:{"cidr":"8", "mask_binary":"11111111", "mask":"255.0.0.0", "subnet_addresses":16777216, "usable_addresses":16777214, "wildcard":"0.255.255.255", "blocksize":1, "octet":1, "mask_octet":4},
			9:{"cidr":"9", "mask_binary":"10000000", "mask":"255.128.0.0", "subnet_addresses":8388608, "usable_addresses":8388606, "wildcard":"0.127.255.255", "blocksize":128, "octet":2, "mask_octet":3},
			10:{"cidr":"10", "mask_binary":"11000000", "mask":"255.192.0.0", "subnet_addresses":4194304, "usable_addresses":4194302, "wildcard":"0.63.255.255", "blocksize":64, "octet":2, "mask_octet":3},
			11:{"cidr":"11", "mask_binary":"11100000", "mask":"255.224.0.0", "subnet_addresses":2097152, "usable_addresses":2097150, "wildcard":"0.31.255.255", "blocksize":32, "octet":2, "mask_octet":3},
			12:{"cidr":"12", "mask_binary":"11110000", "mask":"255.240.0.0", "subnet_addresses":1048576, "usable_addresses":1048574, "wildcard":"0.15.255.255", "blocksize":16, "octet":2, "mask_octet":3},
			13:{"cidr":"13", "mask_binary":"11111000", "mask":"255.248.0.0", "subnet_addresses":524288, "usable_addresses":524286, "wildcard":"0.7.255.255", "blocksize":8, "octet":2, "mask_octet":3},
			14:{"cidr":"14", "mask_binary":"11111100", "mask":"255.252.0.0", "subnet_addresses":262144, "usable_addresses":262142, "wildcard":"0.3.255.255", "blocksize":4, "octet":2, "mask_octet":3},
			15:{"cidr":"15", "mask_binary":"11111110", "mask":"255.254.0.0", "subnet_addresses":131072, "usable_addresses":131070, "wildcard":"0.1.255.255", "blocksize":2, "octet":2, "mask_octet":3},
			16:{"cidr":"16", "mask_binary":"11111111", "mask":"255.255.0.0", "subnet_addresses":65536, "usable_addresses":65534, "wildcard":"0.0.255.255", "blocksize":1, "octet":2, "mask_octet":3},
			17:{"cidr":"17", "mask_binary":"10000000", "mask":"255.255.128.0", "subnet_addresses":32768, "usable_addresses":32766, "wildcard":"0.0.127.255", "blocksize":128, "octet":3, "mask_octet":2},
			18:{"cidr":"18", "mask_binary":"11000000", "mask":"255.255.192.0", "subnet_addresses":16384, "usable_addresses":16382, "wildcard":"0.0.63.255", "blocksize":64, "octet":3, "mask_octet":2},
			19:{"cidr":"19", "mask_binary":"11100000", "mask":"255.255.224.0", "subnet_addresses":8192, "usable_addresses":8190, "wildcard":"0.0.31.255", "blocksize":32, "octet":3, "mask_octet":2},
			20:{"cidr":"20", "mask_binary":"11110000", "mask":"255.255.240.0", "subnet_addresses":4096, "usable_addresses":4094, "wildcard":"0.0.15.255", "blocksize":16, "octet":3, "mask_octet":2},
			21:{"cidr":"21", "mask_binary":"11111000", "mask":"255.255.248.0", "subnet_addresses":2048, "usable_addresses":2046, "wildcard":"0.0.7.255", "blocksize":8, "octet":3, "mask_octet":2},
			22:{"cidr":"22", "mask_binary":"11111100", "mask":"255.255.252.0", "subnet_addresses":1024, "usable_addresses":1022, "wildcard":"0.0.3.255", "blocksize":4, "octet":3, "mask_octet":2},
			23:{"cidr":"23", "mask_binary":"11111110", "mask":"255.255.254.0", "subnet_addresses":512, "usable_addresses":510, "wildcard":"0.0.1.255", "blocksize":2, "octet":3, "mask_octet":2},
			24:{"cidr":"24", "mask_binary":"11111111", "mask":"255.255.255.0", "subnet_addresses":256, "usable_addresses":254, "wildcard":"0.0.0.255", "blocksize":1, "octet":3, "mask_octet":2},
			25:{"cidr":"25", "mask_binary":"10000000", "mask":"255.255.255.128", "subnet_addresses":128, "usable_addresses":126, "wildcard":"0.0.0.127", "blocksize":128, "octet":4, "mask_octet":1},
			26:{"cidr":"26", "mask_binary":"11000000", "mask":"255.255.255.192", "subnet_addresses":64, "usable_addresses":62, "wildcard":"0.0.0.63", "blocksize":64, "octet":4, "mask_octet":1},
			27:{"cidr":"27", "mask_binary":"11100000", "mask":"255.255.255.224", "subnet_addresses":32, "usable_addresses":30, "wildcard":"0.0.0.31", "blocksize":32, "octet":4, "mask_octet":1},
			28:{"cidr":"28", "mask_binary":"11110000", "mask":"255.255.255.240", "subnet_addresses":16, "usable_addresses":14, "wildcard":"0.0.0.15", "blocksize":16, "octet":4, "mask_octet":1},
			29:{"cidr":"29", "mask_binary":"11111000", "mask":"255.255.255.248", "subnet_addresses":8, "usable_addresses":6, "wildcard":"0.0.0.7", "blocksize":8, "octet":4, "mask_octet":1},
			30:{"cidr":"30", "mask_binary":"11111100", "mask":"255.255.255.252", "subnet_addresses":4, "usable_addresses":2, "wildcard":"0.0.0.3", "blocksize":4, "octet":4, "mask_octet":1},
			31:{"cidr":"31", "mask_binary":"11111110", "mask":"255.255.255.254", "subnet_addresses":2, "usable_addresses":0, "wildcard":"0.0.0.1", "blocksize":2, "octet":4, "mask_octet":1},
			32:{"cidr":"32", "mask_binary":"11111111", "mask":"255.255.255.255", "subnet_addresses":1, "usable_addresses":1, "wildcard":"0.0.0.0", "blocksize":1, "octet":4, "mask_octet":1}
		}
		self.subnet_addresses = self.subnet_addresses()
		self.usable_addresses = self.usable_addresses()
		self.blocksize = self.blocksize()
		self.cidr = self.cidr()
		self.mask = self.mask()
		self.mask_binary = self.mask_binary()
		self.mask_octet = self.mask_octet()
		self.wildcard = self.wildcard()
		self.octet = self.octet()
		self.subnet_info = self.subnet_min_max_calc()
		self.subnet_json = json.dumps(self.subnet_info)
		self.subnet_min_ip = self.subnet_info["ip_range_min"]
		self.subnet_max_ip = self.subnet_info["ip_range_max"]
		self.subnet_min_octet = self.subnet_info["min_octet"]
		self.subnet_max_octet = self.subnet_info["max_octet"]
		self.subnet_summary = self.subnet_summary()

	def subnet_summary(self):
		""" returns content for subnet_summary """
		c = self.given_cidr
		s = "{}\n".format(self.iparg)
		s += str("%-20s" % "CIDR" + "\t" + str("%-20s" % self.subnets[c]["cidr"]) + "\n")
		s += str("%-20s" % "Mask" + "\t" + str("%-20s" % self.subnets[c]["mask"]) + "\n")
		s += str("%-20s" % "Binary Mask" + "\t" + str("%-20s" % self.subnets[c]["mask_binary"]) + "\n")
		s += str("%-20s" % "Range" + "\t" + str("%-40s" % str(self.subnet_min_ip + " - " + self.subnet_max_ip) + "\n"))
		s += str("%-20s" % "Blocksize" + "\t" + str("%-20s" % self.subnets[c]["blocksize"]) + "\n")
		s += str("%-20s" % "Subnet Addresses" + "\t" + str("%-20s" % self.subnets[c]["subnet_addresses"]) + "\n")
		s += str("%-20s" % "Usable Addresses" + "\t" + str("%-20s" % self.subnets[c]["usable_addresses"]) + "\n")
		s += str("%-20s" % "ACL Wildcard" + "\t" + str("%-20s" % self.subnets[c]["wildcard"]) + "\n")
		s += str("%-20s" % "Octet Incremented" + "\t" + str("%-20s" % self.subnets[c]["octet"]) + "\n")
		s += str("%-20s" % "Octet Masked" + "\t" + str("%-20s" % self.subnets[c]["mask_octet"]))
		return(s)

	def subnet_addresses(self):
		""" returns content for subnet_addresses """
		return self.subnets[self.given_cidr]["subnet_addresses"]

	def usable_addresses(self):
		""" returns content for usable_addresses """
		return self.subnets[self.given_cidr]["usable_addresses"]

	def blocksize(self):
		""" returns content for blocksize """
		return self.subnets[self.given_cidr]["blocksize"]

	def cidr(self):
		""" returns content for cidr """
		return self.subnets[self.given_cidr]["cidr"]

	def mask(self):
		""" returns content for mask """
		return self.subnets[self.given_cidr]["mask"]

	def mask_binary(self):
		""" returns content for mask_binary """
		return self.subnets[self.given_cidr]["mask_binary"]

	def mask_octet(self):
		""" returns content for mask_octet """
		return self.subnets[self.given_cidr]["mask_octet"]

	def wildcard(self):
		""" returns content for wildcard """
		return self.subnets[self.given_cidr]["wildcard"]

	def octet(self):
		""" returns content for octet """
		return self.subnets[self.given_cidr]["octet"]

	def subnet_min_max_calc(self):
		""" calculates minimum and maximum values for the subnet """
		i = self.given_ip
		b = self.subnets[self.given_cidr]["blocksize"]
		o = self.subnets[self.given_cidr]["octet"]
		v = None
		if o == 1:
			v = self.given_ip_first_octet
		elif o == 2:
			v = self.given_ip_second_octet
		elif o == 3:
			v = self.given_ip_third_octet
		elif o == 4:
			v = self.given_ip_fourth_octet
		c = self.block_increment(b, v, 0)
		f = {"min_octet":c[0], "max_octet":c[1], "ip_range_min":"", "ip_range_max":""}
		if o == 1:
			f["ip_range_min"] = "{}.{}.{}.{}".format(c[0], 0, 0, 0)
			f["ip_range_max"] = "{}.{}.{}.{}".format(c[1], 255, 255, 255)
		elif o == 2:
			f["ip_range_min"] = "{}.{}.{}.{}".format(self.given_ip_first_octet, c[0], 0, 0)
			f["ip_range_max"] = "{}.{}.{}.{}".format(self.given_ip_first_octet, c[1], 255, 255)
		elif o == 3:
			f["ip_range_min"] = "{}.{}.{}.{}".format(self.given_ip_first_octet, self.given_ip_second_octet, c[0], 0)
			f["ip_range_max"] = "{}.{}.{}.{}".format(self.given_ip_first_octet, self.given_ip_second_octet, c[1], 255)
		elif o == 4:
			f["ip_range_min"] = "{}.{}.{}.{}".format(self.given_ip_first_octet, self.given_ip_second_octet, self.given_ip_third_octet, c[0])
			f["ip_range_max"] = "{}.{}.{}.{}".format(self.given_ip_first_octet, self.given_ip_second_octet, self.given_ip_third_octet, c[1])
		self.min_max_info = f
		return(f)

	def block_increment(self, b, v, c):
		""" used by subnet_min_max_calc to perform block math """
		self.min_max_octet = []
		if c <= v:
			c += b
			self.block_increment(b, v, c)
		if c > v:
			if self.cidr in [0, 31, 32]:
				self.min_max_octet = [int(c-b), int(c)]
			else:
				self.min_max_octet = [int(c-b), int(c)-1]
		return self.min_max_octet

	def octet_generator(self):
		""" generator for octet values, yields every octet value as an integer between the calculated min/max values  """
		for x in range(self.subnet_min_octet, self.subnet_max_octet+1):
			yield(x)

	def ip_range_generator(self):
		""" generator for IP values, yields every IP value as a string between the calculated min/max values  """
		o = self.subnets[self.given_cidr]["octet"]
		if o == 1:
			for a in range(self.subnet_min_octet, self.subnet_max_octet+1):
				for b in range(0,256):
					for c in range(0,256):
						for d in range(0,256):
							yield ("{}.{}.{}.{}".format(a, b, c, d))
		elif o == 2:
			for b in range(self.subnet_min_octet, self.subnet_max_octet+1):
				for c in range(0,256):
					for d in range(0,256):
						yield ("{}.{}.{}.{}".format(self.given_ip_first_octet, b, c, d))
		elif o == 3:
			for c in range(self.subnet_min_octet, self.subnet_max_octet+1):
				for d in range(0,256):
					yield ("{}.{}.{}.{}".format(self.given_ip_first_octet, self.given_ip_second_octet, c, d))
		elif o == 4:
			for d in range(self.subnet_min_octet, self.subnet_max_octet+1):
				yield ("{}.{}.{}.{}".format(self.given_ip_first_octet, self.given_ip_second_octet, self.given_ip_third_octet, d))

	def __repr__(self):
		""" default action if the object is printed """
		i = self.given_ip
		return(i)
