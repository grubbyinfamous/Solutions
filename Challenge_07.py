'''
Things to do:
Create 3 Functions
    StoredPasswords(checkPass)
    getUserPass()
    main()
Create a tuple with 50 of the most common passwords in StoredPasswords(checkPass)
Ask the user to create a username and password (different variables for each)
check to see if the user had a password from the tuple and warn them that their password is too common
print the location of the matching password in the tuple
'''

#Here is where I will create the tuple with all common passwords
#I created the tuple as a global variable since I will be using it in multiple functions
common_Passwords = ("123456","123456789","12345","qwerty","password","12345678",\
    "111111","123123","1234567890","1234567","qwerty123","000000","1q2w3e","aa12345678","abc123","password1",\
    "1234","qwertyuiop","123321","password123","12w3e4r5t","iloveyou","654321","666666","987654321","123","123456a",\
    "qwe123","1q2w3e4r","7777777","1qaz2wsx","123qwe","zxcvbnm","121212","asdasd","a123456","555555","dragon",\
    "112233", "123123123", "monkey", "11111111", "qazwsx", "159753", "asdfghjkl", "222222", "1234qwer", "qwerty1",\
    "123654", "123abc")

#We will use this function to call getUserPass(), where we will obtain the user's username and password
def main():
    print("Welcome to the password checker!")
    getUserPass()
 
#This is where we will obtain the user's username and password   
def getUserPass():
    user_Name = ""
    user_Password =""
    result = ""
    
    user_Name = input("Please enter your username: ")
    user_Password = input("Please enter your password: ")
    result = StoredPasswords(user_Password)
    if (result == "Your password is too common. Please consider changing it"):
        print(result)
        print(f"The location of the password in the tuple is at index {common_Passwords.index(user_Password)}")
    else:
        print(result)
    

#This is where we will check if the user's password is in the common passwords tuple
def StoredPasswords(checkPass):
    notFound = ""
    found = ""
    
    #We will use an if else decision structure as well as the in operator to check if the user's password is in the tuple
    if checkPass in common_Passwords:
        found = "Your password is too common. Please consider changing it"
        return found
    else:
        notFound = "You have a strong password"
        return notFound
    
main()