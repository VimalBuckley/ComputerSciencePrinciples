import random

class Student():
    def __init__(self, gpa = 2.5, age = 17, gradeLevel = 10, hairColor = "Brown", eyeColor = "Brown", height = 63, weight = 125, favoriteShoe = "Tenis"):
        self.gpa = gpa
        self.age = age
        self.gradeLevel = gradeLevel
        self.hairColor = hairColor
        self.eyeColor = eyeColor
        self.height = height
        self.weight = weight
        self.favoriteShoe = favoriteShoe

    def study(self, time):
        if time > 1:
            self.gpa += 0.25
        else:
            self.gpa +- 0.25

    def cheat(self):
        if random.randint(0,10) >= 8:
            self.gpa += 2
        else:
            gpa = 0

    def dye(self, newColor):
        self.hairColor = newColor

    def shave(self):
        self.hairColor = "None"

    def birthday(self):
        self.age += 1

    def grow(self):
        self.height += random.random()

    def surgery(self, newHeight):
        self.height = newHeight

    def eat(self, massOfFood):
        self.weight += (random.random() * massOfFood)
    
    def exercise(self, timeHours):
        self.weight -= timeHours

    def shopping(self, newShoe):
        self.favoriteShoe = newShoe

    def contacts(self, colorOfContacts):
        self.eyeColor = colorOfContacts
