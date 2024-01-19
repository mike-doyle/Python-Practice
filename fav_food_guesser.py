print("")
print("")
# Question Lines start for the user
print("Hey there! Got a serious question for you....")
print("")
print("Make sure you type the answer next to the question, then press the ENTER key....")
print("")
fav_food = input("What is my FAVORITE food? --->   "); # User will input their answer, if "Pizza" is entered, game ends.
print("")

#  Potential Results from first guess...
if fav_food == "Pizza":
    print("Yep! So amazing!")
    print("")
    print("Thanks for playing!")
    exit()
else:
    print("Yuck! That's not it!")
    print("")


    
second_guess = input("I'll give you two more chances! What is it?....")
print("")

#  Potential Results from second guess...
if second_guess == "Pizza":
    print("YES you acutally got it!")
    print("")
    print("Great job!! :)")
    exit()
else:
    print("ONE MORE CHANCE TO GUESS!  :(")
    print("")
    print("I'll give you a hint... it's round...")

#  Potential Results from third guess...
third_guess = input("Okay... This is your last guess, what is it?... ")
print("")

if third_guess == "Pizza":
    print("WOOO HOOOO YOU GOT IT!! ")
    print("")
else:
    print("How... how did you not guess it.... :(")
print("")
print("Thanks for playing!!")
print("")
exit()