#Escape Room Assignment

"""
Things to do:
create variables such as riddle answers from input and score
Create decision structures using if, if-else, and if-elif-else statements
Use string comparators to determine if users are correct
Determine the user's score and respond approriately
"""

#Variables for use in the escape room
user_Input = ""
user_Score = 0

#Ask the first question
print("Welcome to the Room of Many Riddles! In order to escape,\
     \nyou must answer my riddles five")
user_Input = input("First riddle: What can you hold in your right hand,\
     \nbut never in your left hand? ")

#Use an if-else statment to determine score for question 1
if(user_Input.lower() == "your left hand"):
 user_Score += 1
 print("Correct! Now on to the next question")
else:
    print("Incorrect! But do not fear, you still have other questions")

#testing
print(f"your current score is {user_Score}.")

#Ask the second question
user_Input = input("Second riddle: What gets wet while drying?")

#Use an if-else statment to determine score for question 2
if(user_Input.lower() == "a towel"):
 user_Score += 1
 print("Correct! Now on to the next question")
else:
    print("Incorrect! But do not fear, you still have other questions")

print(f"your current score is {user_Score}.")

#Ask the third question
user_Input = input("Third riddle: What kind of band never plays music?")

#Use an if-else statment to determine score for question 3
if(user_Input.lower() == "a rubber band"):
 user_Score += 1
 print("Correct! Now on to the next question")
else:
    print("Incorrect! But do not fear, you still have other questions")

print(f"your current score is {user_Score}.")

#Ask the fourth question
user_Input = input("Fourth riddle: What is the end of everything?")

#Use an if-else statment to determine score for question 4
if(user_Input.lower() == "g"):
 user_Score += 1
 print("Correct! Now on to the next question")
else:
    print("Incorrect! But do not fear, you still have other questions")

print(f"your current score is {user_Score}.")

#Ask the final question
user_Input = input("Here is the final riddle: When is a door no longer a door?")

#Use an if-else statment to determine score for question 5
if(user_Input.lower() == "when it is ajar"):
 user_Score += 1
 print("Correct! Now, let us see if you escaped the room")
else:
    print("Incorrect! Now. let us see if you escaped the room")

print(f"your current score is {user_Score}.")

#Determine whether the user has escaped the room
if user_Score >= 3:
    if(user_Score == 5):
        print("You have escaped with a perfect score! you truly are the master of riddles")
    else:
        print("Congratulations, you have escaped the room of many riddles!")
else:
    print("Unforetunately, you did not escape the room of many riddles")