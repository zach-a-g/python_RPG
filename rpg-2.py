class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power 
    
    def attack(self, enemy):
        enemy.health  -= self.power

    def alive(self):
         return self.health > 0

    def print_status(self):
        print("The Stranger has %d health" % (self.health))   


class Hero(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power

class Goblin(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power

kratos = Hero(10, 5)
the_stranger = Goblin(6, 2)


def main():
    

    while the_stranger.alive() and kratos.alive():
        print("You have %d health and %d power." % (kratos.health, kratos.power))
        print("The Stranger has %d health and %d power." % (the_stranger.health , the_stranger.power))
        print()
        print("What do you, God of War, want to do?")
        print("1. Use Blades of Exile on The Stranger")
        print("2. Do nothing and get rekt with punches")
        print("3. Cowards way out (flee)")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            kratos.attack(the_stranger)
            the_stranger.print_status()
            print("You do %d damage to The Stranger." % kratos.power)
            if the_stranger.health  <= 0:
                print("The Stranger is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if the_stranger.health  > 0:
            # Goblin attacks hero
            the_stranger.attack(kratos)
            kratos.print_status()
            print("The Stranger does %d damage to you." % the_stranger.power)
            if kratos.health <= 0:
                print("The God of War has been slain.")

main()