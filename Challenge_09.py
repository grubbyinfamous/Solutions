'''
Things to Do
Use dictionaries to count the occurences of each word in a text file
Use the file methods to read the contents of a text file
Use a nested loop to iterate through the file and each line of the text file
'''

#Without this, I would not be able to read through the file
import json

def main():
    print("welcome to the word counter program!")
    reader()
 
#This is where we start the counter() function and output the dictionary in a formatted table
def reader():
    print("Please wait for the counter")
    word_Count = counter()
    for key in word_Count:
        print(f"Word: {key}, Count: {word_Count[key]}")

#This is where we will count the amount of occurences of each word and return the dictionary to the reader
def counter():
    EOF = False #This is to make sure that we have reached the end of the file
    line = ""
    line_List = []
    word_Count = {}
    count = 1
    read_File = open('C:\\users\\burres\\desktop\\Word_Frequency.txt', 'r')
    
    while EOF == False:
        line = read_File.readline()
        if line == "": #If this is true, this will break the loop
            EOF = True
        else:
            line_List = line.split() #This will turn each line into a list and we will iterate through each word and count each occurence
            for word in line_List:
                if word in word_Count:
                    word_Count[word] = word_Count[word] + 1
                else:
                    word_Count[word] = 1
    return word_Count
        
main()