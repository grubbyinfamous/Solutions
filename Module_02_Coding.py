'''
comment
'''

print("Hello World")


'''
Here is what I'm gonna do
Ask the user what their name is
Ask the user what the current year is
Ask the user what year they were born
Calculate the approximate age of the user
Display the appooximate age of the user
'''

#Here is where I ask for the user's name
#user_Name = input("Hello! What is your name?")
#print("It is nice to meet you", user_Name)

#Here is where I ask for what the current year is
#current_Year = int(input("Would you kindly tell me what the current year is? "))
#print("The current year, according to you is:", current_Year)

#Here is where I ask for the user's birth year
#user_BY = int(input("Would you kindly tell me what year you were born?"))
#print(user_Name, ", you were born in the year", user_BY)

#Here is where I calculate the user's approximate age
#user_Age = current_Year - user_BY

#Here is where I will display the user's current age
#print("Hello",user_Name,". According to your birth year, you are approximately", user_Age, "years old")
val = 123456.789
print(f'{val:,.2f}')
print(f'{0.2:.0%}')
print('One''Two''Three')

#One acre of land is equivalent to 43,560 sq. feet
#Write a program that asks the user to enter the total square feet in a tract of land and calculates the numebr of acres in the tract
feet_Per_Acre = 43560
num_Feet = 0
num_Feet = int(input("How much square feet is in your tract of land?"))
num_Acre = (num_Feet / feet_Per_Acre) * 100
print(f"you have {num_Acre}s in your tract")
