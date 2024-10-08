class user:
    def __init__(self):
        self.usertype = "Guest"

    def register(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f'User(\'{self.username}\',{self.usertype},{self.email})'
    