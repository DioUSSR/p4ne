from pysnmp.hlapi import *
community_name = "public"
ip_addr = "10.31.70.107"
udp_port = 161
snmp_obj1 = ObjectIdentity("SNMPv2-MIB", "sysDescr", 0)
snmp_obj2 = ObjectIdentity("1.3.6.1.2.1.2.2.1.2")
snmp_os = getCmd(SnmpEngine(),
                CommunityData(community_name, mpModel=0),
                UdpTransportTarget((ip_addr, udp_port)),
                ContextData(),
                ObjectType(snmp_obj1))
for i in snmp_os:
    for r in i[3]:
        print(r)
snmp_ifname = nextCmd(SnmpEngine(),
                CommunityData(community_name, mpModel=0),
                UdpTransportTarget((ip_addr, udp_port)),
                ContextData(), ObjectType(snmp_obj2), lexicographicMode=False)
for i in snmp_ifname:
    for r in i[3]:
        print(r[1])


