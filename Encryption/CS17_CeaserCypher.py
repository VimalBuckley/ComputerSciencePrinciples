characters: list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ",", "?", "!", "'"]

def encrypt(message: str, shift: int):
    badCharacters = [letter for letter in message if letter not in characters]
    if len(badCharacters) != 0:
        raise Exception("The messaged contained unrecognized characters:", badCharacters)
    return "".join(characters[loopIndex(characters.index(letter), shift, len(characters))] for letter in message)

def decrypt(encryptedMessage: str, shift: int):
    return encrypt(encryptedMessage, -shift)

def bruteForce(encryptedMessage: str):
    for index in range(len(characters)):
        print(decrypt(encryptedMessage, index))
    
def loopIndex(inital: int, shift: int, length: int):
    if inital < 0:
        inital = 0
    if (inital > length - 1):
        inital = length - 1
    sum = inital + shift
    while (sum > length - 1):
        sum -= length 
    while (sum < 0):
        sum += length
    return sum

shift = 156
encrypted = encrypt("My name is Vimal!", shift)
decrypted = decrypt(encrypted, shift)
print(encrypted)
print(decrypted)