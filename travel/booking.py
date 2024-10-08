import datetime

class booking:
    def __init__(self, startdate, enddate, city, user):
        self.startdate = startdate
        self.enddate = enddate
        self.city = city
        self.user = user
        self.num_guests = 1

    def __repr__(self):
        return f'Booking({self.startdate},{self.enddate},{self.city},{self.user},{self.num_guests})'