class Person:
    def __init__(self, role, can_ride):
        self.role = role
        self.can_ride = can_ride 
    
    def show(self):
        return("Role: {}".format(self.role))