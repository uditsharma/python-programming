import random
import time

from actors import Creature, Wizard


def main():
    print_header()
    game_loop()


def print_header():
    print("----------------------------")
    print("           WIZARD GAME APP")
    print("----------------------------")
    print()


def game_loop():
    creatures = [Creature('Todd', 1), Creature('Tiger', 12), Creature('Bat', 3), Creature('Dragon', 50),
                 Creature('Evil Wizard', 1000)]

    hero = Wizard('Gandolf', 75)

    while True:
        active_creature = random.choice(creatures)
        print('A {} of level {} has appear from a dark and foggy forest...'
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input("Do you want to [a]ttack, [r]un away, or [l]ook around ? ")
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("Wizard runs and hide to gain the power again")
                time.sleep(5)
                print("Wizard is ready to roll")
        elif cmd == 'r':
            print("Running Away")
        elif cmd == 'l':
            print("Wizard looks around and sees the ")
            for c in creatures:
                print("* A {} level of {}".format(c.name, c.level))
        else:
            print("Ok, Exiting game, bye !")
            break


if __name__ == '__main__':
    main()
