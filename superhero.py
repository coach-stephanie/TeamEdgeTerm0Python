from curses import mouseinterval


class Superhero:
    def _init_(self,power,name, years_of_experience,partners,mortal_enemy):
        self.power = "Wherewolf"
        self.name = "Wolverine"
        self. years_of_experience = 4
        self.partners = ["Silver Surfer","Poison Ivy","Wonder Woman"]
        self.mortal_enemy = "Red Skull",
        self.health_points = 10,
        #self.attack_damage = damage

    def intro(self):
        return f"Name: {self.name},power:{self.power},mortal enemy:{self.mortal_enemy}"

    def attack(self,enemy):
        enemy.health_points = enemy.health_points-1
    
    def heal(self):
        self.health_points = self.health_points+1

        
    def defense(self):
        self.health_points = self.health_points+0

    def is_alive(self,enemy):   
        self.is_alive() and enemy.is_alive()
        self.attack(enemy)
        enemy.attack(self)
        if self.is_alive():
        print: