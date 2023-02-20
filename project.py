#Group Members: Logan Brinsmead and Pablo Barriga

# Part 1 of problem,
# checking if substrings of length n for string string contains {a, b, c, d}

#substringWithChars: function that takes a string, loops trough the
#                    string to see if we have one occurence of every letter
#                    in our alphabet
#@param string: string contains the string of characters we will be observing
#Pre Condition: the length of the string should be 0 <= n <= 6, also string should only 
#               have the letters in our alphabet
#@post condition: pops the first character in the string and returns the encoded string,
#          it can also return 1365 which is the rejecting state this occurs when we 
#          don't have every letter in our alphabet
def substringWithChars(string):
  window = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

  if len(string) < 6:
    return encode(string)

  left, right = 0, 0

  while right < 6:
    window[string[right]] += 1
    right += 1

  for value in window.values():
    if value == 0:
      return 1365

  window[string[left]] -= 1
  return encode(string[1:])

#encode: function that takes a string and encodes the value
#@param string: the string to be encoded
#Pre Condition: string should only contain letters in our alphabet
#@post: returns the encoded string as an int
def encode(string):
  dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

  encoded = 0
  counter = len(string) - 1
  for i in range(len(string)):
    encoded += dict[string[i]] * 4**counter
    counter -= 1

  return encoded

#decode: function that takes an int and decodes it to the string that represents the state
#@param number: the number to be decoded
#Pre Condion: number >= 0
#@post condition: returns the decoded number as a string
def decode(number):

  dict = {1: 'a', 2: 'b', 3: 'c', 0: 'd'}
  array = []

  while number > 0:
    r = number % 4

    if r == 0:
      array.append(dict[r])
      number -= 4

    else:
      array.append(dict[r])

    number = number // 4

  s = ''
  counter = len(array) - 1

  for i in range(len(array)):
    s += array.pop(counter)
    counter -= 1

  return s


# Part 2 of problem
#findCount: function to help compute the strings of length n accepted
#           by the DFA
#@param n: the length of the strings
#Pre Condition: the length of the string should be 0 <= n <= 300, 
#@post condition: current[0], number of strings of length n accepted by the DFA
def findCount(n):

  current = [1] * 1366
  current[1365] = 0
  next = current.copy()
  next[1365] = 0
  alphabet = ['a', 'b', 'c', 'd']

  transition = lambda word, char : word + char          # add a character from the alphabet to the end of the string
  
  for i in range(n):
    for j in range(1365):
      temp = 0
      word = decode(j)

      for c in alphabet:
        encoded = substringWithChars(transition(word, c))
        
        temp += current[encoded]
        
        next[j] = temp
    current = next.copy()

  
  return current[0]

# Getting the user input for the program
n = 0
while True:
  n = int(input("Please enter a value for n between 0 and 300: "))
  if n == -1:
    print("Exiting...")
    break
  elif n > 300 or n < -1:
    print("Incorrect input, value n cannot be greater than 300 or less than 0 (-1 to exit).\n")
    continue
  else:
    print(findCount(n))