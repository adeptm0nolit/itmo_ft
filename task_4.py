
def mean_dev(val_l: list):
    avg = sum(val_l) / len(val_l)
    return avg


def std_dev(val_l: list):
    len_l = len(val_l)
    avg = sum(val_l) / len_l
    res = 0
    for i in val_l:
        res += (i - avg) ** 2
    res /= len_l
    return res ** 0.5

with open('./CdSe_CdZnS Core_Shell.txt') as f:
    f = f.readlines()

x = []
y = []
for i in f:
    i = list(map(float, i.replace(',', '.').split('\t')))
    if len(i) == 2:
        x.append(float(i[0]))
        y.append(float(i[1]))
    else:
        continue

print(f'Mean deviance x: {mean_dev(x)}, mean deviance y: {mean_dev(y)}')

print(f'Standard deviance x: {std_dev(x)}, standard deviance y: {std_dev(y)}')
