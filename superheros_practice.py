class Superheros:
    def __init__(self, power, name, age, sidekicks, villans, allies, health_points, damage):
        self.power = power
        self.name = name
        self.age = age
        self.sidekicks = sidekicks
        self.villans = villans
        self.allies = allies
        self.damage = damage
        self.health_points = 100


    def attack (self, villan):
        villan.health_points = villan.health_points - self.damage
        print(f"{self.name} has done damage to {villan.name}! {villan.name} now has {villan.health_points} HP!")
    

hero = Superheros("Electric Bow", "Fischl", "17", "Oz", "Hillichurls", "Traveler", 24 ["bow": 5, "elemental skill": 11, "elemental burst": 18])
villan = Superheros("Water Sword", "Tartaglia", "21", "N/A", "The government", "The Fatui", 19 ["sword": 6, "elemental skill": 13, "elemental burst": 20])

while hero.is_alive() and villan.is_alive():
    hero.attack(villan)
    villan.attack(hero)
