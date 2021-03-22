import paramiko, time, re

host = '10.31.70.209'
login = 'restapi'
password = 'j0sg1280-7@'

def command(session, cmd, timeout):
    bs = 20000
    session.send("\n")
    time.sleep(timeout)
    session.recv(bs)
    session.send("terminal length 0\n")
    time.sleep(timeout)
    session.recv(bs)
    session.send(cmd)
    time.sleep(timeout)
    return session.recv(bs).decode()

ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_connection.connect(host, username=login, password=password, look_for_keys=False, allow_agent=False)
session = ssh_connection.invoke_shell()
res = command(session, 'show ip interface brief\n', timeout=2).split('\n')

for l in res[2:-1]:
    print(l)
    k = l.split(' ')
    p = ('show interface ' + k[0] + ' | i bytes' + '\n')
    rint = command(session, p, timeout=2).split("\n")
    print(rint[2] + '\n' + rint[3])


ssh_connection.close()

