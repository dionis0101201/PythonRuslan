from smartphone import Smartphone

catalog = [Smartphone("Samsung", "Galaxy11", "8-999-123-45-67"),
           Smartphone("Xiaomi", "13_C", "8-999-444-45-55"),
           Smartphone("Xiaomi", "14_T", "8-900-444-45-87"),
           Smartphone("Xiaomi", "8_Pro", "8-960-444-88-88"),
           Smartphone("Realmi", "61", "8-927-095-63-65")]

for smartphone in catalog:
    print(f'{smartphone.phone_brand}, {smartphone.phone_model}, {smartphone.number}')