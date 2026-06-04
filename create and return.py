class car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def display(self):
         print(f"brand:{self.brand},speed:{self.speed}km\h")
def create_car():
        car1=car("joyota",180)
        return car1
mycar=create_car()
mycar.display()
