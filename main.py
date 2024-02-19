import names
from random_address import real_random_address
import random
class Person:
    def __init__(self):
        self.name = names.get_first_name()
        self.last_name = names.get_last_name()
        self.address = real_random_address()
        self.straddress = self.address['address1'] + ", " + self.address['postalCode'] 
        self.email = self.randomEmail()

    def __str__(self):
        return f"{self.name} lives at {self.stradress}"
    def randomEmail(self):
        bothNames= random.choice([False,True])
        domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "protonmail.com", "yandex.com"]
        weights = [50, 5, 16, 20, 5, 4]  # Corresponding weights for each domain

        # Use random.choices() to select a domain based on the specified weights
        selected_domain = random.choices(domains, weights=weights, k=1)[0]
        caracter = ["_",".","__","",""]
        numbers = [str(random.randint(0,9)),str(random.randint(1980,2010))[2:],str(random.randint(1980,2010))] 
        selected_domain
        if bothNames:
            return self.name + random.choice(caracter) + self.last_name + random.choice(caracter) + numbers[random.randint(0,2)] + "@" + selected_domain
        else:
            return self.name + random.choice(caracter) + numbers[random.randint(0,2)] + "@" + selected_domain
        
        