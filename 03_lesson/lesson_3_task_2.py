from smartphone import Smartphone


catalog = []
    
catalog.append(Smartphone("Samsung", "Galaxy11", "8-999-123-45-67"))
phone = Smartphone("Xiaomi", "13_C", "8-999-444-45-55")
phone = Smartphone("Xiaomi", "14_T", "8-900-444-45-87")
phone = Smartphone("Xiaomi", "8_Pro", "8-960-444-88-88")
phone = Smartphone("Realmi", "61", "8-927-095-63-65")


for smartphone in catalog:
   print(f'{phone.phone_brand}, {phone.phone_model}, {phone.number}')