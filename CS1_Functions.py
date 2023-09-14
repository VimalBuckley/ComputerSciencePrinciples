def divisible(number, divisor):
    '''Checks if the number is divisible by the divisor'''
    if number % divisor == 0:
        return True
    return False

def my_mean(v1, v2, v3):
    '''Calculates the mean of 3 numbers'''
    return (v1 + v2 + v3) / 3

def rectanglePerimeter(side1, side2):
    '''Calculates the perimeter of a rectangle given its side lengths'''
    return 2 * (side1 + side2)

def nameCombiner():
    '''Combines your first, middle, and last name'''
    return input("What is your first name? ") + " " + input("What is your middle name? ") + " " + input("What is your last name? ") 
   
def tipCalculator(bill, percentTip):
    '''Tells you your final bill as well as your tip alone'''
    return [round(bill * (1 + percentTip), 2), round(bill*percentTip,2)]

def hypotenuse(side1, side2):
    '''Tells you the hypotenuse of a right triangle with the given side lengths'''
    return (side1**2 + side2**2)**0.5
