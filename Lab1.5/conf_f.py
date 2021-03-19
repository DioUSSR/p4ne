import glob

res = list()
print(res)

for name in glob.glob('C:/Utils/config_files/*.txt'):
    print(name)
    with open(name) as f:
        for line in f:
            p = line.find("ip address")
            if p > 0:
                r = line[p+11:].strip("\n")
                if r not in res: res.append(r)
print(res)




