'''
Objectives
-Create a loop where the user will remain until they get all 5 questions correct
- Use loops to keep users in the program until they solve all 5 quesitons
- Use if statements to determine if users solve the riddles
'''

#Variables for use
user_Input = ""
user_Score = 0

#Enter the room
print("Welcome stranger, to the room of mysteries! You must solve all of my riddles,\
      \n else you will be trapped forever")

#ask the user if they want to play the game
user_Input = input("Would you like to play the game? yes/no")
#the loop begins here
if(user_Input.lower() == "yes"):
    print("Then let us start the game")
    while(user_Score < 5):
        
        #Ask the first question, and determine their score
        user_Input = input("Here is the first riddle: What can you hold in your right hand,\
                       \n but not in your left hand?")
        if(user_Input.lower() == "your left hand"): 
            print("You are correct! On to the next")
            user_Score += 1
        else:
            print("Incorrect, on to the next")
        print(f"your score is {user_Score}.") 
    
        #ask the second question, and determine their score
        user_Input = input("Second riddle: What gets wet while drying?")
        if(user_Input.lower() == "a towel"): 
            print("You are correct! On to the next")
            user_Score += 1
        else:
            print("Incorrect, on to the next")
        print(f"your score is {user_Score}.") 

        #ask the third question and determine their score
        user_Input = input("Third riddle: What kind of band never plays music?")
        if(user_Input.lower() == "a rubber band"): 
            print("You are correct! On to the next")
            user_Score += 1
        else:
            print("Incorrect, on to the next")
        print(f"your score is {user_Score}.") 
    
    #ask the fourth question and determine their score
        user_Input = input("Fourth riddle: What is the end of everything?")
        if(user_Input.lower() == "g"): 
            print("You are correct! On to the next")
            user_Score += 1
        else:
            print("Incorrect, on to the next")
        print(f"your score is {user_Score}.") 
    
    #ask the fifth question and determine their score
        user_Input = input("Here is the final riddle: When is a door no longer a door?")
        if(user_Input.lower() == "when it is ajar"): 
            print("You are correct! Now let us see if you have escaped")
            user_Score += 1
        else:
            print("Incorrect, now let us see if you have escaped")
        print(f"your score is {user_Score}.") 
    
        #determine if the user has escaped the room
        if(user_Score == 5):
            print("Congratulations, you have escaped the room!")
        else:
            print("You have not escaped. Try again")
            user_Score = 0
else:
    print("Very well")