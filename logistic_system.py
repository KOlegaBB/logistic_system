"""
Logistic system
"""
from random import randint


class Item:
    """
    Class for items
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} costs {self.price} UAH."


class Vehicle:
    """
    Class for vehicles
    """
    def __init__(self, vehicleNo, isAvailable=True):
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable


class Location:
    """
    Class for locations
    """
    def __init__(self, city, postoffice):
        self.city = city
        self.postoffice = postoffice


class Order:
    """
    Class for orders
    """
    def __init__(self, user_name, city, postoffice, items):
        self.orderId = randint(99999999, 1000000000)
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = items
        self.vehicle = None

    def calculateAmount(self):
        """
        Calculate full price of all items
        :return: full price
        """
        amount = 0
        for item in self.items:
            amount += item.price
        return amount

    def assignVehicle(self, vehicle: Vehicle):
        """
        Assign vehicle for order
        """
        self.vehicle = vehicle
        vehicle.isAvailable = False

    def __str__(self):
        text = f"Your order number is {self.orderId}."
        return text


class LogisticSystem:
    """
    Class for logistic system
    """
    def __init__(self, vehicles):
        self.orders = []
        self.vehicles = vehicles

    def placeOrder(self, order: Order):
        """
        Find vehicle for order and place it
        """
        for vehicle in self.vehicles:
            if vehicle.isAvailable:
                order.assignVehicle(vehicle)
                self.orders.append(order)
                break
        if order not in self.orders:
            return "There is no available vehicle to deliver an order."

    def trackOrder(self, orderId):
        """
        Show where order will be delivered
        """
        text = None
        for order in self.orders:
            if order.orderId == orderId:
                text = f'Your order {order.orderId} is sent to ' \
                       f'{order.location.city}. Total price: ' \
                       f'{order.calculateAmount()} UAH.'
                break
        if text is None:
            return "No such order"
        return text
