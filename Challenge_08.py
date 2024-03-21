'''
Things to do:
Convert a string input into morse code
Create 2 tuples that contain both alphanumeric and morse code values and have their indexes match
Create 2 functions to convert the string into morse code
'''

#Here is where I will ask for the user's string
def main():
    stringConvert = ""
    morseCode = ""
    continueYN = "Y"
    while (continueYN == "Y"):
        stringConvert = input("Welcome to the Morse Code Converter Program! Please input your chosen phrase ")
        print("Your chosen phrase is " + stringConvert)
        stringConvert = stringConvert.lower()
        morseCode = convert(stringConvert)
        print("Your Morse Code is " + morseCode)
        continueYN = input("Would you like to continue? Y/N ")
        while (continueYN != "Y" and continueYN != "N"):
            continueYN = input("Please enter Y/N ")
        
#Here is where I will find the index of each character in the string and passing it to the converter function
#As well as converting the old string to Morse Code
def convert(stringConvert):
    alphaNumeric = (" ", ",", ".", "?", "1", "2", "3", "4", "5", "6", 
                         "7", "8", "9", "a", "b", "c", "d", "e", "f", "g",
                         "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                         "r", "s", "t", "u", "v", "w", "x", "y", "z")
    newPhrase = ""
    for char in stringConvert:
        if (char in alphaNumeric):
            replacer = getMorse(alphaNumeric.index(char))
            newPhrase = newPhrase + replacer
    return newPhrase

#Here is where I will find the corresponding Morse Code and return it
def getMorse(index):
    morseCode = (" ", "--..--", ".-.-.-", "..--..", "-----", ".----", "..---", "...--"
                      "....-", ".....", "-....", "--...", "---..", "----.", ".-", "-..."
                      "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-.."
                      "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-"
                      ".--", "-..-", "-.-", "--..")
    return morseCode[index]

main()