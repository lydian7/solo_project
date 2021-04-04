import random

class Manufacturer:
    def __init__(self, name, type, address = "01 Manufacturer Plaza", email = "toby@company.com", contact_person = "Toby Flenderson", telephone = "07989345265", active = True, id = None):
        self.name = name
        self.type = type
        self.address = address
        self.telephone = telephone
        self.email = email
        self.contact_person = contact_person
        self.active = active
        self.id = id

