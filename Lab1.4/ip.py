import random
from ipaddress import IPv4Network
class IPv4RandomNetwork(IPv4Network):
    def __init__(self, a, m,):
        IPv4Network.__init__(self, a, m)
    def regular(self):
        return self.is_global
ip = random.randint(0x0B000000, 0xDF000000)
mask = random.randint(8, 24)
t = IPv4RandomNetwork(ip, mask)
print(t)
