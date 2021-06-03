'''
This program will be used for experiments that are usually pointless
Most projects will be deleted when no longer in use
'''

def encode(s):
  return " ".join([str(ord(i)) for i in s])
# encode('I love you 💖')

def decode(s):
  return "".join([chr(int(i)) for i in str(s).split()])
# decode('73 32 108 111 118 101 32 121 111 117 32 128150')

def simplify(n, d=None):
  if isinstance(n, str):
    n, d = tuple([int(i) for i in n.split('/')])
  nFacts = [i for i in range(1, n+1) if n % i == 0]
  dFacts = [i for i in range(1, d+1) if d % i == 0]
  gcf = max([i for i in nFacts if i in dFacts])
  if gcf == 1:
    return "Cannot simplify"
  else:
    n, d = n // gcf, d // gcf
    return f"{n}/{d}" if d != 1 else f"{n}"

def hangman(g=True):
  if g == True:
    word, guesses = "tuesday", set()
    g = False
      while False in [i in guesses for i in word]:
        guess = input("Enter a letter: ")
        guesses.add(guess)
        print("That letter is in the word!" if guess in word else "Guess again!")
        print(f"Current correct guesses: {''.join('_' if i not in guesses else i for i in word)}")
    print("You win!")
  
