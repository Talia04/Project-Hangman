# instructions here 
#https://docs.google.com/document/d/1syV83fqyybyQJD4V80XN1EKwmemQri1ZRSycPlsthrg/edit?usp=drivesdk

#My teammate: Ruvarashe

secret_word = list("______") #actual secret word is: IMAGES, the asterisks are placeholders
#counter for while loop iterations
i = 1

#To display number of wrong guesses and end game when number of fails = 6 
fails = 0

print("~"*70)       #decoration
print("Welcome to my game of HANGMAN!\nLET'S PLAY!")
print("~"*70+"\n")     #decoration
print("Here's how:\n1. The goal is to guess the secret word, one letter at a time\n2. To win, you need to guess all 6 letters in the secret word correctcly\n3. If you guess wrong 6 times, You Lose\n")
print("~"*70) 

print("LET'S GO!!!\n\n")
#a variable for the secret word placeholders
print("The secret word is : _ _ _ _ _ _")

#this loop contains the whole game. Asks the user to make guesses for a maximum of 12 times.
while i in range(1,13):
  if i == 1:
    trial = "st"
  elif i == 2:
    trial = "nd"
  elif i == 3:
    trial = "rd"
  elif i in range(4,13):
    trial = "th"

  user_guess = input("Try your {}{} guess\n".format(i,trial))
  if user_guess in ["i","m","a","g","e","s"]:
    print("😃 Good guess!")
    if user_guess == "i":
      secret_word[0] = "i"
      print(*secret_word)
    elif user_guess == "m":
      secret_word[1] = "m"
      print(*secret_word)
    elif user_guess == "a":
      secret_word[2] = "a"
      print(*secret_word)
    elif user_guess == "g":
      secret_word[3] = "g"
      print(*secret_word)
    elif user_guess == "e":
      secret_word[4] = "e"
      print(*secret_word)
    elif user_guess == "s":
      secret_word[5] = "s"
      print(*secret_word)
  else:
    print("😝 Wrong guess!Try Again.")
    fails += 1
    tries_left = 6 - fails
    print("Trials left : {}".format(tries_left))
  i += 1
  line1 = "--------\n"
  line2 = "|      |\n"
  line3 = "|      O\n"
  line4 = "|     \|  \n"
  line5 = "|     \|/\n"
  line6 = "|      |\n"
  line7 = "|     /  \n"
  line8 = "|     / \\\n"
  line9 = "|\n"
  line10 = "-"

  if fails == 1:
    print(line1+line2+line3+line9*3+line10)
  elif fails == 2:
    print(line1+line2+line3+line4+line9*2+line10)
  elif fails == 3:
    print(line1+line2+line3+line5+line9*2+line10)
  elif fails == 4:
    print(line1+line2+line3+line5+line6+line9+line10)
  elif fails == 5:
    print(line1+line2+line3+line5+line6+line7+line10)
  elif fails == 6:
    print(line1+line2+line3+line5+line6+line8+line10)
    break
  if secret_word == ["i","m","a","g","e","s"]:
    break
    
if secret_word == ["i","m","a","g","e","s"]:
  print("*"*75+"\nCONGRATULATIONS! 🥳 YOU WIN\n"+"*"*75)
else:
  print("GAME OVER. YOU LOSE 👎")