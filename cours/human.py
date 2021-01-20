# coding: utf-8
from animal import Animal

class Human(Animal):
    def __init__(self, param_weight, param_sex, param_age, param_prenom):
        Animal.__init__(self, "Human", param_weight, param_sex, param_age)
        self.prenom = param_prenom
    
    def __str__(self):
        return self.prenom + " " + Animal.__str__(self)

    def move(self):
        print(self.prenom + " walk")

