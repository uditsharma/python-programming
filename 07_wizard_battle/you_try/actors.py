import random


class Wizard:
    def __init__(self, name, level):
        self.level = level
        self.name = name

    def attack(self, creature):
        print("The Wizard {} attacks {}".format(self.name, creature.name))

        my_roll = random.randint(1, 12) * self.level

        creature_roll = random.randint(1, 12) * creature.level

        print("My roll {}".format(my_roll))
        print("Creature roll {}".format(creature_roll))

        if my_roll >= creature_roll:
            print("Wizard {} has easily triumphed over {}".format(self.name, creature.name))
            return True
        else:
            print("Wizard {} has been defeated".format(self.name))
            return False


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Creature: {} of level {}".format(self.name, self.level)
