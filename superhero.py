class Heroes:
    def __init__(self, name, age, grade, health, damage):
        self.name = name
        self.age = age
        self.grade = grade
        self.damage = damage
        self.is_alive = True
        self.health = health

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def attack(self,opponent):
        opponent.health = opponent.health - self.damage


spiderman = Heroes("spiderman",25.5, "12th", 30, 1000)
villan = Heroes("someone", 1, "9th", 50, 10000)


print(f"Spiderman has:", spiderman.health, "health")