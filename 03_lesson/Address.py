class Address:
     
     def __init__(self, postcode, city, street, house, apartament):
        self.postcode = postcode
        self.city = city
        self.street = street
        self.house = house
        self.apartament = apartament

     def __str__(self):
         return (f"{self.postcode}, {self.city}, {self.street},"
                 f"{self.house}, {self.apartament}")