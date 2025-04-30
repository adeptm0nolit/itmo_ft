
def mean_dev(val_l: list): # Функция поиска среднего значения
    avg = sum(val_l) / len(val_l)
    return avg


def std_dev(val_l: list):  # Функция поиска среднеквадратичного отклонения
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
for i in f: # Создание списков x и y из данных, считанных из файла
    i = list(map(float, i.replace(',', '.').split('\t')))
    if len(i) == 2:
        x.append(float(i[0]))
        y.append(float(i[1]))
    else:
        continue

mean_x = mean_dev(x)
std_x = std_dev(x)
mean_y = mean_dev(y)
std_y = std_dev(y)

print(f'1. Mean deviance x: {mean_x}, mean deviance y: {mean_y}\n   Standard deviance x: {std_x}, standard deviance y: {std_y}')

print(f'2. Mean deviance x: {mean_x}, standard deviance x: {std_x}')

print(f'3. Mean deviance y: {mean_y}, standard deviance y: {std_y}')

print("Подробное объяснение см. README.md")