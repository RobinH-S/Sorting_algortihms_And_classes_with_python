class Flight:

    def __init__(self, origin, destination, airline, number):
        self.origin = origin
        self.destination = destination
        self.airline = airline
        self.number = number

    def get_origin(self):
        return self.origin
    def get_destination(self):
        return self.destination

    def get_airline(self):
        return self.airline
    def get_number(self):
        return self.number
    def set_origin(self, newOrigin):
        self.origin = newOrigin

    def set_destination(self, new_destination):
        self.destination = new_destination

    def set_number(self, new_number):
        self.number = new_number

    def set_airline(self, new_airline):
        self.airline = new_airline


airline = Flight('Bergen' , 'Paris', 'SAS', 'Sk5049')
print(airline.get_origin() ,'going to', airline.get_destination(), 'with' , airline.get_airline(), 'flightnr. ' , airline.get_number())