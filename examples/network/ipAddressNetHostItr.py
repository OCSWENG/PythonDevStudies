import ipaddress

NETARRAY = [
    '10.9.0.0/24',
    'fdfd:87b5:b475:5e3e::/64',
]

for network in NETARRAY:
    net = ipaddress.ip_network(network)
    print('{!r}'.format(net))
    for i, ip in zip(range(3), net.hosts()):
        print(ip)
    print()

