#base
class vehicle:
    def move(self):
        print("The vehicle is moving")  

# derived class
class car(vehicle):
    def move(self):
        print("The car is moving")  

class plane(vehicle):
    def move(self):
        print("The plane is flying")        

class boat(vehicle):    
    def move(self):
        print("The boat is sailing")

# instances
vehicles = [car(), plane(), boat()]

foer v in vehicles:
    v.move()