import random 

class Soldier:  
    def __init__(self, name, health=100):  
        self.name = name
        self.health = health
        
    def attack(self, enemy):
        damage = 10
        enemy.health -= damage
        print("SLASH !") 
        print(f"{self.name} attacks {enemy.name}!, [-{damage}HP]")
        print(f"{enemy.name}'s health: {max(0, enemy.health)}")

class Archer(Soldier):  
    def __init__(self, name, range=5, health=80):
        self.range = range
        super().__init__(name, health)

    def attack(self, enemy): 
        print("Headshot!")
        damage = 7
        enemy.health -= damage
        print(f"{self.name} shoots {enemy.name}!, [-{damage}HP]")
      
        if random.random() < 0.4:
            enemy.health -= damage
            print(f"{self.name} shoots a second arrow at {enemy.name} [-{damage}HP]")
        print(f"{enemy.name}'s health: {max(0, enemy.health)}")

class Cavalry(Soldier):
    def __init__(self, name, health=120, speed=8):
        super().__init__(name, health)
        self.speed = speed
        
    def attack(self, enemy):
        print("CHARGE!!")
        damage = 15
        enemy.health -= damage
        print(f"{self.name} charges at {enemy.name}!. [-{damage}HP]")
        print(f"{enemy.name}'s health: {max(0, enemy.health)}")

# Battle
def fight_to_death(army, enemy):
    print("🔥 BATTLE COMMENCES 🔥")
    round_num = 1
    
    while True:
        print(f"\n------ ROUND {round_num} ------")
        round_num += 1
        
        # Your army attacks
        for unit in army:
            if unit.health > 0 and enemy.health > 0:
                unit.attack(enemy)
                
        # Check if enemy is defeated
        if enemy.health <= 0:
            print(f"\n🏆 YOUR ARMY WINS!")
            break
            
        # Enemy attacks a random living unit
        if enemy.health > 0:
            living_units = [u for u in army if u.health > 0]
            if living_units:
                target = random.choice(living_units)
                print(f"\n⚔️ {enemy.name} counterattacks!")
                damage = 25  
                target.health -= damage
                print(f"{enemy.name} strikes {target.name}! [-{damage}HP]")
                print(f"{target.name}'s health: {max(0, target.health)}")
                
                # Check if your army is defeated
                if all(unit.health <= 0 for unit in army):
                    print(f"\n💀 The enemy stands victorious...")
                    break


enemy = Soldier("Titan")
your_army = [Soldier("Shadow"), Archer("Ussop"), Cavalry("Prince")]

# Start Battle
fight_to_death(your_army, enemy)
