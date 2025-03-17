import random
randomNum = random.randint(1,100)

def check_guess(): 
 while True:
        guess = input("Guess the Number or Quit(Q) : ")
        if(guess == "Q"):
            break

        guess = int(guess)
    
        if(guess == randomNum):
            print(f"Congrats! {guess} is the correct answer!\n")
            break
        elif(guess<randomNum):
            print(f"{guess} is too small! Take a bigger guess")
        else:
            print(f"{guess} is too big! Take a smaller guess")

check_guess()            

print("___GAME____OVER__")        


