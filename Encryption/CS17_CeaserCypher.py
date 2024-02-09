characters: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()`~-=_+[]\;',./}{|:<>? "
shortCharacters: str = "abcdefghijklmnopqrstuvwxyz"
def encrypt(message: str, shift: int):
    return "".join(characters[loopIndex(characters.index(letter), shift, len(characters))] for letter in message)

def decrypt(encryptedMessage: str, shift: int):
    return encrypt(encryptedMessage, -shift)

def bruteForce(encryptedMessage: str):
    for index in range(len(characters)):
        print(decrypt(encryptedMessage, index))

def standardEncrypt(message: str, shift: int):
    encryptedMessage = []
    for letter in message:
        if letter == " ":
            encryptedMessage.append(" ")
        else:
            encryptedMessage.append(shortCharacters[loopIndex(shortCharacters.index(letter), shift, len(shortCharacters))])
    return "".join(encryptedMessage)

def standardDecrypt(message: str, shift:int):
    return standardEncrypt(message, -shift)    

def standardBruteForce(message: str):
    for index in range(len(shortCharacters)):
        print(standardDecrypt(message, index))

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

def UI():
    action: str = input("Would you like to encrypt or decrypt?\nType encrypt or decrypt: ") + "ed"
    if not action == "encrypted" and not action == "decrypted":
        raise Exception("Please choose a valid action: encrypt or decrypt")
    try:
        shift: int = int(input("What is the shift?"))
    except:
        raise Exception("Your shift must be a valid number!")
    phrase: str = input("What is the phrase to be " +  action + "?")
    badCharacters = [letter for letter in phrase if letter not in characters]
    if len(badCharacters) != 0:
        raise Exception("The messaged contained unrecognized characters:", badCharacters)
    if action == "encrypted":
        print(encrypt(phrase, shift))
    else:
        print(decrypt(phrase, shift))

UI()