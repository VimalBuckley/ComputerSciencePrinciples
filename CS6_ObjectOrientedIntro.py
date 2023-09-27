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
