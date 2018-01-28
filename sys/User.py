class User:
    # User has:
        # Name
        # Queue time
        # Phone
        # Location
    def __init__(self, name, phone, pw):
        self.name = name
        self.password = pw
        self.phone = phone

    def enterQueue(self, time):
        self.rank = time

    def setLocation(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    # Increase Queue time ? (Tree set?)
