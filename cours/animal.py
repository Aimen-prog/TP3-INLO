# coding: utf-8
class Animal:
    """ Animal classe's """
    biome = "savana"

    def __init__(self, param_species, param_weight, param_sex, param_age):
       self.weight = param_weight
       self.species = param_species
       self.sex = param_sex
       self.age = param_age
       self.__uniqId = 1
       #self._age = param_age

    def move(self):
        print("{} move".format(self.species))

    def make_noise(self, noise):
        print("{} : {}".format(self.species, noise))

    def change_biome(cls, new_biome):
        Animal.biome = new_biome
    change_biome = classmethod(change_biome)

    def definition():
        print("Je reprensente la class {}".format(__class__))
    
    # getter, setter avec controle
    def _get_age(self):
        try:
            return self._age
        except AttributeError:
            print("No age for object")
    
    def _set_age(self, param_age):
        if param_age < 0:
            self._age = 0
        else:
            self._age = param_age

    def _del_age(self):
        del self._age
    
    # property(getter, setter, deleter, helper)
    age = property(_get_age, _set_age, _del_age,"animal age")



    definition = staticmethod(definition)
    
    def __repr__(self):
        return self.species+" " + str(self.weight) + " kg " + self.sex + " age : " + str(self._age)

    def __str__(self):
        return "STR " +self.species+" " + str(self.weight) + " kg " + self.sex + " age : " + str(self._age)

    def __eq__(self, b):
        return isinstance(b, Animal) and self._age == b.age and self.species == b.species