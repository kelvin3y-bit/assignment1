class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.strength = 100

    def introduce(self):
        print f"I am{self.name} has the power of {self.power}"

    def fight(self):
        print f"{self.name} is fighting with strength {self.strength}!"

class FlyingHero(Superhero):
    def __init__(self, name, power, flight_speed):
        super().__init__(name, power)
        self.flight_speed = flight_speed

    def fly(self):
        print f"{self.name} is flying at a speed of {self.flight_speed}!"

#instances
hero1 = Superhero("Superman", "super strength")
hero2 = FlyingHero("Ironman", "high-tech suit", 300)

#test
hero1.introduce()   
hero1.fight()

hero2.introduce()
hero2.fight()

