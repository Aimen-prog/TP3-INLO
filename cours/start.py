# coding: utf-8
from animal import Animal
from human import Human

if __name__ == "__main__":
    # monkey = Animal()
    # print("Singe poids : {}".format(monkey.weight))
    # whale = Animal()
    # Animal.weight = 10000
    # human = Animal()
    # print("Baleine poids : {}".format(whale.weight))
    # print("Singe poids : {}".format(monkey.weight))
    # print("Humain poids : {}".format(human.weight))
    monkey = Animal("monkey", 10, "F", 10)
    whale  = Animal("whale", 10000, "M",20 )
    human  = Human(80, "F", -1, "Zoé")
    print(human)
    whale.make_noise("azeazeazeazea")
    Animal.definition()
    #del human.age
    print(human.age)
    #help(Animal)
    print(human.__dict__)
    #print(human.__uniqId)