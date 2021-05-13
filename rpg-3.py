class Character:
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name
    
    def attack(self, enemy):
        enemy.health -= self.power

    def alive(self):
         return self.health > 0

    def print_status(self):
        print("%s has %d health" % (self.name, self.health))   


class Hero(Character):
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name

class Goblin(Character):
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name

class Zombie(Character):
    def alive(self):
        return True

kratos = Hero(20, 5, "Kratos")
the_stranger = Goblin(15, 2, "The Stranger")
zeus = Zombie(10, 10, "Zeus")

def main():
    

    while kratos.alive() and zeus.alive():
        print("You have %d health and %d power." % (kratos.health, kratos.power))
        print("Zeus has %d health and %d power." % (zeus.health , zeus.power))
        print()
        print("What do you, God of War, want to do?")
        print("1. Use Blades of Exile on Zeus")
        print("2. Do nothing and get rekt with thunderbolts")
        print("3. Cowards way out (flee)")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            kratos.attack(zeus)
            zeus.print_status()
            print("You do %d damage to Zeus." % kratos.power)
            if zeus.alive() == False:
                print("Zeus is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if zeus.alive():
            # Goblin attacks hero
            zeus.attack(kratos)
            kratos.print_status()
            print("Zeus does %d damage to you." % zeus.power)
            if kratos.alive() == False:
                print("The God of War has been slain.")

main()