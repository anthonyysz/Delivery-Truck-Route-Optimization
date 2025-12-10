
class Package: #Creating the Package class, with each attribute that will be necessary
    def __init__(self, idnum, address, city, state, zipcode, deadline, weight, notes):
        self.idnum = idnum
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.truck = None
        self.status = None
        self.delivery_time = None
        