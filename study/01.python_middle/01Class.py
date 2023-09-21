class Car():
    """
    Car class
    Author: kim
    Date: 2023.09.15
    자동차 클래스 ...
    """
    # 클래스 변수(모든 인스턴스가 공유)
    car_count = 0
    price_per_raise = 1.0

    # 인스턴스 변수(앞에 언더바를 붙여 구분)
    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 're : {} - {}'.format(self._company, self._details)

    def __del__(self):
        Car.car_count -= 1

    def __reduce__(self):
        pass

    # 인스턴스 매서드
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))

    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # 클래스 메서드(데코레이터가 붙음)
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('1보다 큰값 넣어라')
            return
        cls.price_per_raise = per
        print('Succeed! price increased.')

    # static 메서드
    # 유연한 함수를 구현
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'OK! This Car is {}'.format(inst._company)
        else:
            return 'Not Bmw!'


car1 = Car('Ferrari1', {'color': 'White1', 'horsepower': 4001, 'price': 80001})
car2 = Car('Bmw', {'color': 'White2', 'horsepower': 4002, 'price': 80002})
car3 = Car('Ferrari3', {'color': 'White3', 'horsepower': 4003, 'price': 80003})

print(car1)

# 클래스 변수 값 공유
print(car1.car_count)
print(car2.car_count)
print(car3.car_count)
print(Car.car_count)


print(id(car1))
print(id(car2))
print(id(car3))

# 해당 클래스가 가진 매직매서드(attr)를 모두 보여줌
# 상위 클래스로부터 상속받는 모든 것을 보여주지만 값은 안보여줌
# 클래스 변수 확인 가능
print(dir(car1))
print(dir(car2))

# 상속 받는 것을 제외하고, 현재 가지고 있는 값 포함 확인 가능
print(car1.__dict__)
print(car2.__dict__)

# 해당 클래스에 대한 정보글을 확인 가능
print(Car.__doc__)

# 직접 작성한 매서드 활용
car1.detail_info()
car2.detail_info()

# 비교 : Car 클래스의 아이디를 물어보므로 다 같음
print(car1.__class__, car2.__class__, car3.__class__)
print(id(car1.__class__), id(car2.__class__), id(car3.__class__))

# 에러 Car.detail_info() -> self 인자 전달해 줘야함
Car.detail_info(car1)
car1.detail_info()

# 삭제 확인
# del car2
# print(Car.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))

# 캡슐화에 맞지 않음 -> 직접 인스턴스 변수에 접근하는 것은 좋지 않음
# 변수값이 변경되면 프로그램에 영향을 줄 수 있기 때문
print(car1._details.get('price'))
print(car1._details['price'])

# 가격 인상전
print(car1.get_price())
print(car2.get_price())

# 가격 인상(직접 접근 좋지않음)
# Car.price_per_raise = 1.4

Car.raise_price(1.3)

# 가격 인상후
print(car1.get_price())
print(car1.get_price_culc())

print(car1.is_bmw(car1))
print(car1.is_bmw(car2))
print(car2.is_bmw(car2))
print(Car.is_bmw(car2))
