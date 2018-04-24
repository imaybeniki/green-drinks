import csv
f = open('combinations.csv', 'r')
reader = csv.reader(f)
dic = {}
for line in reader:
    i = line[0]
    sl = set(line)
    dic.update({i: sl})

for n in range(6):
    print("Select an ingredient from list")
    print(dic.get('All'))
