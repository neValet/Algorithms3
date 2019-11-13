class Park:
    def __init__(self, address, bike_path_length, ticket_price):
        self.address = address
        self.bike_path_length = bike_path_length
        self.ticket_price = ticket_price

    def __repr__(self):
        return str(self.__dict__)
