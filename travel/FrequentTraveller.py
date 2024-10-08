from travel.user import user

class FrequentTraveller(user):
    def __init__(self):
        super().__init__()
        self.user_type = "Frequent Traveller"
        self.travellerID = None

    def register(self, username, password, emailID, travellerID):
        super().register(username, password, emailID)
        self.travellerID = travellerID

    def __repr__(self):
        return f'FrequentTraveller(\'{self.username}\',\'{self.user_type}\',\'{self.email}\',\'{self.travellerID}\')'
