'''
Things to do:
Create 4 classes:
Humanoid: height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma
human: child of humanoid, can add +2 to any stat
elf: child of humanoid, has 100% resistance to sleep and +2 to dexterity and charisma
dwarf: child of humanoid, has 20% resistance to magic, gains +2 bonus to strength and constituition, and -2 to charisma
Use user input and random number generators to generate a character
Bonus: Maybe use a GUI
'''

#without these, I would not be able to randomly generate numbers and create GUI
import random
import tkinter

class Humanoid:
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.__height = height
        self.__weight = weight
        self.__hair_color = hair_color
        self.__eye_color = eye_color
        self.str = strength
        self.dex = dexterity
        self.const = constitution
        self.intel = intelligence
        self.wis = wisdom
        self.cha = charisma

    def getHeight(self):
        return self.__height
    
    def getWeight(self):
        return self.__weight
    
    def getHairColor(self):
        return self.__hair_color
    
    def getEyeColor(self):
        return self.__hair_color
    
    def getStr(self):
        return self.str
    
    def getDex(self):
        return self.dex
    
    def getConst(self):
        return self.const
    
    def getIntel(self):
        return self.intel
    
    def getWis(self):
        return self.wis
    
    def getCha(self):
        return self.cha
    
    def setHeight(self, height):
        self.__height = height

    def setWeight(self, weight):
        self.__weight = weight

    def setHairColor(self, hair_color):
        self.__hair_color = hair_color

    def setEyeColor(self, eye_color):
        self.__eye_color = eye_color

    def setStr(self, strength):
        self.str = strength
    
    def setDex(self, dexterity):
        self.dex = dexterity

    def setConst(self, constitution):
        self.const = constitution
    
    def setIntel(self, intelligence):
        self.intel = intelligence

    def setWis(self, wisdom):
        self.wis = wisdom
    
    def setCha(self, charisma):
        self.cha = charisma

class Human(Humanoid):
    def __init__(self, height, weight, hair_color, eye_color, str, dex, const, intel, wis, cha, mod_attribute):
        super().__init__(height, weight, hair_color, eye_color, str, dex, const, intel, wis, cha)
        self.mod_Attribute = mod_attribute

    def getMod(self):
        return self.mod_Attribute
    
    def setMod(self, modAttribute):
        self.mod_Attribute = modAttribute

    def addMod(self):
        if (self.mod_Attribute.lower() == "strength"):
            super().setStr(super().getStr() + 2)
        elif (self.mod_Attribute.lower() == "dexterity"):
            super().setDex(super().getDex() + 2)
        elif (self.mod_Attribute.lower() == "constitution"):
            super().setConst(super().getConst() + 2)
        elif (self.mod_Attribute.lower() == "intelligence"):
            super().setIntel(super().getIntel() + 2)
        elif (self.mod_Attribute.lower() == "wisdom"):
            super().setWis(super().getWis() + 2)
        elif (self.mod_Attribute.lower() == "charisma"):
            super().setCha(super().getCha() + 2)
            
class Elf(Humanoid):
    
    def __init__(self, height, weight, hair_color, eye_color, str, dex, const, intel, wis, cha):
        super().__init__(height, weight, hair_color, eye_color, str, dex, const, intel, wis, cha)
        self.__Resistance = "100% Resistance to Sleep"
        
    def getResistance(self):
        return self.__Resistance
    
    def addRacialMod(self):
        super().setDex(super().getDex() + 2)
        super().setCha(super().getCha() + 2)
        
class Dwarf(Humanoid):
    def __init__(self, height, weight, hair_color, eye_color, str, dex, const, intel, wis, cha):
        super().__init__(height, weight, hair_color, eye_color, str, dex, const, intel, wis, cha)
        self.__resistance = "20% Resistance to magic"
        
    def addRacialMod(self):
        super().setStr(super().getStr() + 2)
        super().setConst(super().getConst() + 2)
        
    def subRacialMod(self):
        super().setCha(super().getCha() - 2)
        
    def getResistance(self):
        return self.__resistance
        
def characterCreator():
    #Generating valuables for later use
    races = {1: 'Human', 2: 'Elf', 3: 'Dwarf'}
    user_Race = ""
    user_Weight = 0
    user_Height = 0
    user_Hair_Color = ""
    user_Eye_Color = ""
    user_Str = 0
    user_Dex = 0
    user_Const = 0
    user_Int = 0
    user_Wis = 0
    user_Charisma = 0
    
    print("Welcome to the D&D 6e Charactor Creator! This is a simple RPG simulator written in Python. Please choose from the following playable races")
    for key in races:
        print(f"{key}: {races[key]}")
    
    user_Race = getUserRace(races)
    user_Height = getUserHeight()
    user_Weight = getUserWeight()
    user_Hair_Color = getUserHairColor()
    user_Eye_Color = getUserEyeColor()
    
    print("***Now randomly rolling stat attributes for your character")
    user_Str = random.randint(1, 18)
    user_Dex = random.randint(1, 18)
    user_Const = random.randint(1, 18)
    user_Int = random.randint(1, 18)
    user_Wis = random.randint(1, 18)
    user_Charisma = random.randint(1, 18)
    
    if user_Race == "Human":
      character = humanGenerator(user_Height, user_Weight, user_Hair_Color, user_Eye_Color, user_Str, user_Dex, user_Const, user_Int, user_Wis, user_Charisma)
      print("Your human has the following stats:")
      print(f"Height: {character.getHeight()}")
      print(f"Weight: {character.getWeight()}")
      print(f"Hair Color: {character.getHairColor()}")
      print(f"Eye Color: {character.getEyeColor()}")
      print(f"Strength: {character.getStr()}")
      print(f"Dexterity: {character.getDex()}")
      print(f"Constitution: {character.getConst()}")
      print(f"Intelligence: {character.getIntel()}")
      print(f"Wisdom: {character.getWis()}")
      print(f"Charisma: {character.getCha()}")
      
      print(f"As a human, you picked the {character.getMod()} stat to add the +2 bonus, so here are your final attributes")
      character.addMod()
      print(f"Height: {character.getHeight()}")
      print(f"Weight: {character.getWeight()}")
      print(f"Hair Color: {character.getHairColor()}")
      print(f"Eye Color: {character.getEyeColor()}")
      print(f"Strength: {character.getStr()}")
      print(f"Dexterity: {character.getDex()}")
      print(f"Constitution: {character.getConst()}")
      print(f"Intelligence: {character.getIntel()}")
      print(f"Wisdom: {character.getWis()}")
      print(f"Charisma: {character.getCha()}")
    elif user_Race == "Elf":
        character = elfGenerator(user_Height, user_Weight, user_Hair_Color, user_Eye_Color, user_Str, user_Dex, user_Const, user_Int, user_Wis, user_Charisma)
        print("Your elf has the following stats: ")
        print(f"Height: {character.getHeight()}")
        print(f"Weight: {character.getWeight()}")
        print(f"Hair Color: {character.getHairColor()}")
        print(f"Eye Color: {character.getEyeColor()}")
        print(f"Strength: {character.getStr()}")
        print(f"Dexterity: {character.getDex()}")
        print(f"Constitution: {character.getConst()}")
        print(f"Intelligence: {character.getIntel()}")
        print(f"Wisdom: {character.getWis()}")
        print(f"Charisma: {character.getCha()}")
        
        print("As an elf, you gain a resistance to sleep and gain +2 to your dexterity and charisma. Here are your final stats:")
        character.addRacialMod()
        print(f"Height: {character.getHeight()}")
        print(f"Weight: {character.getWeight()}")
        print(f"Hair Color: {character.getHairColor()}")
        print(f"Eye Color: {character.getEyeColor()}")
        print(f"Strength: {character.getStr()}")
        print(f"Dexterity: {character.getDex()}")
        print(f"Constitution: {character.getConst()}")
        print(f"Intelligence: {character.getIntel()}")
        print(f"Wisdom: {character.getWis()}")
        print(f"Charisma: {character.getCha()}")
        print(character.getResistance())
    elif user_Race == "Dwarf":
        character = dwarfGenerator(user_Height, user_Weight, user_Hair_Color, user_Eye_Color, user_Str, user_Dex, user_Const, user_Int, user_Wis, user_Charisma)
        print("Your dwarf has the following stats: ")
        print(f"Height: {character.getHeight()}")
        print(f"Weight: {character.getWeight()}")
        print(f"Hair Color: {character.getHairColor()}")
        print(f"Eye Color: {character.getEyeColor()}")
        print(f"Strength: {character.getStr()}")
        print(f"Dexterity: {character.getDex()}")
        print(f"Constitution: {character.getConst()}")
        print(f"Intelligence: {character.getIntel()}")
        print(f"Wisdom: {character.getWis()}")
        print(f"Charisma: {character.getCha()}")
        
        print("As a dwarf, you gain a resistance to magic, gain +2 to your strength and constitution, and lose -2 to charisma. Here are your final stats:")
        character.addRacialMod()
        character.subRacialMod()
        print(f"Height: {character.getHeight()}")
        print(f"Weight: {character.getWeight()}")
        print(f"Hair Color: {character.getHairColor()}")
        print(f"Eye Color: {character.getEyeColor()}")
        print(f"Strength: {character.getStr()}")
        print(f"Dexterity: {character.getDex()}")
        print(f"Constitution: {character.getConst()}")
        print(f"Intelligence: {character.getIntel()}")
        print(f"Wisdom: {character.getWis()}")
        print(f"Charisma: {character.getCha()}")
        print(character.getResistance())
        
      

#I split the code up into functions for use in the GUI portion later   
def getUserRace(races):
    while True:
        try:
            user_RaceChoice = int(input("Please choose your race for your character(Use 1, 2, or 3): "))
        except ValueError:
            print("Please use numbers") 
        else:   
            if user_RaceChoice != 1 and user_RaceChoice != 2 and user_RaceChoice != 3:
                print("Please use 1, 2, or 3")
            else:
                user_Race = races[user_RaceChoice]
                print(f"Your chosen race is {races[user_RaceChoice]}")
                break
    
    return user_Race

def getUserHeight():
    while True:
        try:
            user_Height = int(input("Please enter your character's height! (Please input a number between 3 to 7 ft): "))
        except ValueError:
            print("Please use real numbers")
        else:
                if user_Height < 3 or user_Height > 7:
                    print("Please put a number between 3 and 7 feet")
                else:
                    print(f"Your character's height is {user_Height} feet")
                    break
        
    return user_Height

def getUserWeight():
    while True:
        try:
            user_Weight = int(input("Please enter your character's weight! (Please input a number between 60 to 300 lbs): "))
        except ValueError:
            print("Please use real numbers")
        else:
                if user_Weight < 60 or user_Weight > 300:
                    print("Please put a number between 60 and 300 lbs")
                else:
                    print(f"Your character's height is {user_Weight} lbs")
                    break
        
    return user_Weight

def getUserHairColor():
    possible_Colors = {1: "white", 2: "silver", 3: "gray", 4: "black", 5: "brown", 6: "green", 7: "blue", 8: "yellow", 9: "pink", 10: "red", 11: "blonde"}
    userChoice = 0
    print("Here are the possible hair colors")
    
    for key in possible_Colors:
        print(f"{key}: {possible_Colors[key]}")
        
    while True:
        try:
            userChoice = int(input("Please enter the number of your chosen color: "))
        except ValueError:
            print("Please use whole numbers")
        else:
            if userChoice < 1 or userChoice > 11:
                print("Please use the valid range from 1 to 11")
            else:
                print(f"Your chosen hair color is {possible_Colors[userChoice]}")
                break
    
    return possible_Colors[userChoice]

def getUserEyeColor():
    possible_Colors = {1: "white", 2: "black", 3: "red", 4: "green", 5: "blue", 6: "brown", 7: "purple", 8: "amber"}
    userChoice = 0
    print("Here are the possible eye colors")
    
    for key in possible_Colors:
        print(f"{key}: {possible_Colors[key]}")
    
    while True:
        try:
            userChoice = int(input("Please enter the number of your chosen eye color: "))
        except ValueError:
            print("Please use whole numbers")
        else:
            if userChoice < 1 or userChoice > 8:
                print("Please use the valid range from 1 to 8")
            else:
                print(f"Your chosen eye color is {possible_Colors[userChoice]}")
                break
            
    return possible_Colors[userChoice]
                
def humanGenerator(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
    userModChoice = 0
    stats = {1: 'Strength', 2: "Dexterity", 3: "Constitution", 4: "Intelligence", 5: "Wisdom", 6: "Charisma"}
    print("Here are your stats:")
    print(f"1: Strength - {strength}")
    print(f"2: Dexterity - {dexterity}")
    print(f"3: Constitution - {constitution}")
    print(f"4: Intelligence - {intelligence}")
    print(f"5: Wisdom - {wisdom}")
    print(f"6: Charisma - {charisma}")

    while True:
        try:
            userModChoice = int(input("Please enter the number of the stat you would like to modify"))
        except ValueError:
            print("Please use whole numbers")
        else:
            if userModChoice < 1 or userModChoice > 6:
                print("Please use the numbers from 1 to 6")
            else:
                print(f"The stat you chose to modify is {stats[userModChoice]}")
                break
            
    character = Human(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma, stats[userModChoice])
    return character

def elfGenerator(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
    character = Elf(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
    return character

def dwarfGenerator(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
    character = Dwarf(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
    return character
        
if __name__ == "__main__":
    characterCreator()