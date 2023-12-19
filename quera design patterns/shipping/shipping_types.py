from interfaces import ShippingType
from shipping_vehicles import Car, Truck, Motorcycle


class NormalShippingType(ShippingType):
    def create_vehicle(self):
        return Car()
    
class HeavyShippingType(ShippingType):
    def create_vehicle(self):
        return Truck()
    
class QuickShippingType(ShippingType):
    def create_vehicle(self):
        return Motorcycle()
