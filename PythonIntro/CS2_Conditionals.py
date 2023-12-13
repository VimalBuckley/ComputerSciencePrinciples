import random

def myGrade2(score,max):
    percentGrade = 100*(score/max)
    if percentGrade >= 60:
        if percentGrade >= 63:
            if percentGrade >= 67:
                if percentGrade >= 70:
                    if percentGrade >= 73:
                        if percentGrade >= 77:
                            if percentGrade >= 80:
                                if percentGrade >= 83:
                                    if percentGrade >= 87:
                                        if percentGrade >= 90:
                                            if percentGrade >= 93:
                                                if percentGrade >= 98:
                                                    return "n A+"
                                                return "n A"
                                            return "n A-"
                                        return " B+"
                                    return " B"
                                return " B-"
                            return " C+"
                        return " C"
                    return " C-"
                return " D+"
            return " D"
        return " D-"
    return " F"

def rollTwoDice():
    '''Rolls two 6 sided die, and gives you your result'''
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return "You rolled a " + str(die1) + " and a " + str(die2) + ", and your total was " + str(die1+die2)



