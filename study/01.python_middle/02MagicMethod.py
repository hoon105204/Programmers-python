# 파이썬의 핵심 : 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)
# Special Method(Magic Method) : 클래스 안에 정의할 수 있는 특별한(Built-in) 메서드

# 기본형
print(int)
print(float)

# 모든 속성 및 메서드 출력
print(dir(int))
print(dir(float))

n = 10

print(type(n))
print(n + 100, n.__add__(100))
print(bool(n), n.__bool__())
print(n * 100, n.__mul__(100))


# 클래스 예제 1
class Fruit():
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info : {}, {}'.format(self._name, self._price)

    def __add__(self, other):
        print('called >> __add__')
        return (self._price + other._price) * 0.8

    def __sub__(self, other):
        print('called >> __sub__')
        return self._price - other._price

    def __le__(self, other):
        print('called >> __le__')
        if self._price <= other._price:
            return True
        else:
            return False

    def __ge__(self, other):
        print('called >> __ge__')
        if self._price >= other._price:
            return True
        else:
            return False


s1 = Fruit('Orange', 8000)
s2 = Fruit('banana', 7000)

# 원하는 매직 메서드 새롭게 구현
print(s1 + s2)
print(s1 - s2)
print(s1 >= s2)
print(s1 <= s2)
print(s1)


# 클래스 예제2
class Vector(object):
    def __init__(self, *args):
        """
        Create a vector, example : v = Vector(5,10)
        """
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        """
        Return thr vector information.
        """
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        """
        Return the Vector add on self and other
        """
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, other):
        return Vector(self._x * other, self._y * other)

    def __bool__(self):
        return bool(max(self._x, self._y))


# Vector 인스턴스
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()

# 매직메서드 출력
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)
print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(bool(v1), bool(v2), bool(v3))

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(l_leng1)

# 네임드 튜플 사용
# 일반적인 튜플에 값 추가 하는 상황 방지 가능
from collections import namedtuple

Point = namedtuple('Pt', ['x', 'y'])
Point = namedtuple('Pt', 'x y')
Point = namedtuple('Pt', 'x, y')
pt3 = Point(1.0, 5.0)
pt4 = Point(x=2.5, y=1.5)

# 인덱스&키 접근 가능
print(pt3, pt3.x, pt3[0])

# 딕셔너리 언패킹해서 x와 y에 값이 들어가도록
temp_dict = {'x': 75, 'y': 55}
p5 = Point(**temp_dict)

temp = [52, 38]
# 네임드 튜플 메서드
# _make() : 새로운 객체 생성
p4 = Point._make(temp)
print(p4)

# _fields : 필드 네임 확인
print(p4._fields)

# _asdict() : OrderdDict 반환
print(p4._asdict())

Classes = namedtuple('Classes', ['rank', 'number'])

numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

print(numbers, ranks)

students = [Classes(rank, number) for rank in ranks for number in numbers]

print(students)

# 추천
students2 = [Classes(rank, number)
             for rank in 'A B C D'.split()
             for number in [str(n)
                            for n in range(1, 21)]]
print(students2)
