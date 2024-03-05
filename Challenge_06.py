'''
Objectives:
Write a program that writes a series of random numbers to a file
Use the random import to generate random numbers
Use the file function to create and write to a file
Catch exceptions and handle them (particularly users inputting strings instead of ints)
'''

#This is so that the program can generate random files
import random

#this is the main function, where it will call the function fileGenerator() 
def main():
    print("Welcome to the random number generator! In this program \n we will be creating a new file and writing a series of random numbers to it")
    fileGenerator()
    print("the file has now been created, please check under D:\\StudentTestCodeFiles\\rng.txt")
    
#This function is where the new file will be created, and where the program will ask for the number of 
#random numbers to generate. This is also where exception handling will be used    
def fileGenerator():
    randNums = 0 #This will be the amount of random numbers to generate, pending user input
    random_File = open("D:\\StudentTestCodeFiles\\rng.txt", "w")
    is_Int = False
    print("The name of the new file is rng.txt, and it is under D:\\StudentTestCodeFiles")
    
    #This is where the user will input their number of random numbers to generate, and
    #I will use exception handling to catch those who try to put in a string
    try:
        randNums = int(input("Please put the number of random numbers to generate, in integer form: "))
    except ValueError: #this code will execute when the user inputs a string instead of an integer
        while(is_Int == False):
            try:
                randNums = int(input("Please put in a number in the form of an integer: "))
            except ValueError: #if the user keeps putting in a string, they will be forced to try again
                print("Please try again")
            else: #This else block will execute if the user inputs an integer
                break
    
    writeNumbers(randNums)
    random_File.close()
        

#This is where we shall write the random numbers in the file we generated in fileGenerator()
def writeNumbers(randNums):
    #This variable is for the random numbers that we will write in the file
    writeRandom = 0
    random_File = open("D:\\StudentTestCodeFiles\\rng.txt", "a")
    
    #This for loop will use the number the user inputted in the following for loop to generate random numbers and write it into the new fi;e
    for x in range(randNums):
        writeRandom = random.randint(1, 500)
        random_File.write(f"{writeRandom}\n")
    
    random_File.close()
    
main()