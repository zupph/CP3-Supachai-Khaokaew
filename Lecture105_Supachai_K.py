class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirCondition(self):
        print("turn on : Air")

class Car(Vehicle):
    def turnOnAir(self):
        print("Car ", end="")
        car = Vehicle()
        car.turnOnAirCondition()

class Van(Vehicle):
    def vanTurnOnAir(self):
        print("Van ", end="")
        van = Vehicle()
        van.turnOnAirCondition()

class Pickup(Vehicle):
    def pickupTurnOnAir(self):
        print("Pickup ", end="")
        pickup = Vehicle()
        pickup.turnOnAirCondition()

class Estatecar(Vehicle):
    def turnOnAir(self):
        print("Estatecar ", end="")
        estatecar = Vehicle()
        estatecar.turnOnAirCondition()

car1 = Car()
car1.turnOnAir()
van1 = Van()
van1.vanTurnOnAir()
pickup1 = Pickup()
pickup1.pickupTurnOnAir()
estatecar1 = Estatecar()
estatecar1.turnOnAir()
