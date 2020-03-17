class Machine:
    prompts = {  #prompts allows you to just call the string instead of typing it out, cleans it up
        'start': 'Write action (buy, fill, take, remaining, exit): ',
        'buy': 'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ',
        'water fill': 'Write how many ml of water do you want to add: ',
        'milk fill': 'Write how many ml of milk do you want to add: ',
        'coffee fill': 'Write how many grams of coffee beans do you want to add: ',
        'cups fill': 'Write how many disposable cups of coffee do you want to add: ',
    }

    def __init__(self, water=400, milk=540, coffeebeans=120, disposable_cups=9, money=550): #sets initial quantity of resources in machine
        self.water = water
        self.milk = milk
        self.coffeebeans = coffeebeans
        self.disposable_cups = disposable_cups
        self.money = money

    def makecoffee(self, water_needed, milk_needed, beans_needed, cup, cost):
        self.wn = water_needed
        self.mn = milk_needed
        self.bn = beans_needed
        self.dc = cup
        self.cost = cost
        if self.water < self.wn:
            print("Sorry, not enough water!")
            self.startup()
        elif self.milk < self.mn:
            print("Sorry, not enough milk!")
            self.startup()
        elif self.coffeebeans < self.bn:
            print("Sorry, not enough coffee beans!")
            self.startup()
        elif self.disposable_cups < self.dc:
            print("Sorry, not enough disposable cups!")
            self.startup()
        else:
            self.water -= self.wn
            self.milk -= self.mn
            self.coffeebeans -= self.bn
            self.disposable_cups -= self.dc
            self.money += self.cost
            print("I have enough resources, making you a coffee!")
            self.startup()

    def userinput(self, action):
        if action == "buy":
            self.userbuy()
        elif action == "fill":
            self.userfill()
        elif action == "remaining":
            self.userremaining()
        elif action == "take":
            self.usertake()

    def startup(self):
        action = input(self.prompts['start'])
        if action == "exit":
            return False
        else:
            self.userinput(action)

    def usertake(self):
        print(f"I gave you {self.money}")
        self.money = 0
        self.startup()
    
    def userremaining(self):
        print("The coffee machine has: ")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffeebeans} of coffee beans")
        print(f"{self.disposable_cups} of disposable cups")
        print(f"{self.money} of money")
        self.startup()

    def userfill(self): # takes user input for each resource and adds it to the variable
        self.water += int(input(self.prompts['water fill']))
        self.milk += int(input(self.prompts['milk fill']))
        self.coffeebeans += int(input(self.prompts['coffee fill']))
        self.disposable_cups += int(input(self.prompts['cups fill']))
        self.startup()

    def userbuy(self):
        ctype = input(self.prompts['buy'])
        if ctype == '1':
            self.makecoffee(250, 0, 16, 1, 4)
        elif ctype == '2':
            self.makecoffee(350, 75, 20, 1, 7)
        elif ctype == '3':
            self.makecoffee(200, 100, 12, 1, 6)
        elif ctype == 'back':
            self.startup()


while True:
    cm = Machine()

    cm.startup()
    break
