#global variables of each type of fruit/veggie
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

#defining constants
doneString = "Press done if complete or continue to add more for additional cost:"
baseString = "Select your base ingredient:"
liquidString = "Select your liquid:"
ingredientString = "Select ingredients from list, when complete press done:"

#classes to differentiate the types of ingredients
class Fruit:
    base = True
    mixList = set([])
    amount = 0

class Vegetable:
    base = False
    mixList = set([])
    amount = 0

class Addition:
    base = True
    mixList = set([])
    amount = 0

#defines flavors as objects
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

    banana.mixList = set([banana, apple, strawberry, spinach, whey, agave])
    apple.mixList = set([banana, apple, strawberry, spinach, whey, agave])
    strawberry.mixList = set([banana, apple, strawberry, whey, agave])
    spinach.mixList = set([banana, apple, whey, agave])
    whey.mixList = set([banana, apple, strawberry, spinach, whey, agave])
    agave.mixList = set([banana, apple, strawberry, spinach, whey])

    print(banana.mixList.union(whey))

def updateTotal(mixList):
    global doneString
    total = 0
    for ingredients in mixList:
        if total >= 8:
            print(doneString)
        total += ingredients.amount
    return total

def main():
    global liquidString
    global baseString
    global ingredientString
    global doneString
    doneYet = True

    defineFlavors()

    liquid = input(liquidString)
    base = input(baseString)
    mixList = []
    while(not doneYet):
        newIngredient = input(ingredientString)
        if newIngredient is 'Done' or 'DONE' or 'done':
            break
        mixList.append(newIngredient)






