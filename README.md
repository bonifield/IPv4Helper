# IPv4Helper
Handle and manipulate IPv4 CIDRs in a simple fashion, including generating CIDR ranges and viewing general subnet information.

### Installation
```
pip install ipv4helper
```

### Usage
Provide an IPv4 address, and optionally the CIDR it resides in (otherwise "/32" will be appended to the given IP).
```
from ipv4helper import IPv4Helper
i = IPv4Helper("127.144.4.9/28")
print(i.subnet_summary)
for x in i.ip_range_generator():
	print(x)

# snipped output
# ...
# 127.144.4.9/28
# CIDR                    28
# Mask                    255.255.255.240
# Range                   127.144.4.0 - 127.144.4.15
# Blocksize               16
# Subnet Addresses        16
# Usable Addresses        14
# ACL Wildcard            0.0.0.15
# Octet Incremented       4
# Octet Masked            1
# ...
# 127.144.4.0
# 127.144.4.1
# 127.144.4.2
# 127.144.4.3
# 127.144.4.4
# ...
```

### Integration with IPv4Mutate [GitHub](https://github.com/bonifield/IPv4Mutate) [PyPi](https://pypi.org/project/ipv4mutate/)
```
from ipv4helper import IPv4Helper
from ipv4mutate import IPv4Mutate
i = IPv4Helper("127.144.4.9/28")
for x in i.ip_range_generator():
	z = IPv4Mutate(x)
	print(z.mutate_hex)

# snipped output
# ...
# 0x7f.0x90.0x4.0x0
# 0x7f.0x90.0x4.0x1
# 0x7f.0x90.0x4.0x2
# 0x7f.0x90.0x4.0x3
# ...
```

### Important Notes
- "/0" is not supported in this version, but it will be "soon"

### Available Attributes
### Available Attributes
```
blocksize
cidr
given_ip
given_cidr
given_ip_first_octet
given_ip_second_octet
given_ip_third_octet
given_ip_fourth_octet
iparg
mask
mask_binary
octet # position to be incremented
mask_octet # position to be masked
subnets # dictionary of general subnet information
subnet_summary
subnet_addresses
usable_addresses
subnet_info # dictionary
subnet_json # json
subnet_min_ip
subnet_max_ip
subnet_max_octet
subnet_min_octet
wildcard
```

### Available Generator Functions
```
octet_generator()
ip_range_generator()
```

### TODO
- better internal naming convention
- /0 support
- integrate with IPv4Mutate and IPv6Helper
