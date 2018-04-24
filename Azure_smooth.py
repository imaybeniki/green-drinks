import csv
f = open('combinations.csv', 'r')
reader = csv.reader(f)
dic = {}
for line in reader:
    i = line[0]
    sl = set(line)
    dic.update({i: sl})

product = []
smoothie = dic.get('Almond Milk')
del dic['Almond Milk']
while len(product) < 7:
    fruit = input("Please select ingredient from list:\n" + str(smoothie) + '\n')
    if fruit in dic:
        smoothie = set.intersection(smoothie, dic.get(fruit))
        product.append(fruit)
    else:
        print("Sorry, that ingredient was not recognized")

print('Your smoothie contains ' + str(product))
