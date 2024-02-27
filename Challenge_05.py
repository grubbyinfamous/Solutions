'''
Things to do
create functions to use for math operations such as exponentiation and multiplication
Ask users how long (in seconds) an object has been falling for
prompt users when they want to stop
Use local variables and constants in calculations
'''
#This is the main function, and its main purpose is to obtain the seconds from the user and call functions to calculate distance
def main(): 
    #Create variables for use in this function
    print("Welcome to the free falling distance calculator")
    calculator()
    #This loop will remain active so long as the user wants to continue calculating the free fall distance
  
#This function is where the loop for the distance in each second will take place
def calculator():
    seconds = 0
    current_Second = 0
    user_Stop = "n"
    distance = 0.0
    time_Squared = 0.0
    while(user_Stop.lower() == "n"):
        seconds = int(input("Please input the amount of time (in seconds) the object has been falling "))
        for n in range(seconds):
            current_Second = n+1
            time_Squared = exponentiation(current_Second) #This is where t^2 will be calculated, using the function exponentiation()
            print(f"Here is {current_Second} seconds squared: {time_Squared} seconds squared.") #This returns the time given squared
            distance = calcDistance(time_Squared) #This is where main() calls the calcDistance function and it is sending time_Squared so that it can calculate distance
            print(f"The object's distance traveled in {current_Second} seconds is {distance}")
        user_Stop = input("Would you like to stop? y/n ") #This is here to make sure that the user wants to continue
        while(user_Stop.lower() != "y" and user_Stop.lower() != "n"): #This is in case the user does not input either y or n
            user_Stop = input("Please enter either y or n: ")

#This function is where the time (in seconds) is raised to the 2nd power
def exponentiation(seconds):
    time_Squared = seconds**2
    return time_Squared #returns the time (in seconds) squared to the main function

#This function is where the distance will be calculated using the equation .5 * g * t^2
def calcDistance(time_Squared):
    gravity = 9.8
    distance = .5 * gravity * time_Squared #This uses the equation .5 * g * t^2
    return distance #returns the calculated distance so that the main function can display it

#This runs the main function
main()
    
    
