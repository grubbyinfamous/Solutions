'''
Things to do:
Create a class called PlayerCharacter
Use the def __init__ method to create the following attributes
    Health from 1- 100
    Armor Rating
    Attack Power
    from 1-20
Create an object from PlayerCharacter called Wizard
Create a main() function that asks the user to input each of the values associated with the PlayerCharacter attributes
Print the Wizard's attributes
'''

class PlayerCharacter:
    
    #Here is where we will initialize the PlayerCharacter with the health, armor, and attack attributes
    def __init__(self, health, armor_rating, attack_power):
        self.health = health
        self.armor_rating = armor_rating
        self.attack_power = attack_power
        
    #The following methods will be used as accessor methods so that we can access the class' attributes
    def getHealth(self):
        return self.health
    
    def getArmor(self):
        return self.armor_rating
    
    def getAttack(self):
        return self.attack_power
    
    #The following methods will be used as mutator methods so that the user can modify the class' attributes
    def setHealth(self, mod_health):
        self.health = mod_health
        
    def setArmor(self, mod_armor):
        self.armor_rating = mod_armor
        
    def setAttack(self, mod_attack):
        self.attack_power = mod_attack

if __name__ == "__main__":
    
    print("Welcome to the Wizard creator program!")
    
    #Here is where the wizard will be created
    wizard = PlayerCharacter(1, 1, 1)
    print("Your current wizard's stats are: ")
    print(f"Health: {wizard.getHealth()}")
    print(f"Armor Rating: {wizard.getArmor()}")
    print(f"Attack Power: {wizard.getAttack()}")
    
    #This is the start of the section where the user will set the wizard's stats
    #I will use while loops and exception handling since users may not follow directions and I need to make sure that they do
    while True:
        try:
            mod_health = int(input("Please enter the wizard's heatlh from 1 to 100: "))  
        except ValueError:
            print("Please enter a number")
        else:
            if mod_health < 1 or mod_health > 100:
                 print("Please use a number between 1 and 100")
            else:
                wizard.setHealth(mod_health)
                break
    
    while True:
        try:
            mod_Armor = int(input("Please enter the wizard's armor rating from 1 to 20: "))  
        except ValueError:
            print("Please enter a number")
        else:
            if mod_Armor < 1 or mod_Armor> 20:
                 print("Please use a number between 1 and 100")
            else:
                wizard.setArmor(mod_Armor)
                break
    
    while True:
        try:
            mod_Attack = int(input("Please enter the wizard's attack power from 1 to 20: "))  
        except ValueError:
            print("Please enter a number")
        else:
            if mod_Attack < 1 or mod_Attack> 20:
                 print("Please use a number between 1 and 100")
            else:
                wizard.setAttack(mod_Attack)
                break
    
    print("Here is your wizard's current stats:")
    print(f"Health: {wizard.getHealth()}")
    print(f"Armor Rating: {wizard.getArmor()}")
    print(f"Attack Power: {wizard.getAttack()}")
    