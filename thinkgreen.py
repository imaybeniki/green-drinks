# global variables of each type of fruit/veggie
global banana
global strawberry
global apple
global spinach
global avocado
global whey
global agave
global doneString
global baseString
global ingredientString
global liquidString

# defining constants
doneString = "Press done if complete or continue to add more for additional cost: \n"
baseString = "Select your base ingredient from options below: \n"
liquidString = "Select your liquid from options below: \n"
ingredientString = "Select ingredients from list, when complete press done: \n"


# classes to differentiate the types of ingredients
class Fruit:
    base = True
    mix_list = set([])
    amount = 0


class Vegetable:
    base = False
    mix_list = set([])
    amount = 0


class Addition:
    base = True
    mix_list = set([])
    amount = 0


# defines flavors as objects
def defineFlavors():
    global banana
    global apple
    global strawberry
    global spinach
    global avocado
    global whey
    global agave

    banana = Fruit()
    apple = Fruit()
    strawberry = Fruit()
    spinach = Vegetable()
    avocado = Vegetable()
    whey = Addition()
    agave = Addition()

    banana.mix_list = set(['banana', 'apple', 'strawberry', 'spinach', 'whey', 'agave'])
    apple.mix_list = set(['banana', 'apple', 'strawberry', 'spinach', 'whey', 'agave'])
    strawberry.mix_list = set(['banana', 'apple', 'strawberry', 'whey', 'agave'])
    spinach.mix_list = set(['banana', 'apple', 'whey', 'agave'])
    whey.mix_list = set(['banana', 'apple', 'strawberry', 'spinach', 'whey', 'agave'])
    agave.mix_list = set(['banana', 'apple', 'strawberry', 'spinach', 'whey'])

    #print(banana.mix_list.intersection(whey.mix_list))


def updateTotal(mix_list):
    global doneString
    total = 0
    for ingredients in mix_list:
        if total >= 8:
            print(doneString)
        total += ingredients.amount
    return total


def main():
    global liquidString
    global baseString
    global ingredientString
    global doneString

    defineFlavors()

    mix_list = []
    options = set(['banana', 'apple', 'strawberry', 'spinach', 'whey', 'agave'])
    bases = set(['banana, avocado'])
    liquids = set(['coconut water', 'water', 'skim milk', 'whole milk', 'orange juice', 'yogurt'])

    liquid = input(liquidString + str(liquids) + "\nLiquid:")
    mix_list.append(liquid)

    base = input(baseString + str(bases) + "\nBase:")
    mix_list.append(base)

    if base is 'banana' or 'Banana':
        options = banana.mix_list
    elif base is 'avocado' or 'Avocado':
        options = avocado.mix_list
    else:
        base = input("Please select a base from the list: \n")
        print(bases)

    while True:
        new_ingredient = input(ingredientString + str(options) + "\nIngredient:")
        if new_ingredient is 'Done' or 'DONE' or 'done':
            break
        mix_list.append(new_ingredient)
        updateTotal(mix_list)
        if new_ingredient is 'Banana' or 'banana':
            options = banana.mix_list.intersection(options)
        elif new_ingredient is 'Apple' or 'apple':
            options = apple.mix_list.intersection(options)
        elif new_ingredient is 'Strawberry' or 'strawberry':
            options = strawberry.mix_list.intersection(options)
        elif new_ingredient is 'Spinach' or 'spinach':
            options = spinach.mix_list.intersection(options)
        elif new_ingredient is 'Whey' or 'whey':
            options = whey.mix_list.intersection(options)
        elif new_ingredient is 'Agave' or 'agave':
            options = agave.mix_list.intersection(options)
        else:
            print("Please select an ingredient from the list. \n")


if __name__ == '__main__':
    main()