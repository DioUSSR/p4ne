import glob, re
res = list()
def Classificator(x):
    int = re.match(r'(interface)(.+)', x)
    ip = re.search(r'(([0-9]{1,3}[.]){3}([0-9]{1,3}[\ ]){1}((255[.])([0-9]{1,3}[.\ ]){3}))', x)
    host = re.match(r'(hostname)(.+)', x)
    if bool(ip) is True: return {'ip':ip.group(1)}
    if bool(int) is True: return {'interface':int.group(2)}
    if bool(host) is True: return {'hostname':host.group(2)}
    return{"none":0}
iplist = []
intlist = []
hostlist = []
for name in glob.glob('C:/Utils/config_files/*.txt'):
    with open(name) as f:
        for line in f:
            k = Classificator(line)
            if 'ip' in k.keys(): iplist.append(k['ip'])
            if 'interface' in k.keys(): intlist.append(k['interface'])
            if 'hostname' in k.keys(): hostlist.append(k['hostname'])
print(iplist)
print(intlist)
print(hostlist)