import random
n = random.randint(1, 100)
a = -1
guesses = 0


while( a!= n):
  guesses +=1
  a = int(input("Guess a number: "))
  if (a>n):
    print("Lower number please")
  elif(a<n):
    print("Greater number please")
  else:
    print(f" You guessed {n}it right in {guesses} attempts")



