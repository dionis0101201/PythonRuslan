from Address import Address
from Mailing import Mailing

to_address = Address("153750", "Пенза", "Ленина", "45", "121") 
from_address = Address("111323", "Мадрид", "Луночарского", "155", "28")
mailing = Mailing("258258", from_address, to_address, "323")

print(mailing)