#global variables of each type of fruit/veggie
global banana
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
    global spinach
    global avocado
    global whey
    global agave

def updateTotal(mixList):
    global doneString
    total = 0
    for ingredients in mixList:
        if total >= 8:
            print(doneString)
        total += ingredients.amount




