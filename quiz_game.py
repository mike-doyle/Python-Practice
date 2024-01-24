import sys
import time


# added delay to make game feel more interactive 
# rather than instantly displaying questions/answers

def question_one(string, delay):
    for char in string:
        time.sleep(delay)
        sys.stderr.write(char)
def question_two(string, delay):
    for char in string:
        time.sleep(delay)
        sys.stderr.write(char)
def question_three(string, delay):
    for char in string:
        time.sleep(delay)
        sys.stderr.write(char)
def question_four(string, delay):
    for char in string:
        time.sleep(delay)
        sys.stderr.write(char)
def question_five(string, delay):
    for char in string:
        time.sleep(delay)
        sys.stderr.write(char)
def question_six(string, delay):
    for char in string:
        time.sleep(delay)
        sys.stderr.write(char)
def question_seven(string, delay):
    for char in string:
        time.sleep(delay)
        sys.stderr.write(char)
def question_eight(string, delay):
    for char in string:
        time.sleep(delay)
        sys.stderr.write(char)
def question_nine(string, delay):
    for char in string:
        time.sleep(delay)
        sys.stderr.write(char)
def question_ten(string, delay):
    for char in string:
        time.sleep(delay)
        sys.stderr.write(char)
def what_name(string, delay):
    for char in string:
        time.sleep(delay)
        sys.stderr.write(char)
def decide(string, delay):
    for char in string:
        time.sleep(delay)
        sys.stderr.write(char)

# Variable to keep track of game score
# Score will display at end of game depending on amount of answers user got correct.
score = 0

print("")
print("Welcome to 'Quiz Game'!\n")

what_name("What is your name?\nType Here --->  ",0.04)
name_enter = input()

print("Great to meet you " + name_enter + ", lets get started!")

print("")

decide("4 Questions! (+1 for correct answers, -1 for incorrect answers...) \n\nWould you like to play?\nType 'yes' or 'no'--->  ",0.04)
decide_game = input()
if decide_game.lower() != "yes":
    quit() 

print("")

question_one("Great!\n\n[Question 1: What is the name of the planet closest to the sun?]\n\nA. Mars\nB. Mercury\nC. Venus\nD. Saturn\n\nType your answer here ---> ",0.03)
answer_one = input().lower().strip()

print("")

if answer_one.lower() == "a":
    print("Bad choice!")
    score -= 1
elif answer_one.lower() == "b":
    print("Great job! Next question..")
    score += 1
elif answer_one.lower() == "c":
    print("Oh man.. not the right answer.")
    score -= 1
elif answer_one.lower() == "d":
    print("Yikes.. Not even close!")
    score -= 1
else:
    print("... Thats not a valid answer, -1.")
    score -= 1

print("")

question_two("[Question 2: Is there anything FASTER than light?]\n\nA. Yes!\nB. NO!\n\nType your answer here ---> ",0.04)
answer_two = input().lower().strip()
print("")

if answer_two.lower() == "a":
    print("Nope, sorry wrong answer!")
    score -= 1
elif answer_two.lower() == "b":
    print("Nice Job! On to the next one!\n\n")
    score += 1
else:
    print("... Thats not a valid answer, -1.")
    score -= 1

print("")

print("[Question 3: What is the name of the 5th US President?]\n")

print("")

question_three("A.Abraham Lincoln\nB.Thomas Jefferson\nC.James Monroe\nD.Grover Cleveland\n\nType your answer here ---> ",0.04)
answer_three = input().lower().strip()
print("")

if answer_three.lower() == "a":
    print("Nope, sorry wrong answer.")
    score -= 1
elif answer_three.lower() == "b":
    print("Thats incorrect!")
    score -= 1
elif answer_three.lower() == "c":
    print("WOW! Not sure how you managed to get that one right...\nNext Question!\n\n")
    score += 1
elif answer_three.lower() == "d":
    print("Good try but thats not right..")
    score -= 1
else:
    print("... Thats not a valid answer, -1.")
    score -= 1

print("")

question_four("[Question 4: Which of these cities has the highest population?]\n"\
"A. Tokyo\nB. Seoul\nC. New York\nD. Istanbul\n\n"\
'Type your answer here ---> ',0.04)
answer_four = input().lower().strip()
print("")

if answer_four.lower() == "a":
    print("Nope, sorry wrong answer.")
    score -= 1
elif answer_four.lower() == "b":
    print("Thats incorrect!")
    score -= 1
elif answer_four.lower() == "c":
    print("That answer is incorrect!")
    score -= 1
elif answer_four.lower() == "d":
    print("Very nice! You got it.")
    score += 1
else:
    print("... Thats not a valid answer, -1.")
    score -= 1

print("")
print("Calcualating Score... \n\n")
time.sleep(2)
print("Sorry this is taking some time... \n\n")
time.sleep(3)
print("Okay finally got my caluclator working...\n\n")
time.sleep(2)

print("You got " + str(score) + " questions correct " + name_enter + ".\n")
print("That's " + str((score / 4) * 100) + "%.\n\n")

print("")


if score > 5:
    print("AMAZING JOB!")
elif score <= 4:
    print("Try again for a better score!")

print("")
print("")
print("")