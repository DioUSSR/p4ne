import glob

res = list()
print(res)

for name in glob.glob('C:/Utils/config_files/*.txt'):
    print(name)
    with open(name) as f:
        for line in f:
            p = line.find("ip address")
            if p > 0: res.append(line[p+11:p+46])
list(set(res))
print(res)


