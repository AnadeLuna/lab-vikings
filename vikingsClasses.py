
# Soldier


class Soldier:
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.health -= damage 

# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        super().__init__(health,strength)
        self.name = name
    def attack(self):
         return super().attack()
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon (Soldier):
    def __init__(self,health,strength):
        super().__init__(health,strength)
    def attack(self):
        return super().attack()
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else: 
            return "A Saxon has died in combat"


# War
import random

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = [] 
    
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)
    
    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)
    
    
    def vikingAttack(self):
        choiceSaxon = random.choice(self.saxonArmy)
        choiceViking = random.choice(self.vikingArmy)
        attackv = choiceSaxon.receiveDamage(choiceViking.attack())
        healthViking = choiceViking.attack() 
        if healthViking >= 0:
            self.saxonArmy.remove(choiceSaxon)
        return attackv
    
    def saxonAttack(self):
        choiceSaxon = random.choice(self.saxonArmy)
        choiceViking = random.choice(self.vikingArmy)
        attacks = choiceViking.receiveDamage(choiceSaxon.attack())
        healthSaxon = choiceSaxon.attack()
        if healthSaxon >= 0:
            self.vikingArmy.remove(choiceViking)     
        return attacks
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
            return "Vikings and Saxons are still in the thick of battle."



        
        





        

    









    
