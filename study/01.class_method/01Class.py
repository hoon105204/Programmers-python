class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 're : {} - {}'.format(self._company, self._details)

    def __reduce__(self):
        pass


car1 = Car('Ferrari1', {'color': 'White1', 'horsepower': 4001, 'price': 80001})
car2 = Car('Ferrari2', {'color': 'White2', 'horsepower': 4002, 'price': 80002})
car3 = Car('Ferrari3', {'color': 'White3', 'horsepower': 4003, 'price': 80003})

print(car1)
print(car2)
print(car3)

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

print()
print()

car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)


