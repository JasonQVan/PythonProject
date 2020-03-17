
machinewater = 400
machinemilk = 540
machinebeans = 120
Cups_Coffee = 0
money = 550
disposable_cups = 9

water = 200
milk = 50
coffee_beans = 15
expwater = 250
expbeans = 16
latwater = 350
latbeans = 20
latmilk = 75
cappuwater = 200
cappumilk = 100
cappubeans = 12


def actionbuy():
    global machinewater
    global machinebeans
    global machinemilk
    global disposable_cups
    global money
    print("What do you want to buy? 1 - expresso, 2 - latte, 3 - cappuccino")
    coffeetype = input()
    if coffeetype == "1":
        if machinewater < 250 or machinebeans < 16 or disposable_cups == 0:
            checkmachine()
        else:
            machinewater = machinewater - 250
            machinebeans = machinebeans - 16
            money = money + 4
            disposable_cups = disposable_cups - 1
            print("I have enough resources, making you a coffee!")

    elif coffeetype == "2":
        if machinemilk < 75 or machinewater < 350 or machinebeans < 20 or disposable_cups == 0:
            checkmachine()
        else:
            machinewater = machinewater - 350
            machinemilk = machinemilk - 75
            machinebeans = machinebeans - 20
            money = money + 7
            disposable_cups = disposable_cups - 1
            print("I have enough resources, making you a coffee!")
    elif coffeetype == "3":
        if machinemilk < 100 or machinewater < 200 or machinebeans < 12:
            checkmachine()
        else:
            machinewater = machinewater - 200
            machinemilk = machinemilk - 100
            machinebeans = machinebeans - 12
            money = money + 6
            disposable_cups = disposable_cups - 1
            print("I have enough resources, making you a coffee!")
    else:
        print("Not a valid option!")


def actionfill():
    global machinewater
    global machinebeans
    global machinemilk
    global disposable_cups

    print("Write how many ml of water do you want to add:")
    fillwater = int(input())
    print("Write how many ml of milk do you want to add:")
    fillmilk = int(input())
    print("Write how many grams of coffee beans do you want to add:")
    fillbeans = int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    fillcups = int(input())

    machinewater += fillwater
    machinemilk += fillmilk
    machinebeans += fillbeans
    disposable_cups += fillcups


def actiontake():
    global money
    print("I gave u $" + str(money))
    money = 0


def actionremain():
    global machinewater
    global machinebeans
    global machinemilk
    global disposable_cups
    global money

    print("The coffee machine has: ")
    print(str(machinewater) + " of water")
    print(str(machinemilk) + " of milk")
    print(str(machinebeans) + " of coffee beans")
    print(str(disposable_cups) + " of disposable cups")
    print(str(money) + " of money")


def checkmachine():
    global expwater
    global expbeans
    global latwater
    global latbeans
    global latmilk
    global cappuwater
    global cappumilk
    global cappubeans
    global water
    global milk
    global coffee_beans
    global disposable_cups

    if machinewater < latwater or machinewater < cappuwater or machinewater < expwater:
        return print("Sorry, not enough water!")
    elif machinemilk < latmilk or machinemilk < cappumilk:
        return print("Sorry, not enough milk!")
    elif machinebeans < expbeans or machinebeans < cappubeans or machinebeans < latbeans:
        return print("Sorry, not enough coffee beans!")


while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if action == "buy":
        actionbuy()

    elif action == "fill":
        actionfill()

    elif action == "take":
        actiontake()

    elif action == "remaining":
        actionremain()

    elif action == "exit":
        break
