'''
Testing:
    How to create new files through Python
    How to do exception handling
'''

def createNewFile():
    file = open(r'D:\\StudentTestCodeFiles\\testText.txt', 'w')
    
    file.write("Welcome to this new file lol lmao")
    file.close()
    
def readFile():
    file = open('D:\\StudentTestCodeFiles\\testText.txt', 'r')
    line_One = file.readline()
    print(line_One)
    whole_Document = file.read()
    print(whole_Document)
    file.close()
    
def writeFile():
    file = open('D:\\StudentTestCodeFiles\\testText.txt', 'a')
    file.write("\nNow this is the second line")
    file.close()
        
createNewFile()
readFile()
writeFile()
readFile()