import os

def programQuit():
  print()
  input("Press ENTER to enter another number. ")

def isOdd(number):
  remainder = number % 2
  if(remainder == 1):
    return True
  else:
    return False

def isEven(number):
  remainder = number % 2
  if(remainder == 0):
    return True
  else:
    return False

def main():
  os.system("clear")
  print("""Hailstone String Generator Version: 1.2


Changelog:
  Version 1.0
    - Created this program
  Version 1.1
    - Removed double 1 bug
  Version 1.2
    - Removed blank input crash bug
    - Added the Changelog


Use the enter key to submit.
If the program freezes, wait a minute, if nothing happened, rerun the program.
To quit this program, press CTRL + C.
To copy text, select the text you would like to copy and press CTRL + SHIFT + C.
Please do not add decimal points to your number.
""")
  hailstoneStarterString = input("Enter the number you want to start the Hailstone with: ")
  try:
    hailstoneNumber = int(hailstoneStarterString)
  except:
    print("You need to put a number here.")
    programQuit()
    main()
  running = True
  currentNumber = hailstoneNumber
  print()
  print("Hailstone:")
  print(currentNumber)
  while running:
    if(currentNumber == 1):
      running =  False
    elif(isEven(currentNumber)):
      currentNumber = currentNumber / 2
      print(currentNumber)
    elif(isOdd(currentNumber)):
      currentNumber = currentNumber * 3
      currentNumber = currentNumber + 1
      print(currentNumber)
    
  programQuit()
  main()
main()