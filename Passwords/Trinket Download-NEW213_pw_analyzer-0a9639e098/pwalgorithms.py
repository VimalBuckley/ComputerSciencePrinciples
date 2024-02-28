# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("C:/Users/vimal/Documents/Github/ComputerSciencePrinciples/Passwords/Trinket Download-NEW213_pw_analyzer-0a9639e098/dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

def two_word(password):
  words = get_dictionary()
  guesses = 0
  for w in words:
    for w2 in words:
      guesses += 1
      if w + w2 == password:
        return True, guesses
  return False, guesses

def two_words_and_digit(password):
  words = get_dictionary()
  digits = ["", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  guesses = 0
  for w in words:
    for w2 in words:
      guesses += 1
      for digit in digits:
        if digit + w + w2 == password or w + w2 + digit == password or digit + w + w2 + digit == password:
          return True, guesses
  return False, guesses