charcters: list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ",", "?", "!", "'"]

def encrypt(message: str, shift: int):
    encryptedCharacters = []
    for letter in message:
        encryptedCharacters.append(charcters[loopIndex(charcters.index(letter), shift)])
    return "".join(encryptedCharacters)

def decrypt(encrptedMessage: str, shift: int):
    return encrypt(encrptedMessage, -shift)
    
def loopIndex(inital, shift):
    if inital < 0:
        inital = 0
    if (inital > len(charcters) - 1):
        inital = len(charcters) - 1
    sum = inital + shift
    while (sum > len(charcters) - 1):
        sum -= (len(charcters)) 
    while (sum < 0):
        sum += (len(charcters))
    return sum

print(encrypt("flajsf4793", 2))
print(decrypt(encrypt("flajsf4793", 2), 2))