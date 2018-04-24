import csv
f = open('combinations.csv', 'r')
reader = csv.reader(f)
combos = []
for line in reader:
    i = line[0]
    sl = set(line)
    dic = {i: sl}
    combos.append(dic)

print(combos)





