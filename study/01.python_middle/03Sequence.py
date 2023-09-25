# list comprehending
chars = '+_)(*&^%$#@!'
code_list = [ord(s) for s in chars if ord(s) > 40]
print(code_list)

# map, Filter 이용
code_list = list(filter(lambda x: x > 40, map(ord, chars)))
print(code_list)

# Generator -> 반복가능한(iterable) 객체를 만들기 위한 도구
# 처음부터 메모리를 차지하는 것이 아닌 하나씩 불러와 이용함, 메모리를 효율적으로 이용
import array

tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))

print(type(tuple_g))
print(next(tuple_g))
print(type(array_g))
print(array_g.tolist())

print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s, end=' ')
print()

# 리스트 주의
marks1 = [['~'] * 3 for _ in range(4)]
marks2 = [['~'] * 3] * 4
print(marks1)
print(marks2)

# 수정
marks1[0][1] = 'x'
marks2[0][1] = 'x'  # 의도하지 않은 변경이 이뤄짐, 하나의 아이디 값을 가진 리스트가 복사가 된것이라서
print(marks1)
print(marks2)

# 증명
print([id(i) for i in marks1])
print([id(i) for i in marks2])

# 튜플 advanced
# unpacking
print(divmod(100, 9))
# print(divmod((100, 9))) 에러남
print(divmod(*(100, 9)))
print(*(divmod(*(100, 9))))

x, y, *rest = range(10)
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)

# 가변 불변
l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2

print(l, id(l))
print(m, id(m))

l *= 2
m *= 2

print(l, id(l))
print(m, id(m))

# 정렬
f_list = ['banana', 'strawberry', 'mango', 'apple', 'coconut']
print('sorted - ', sorted(f_list))
print('sorted - ', sorted(f_list, reverse=True))
print('sorted - ', sorted(f_list, key=len))
print('sorted - ', sorted(f_list, key=lambda x: x[-1]))
print('sorted - ', sorted(f_list, key=lambda x: x[-1], reverse=True))

print(f_list)  # 원본이 바뀌지 않음

print('sort - ', f_list.sort(), f_list)
print('sort - ', f_list.sort(reverse=True), f_list)
print('sort - ', f_list.sort(key=len), f_list)
print('sort - ', f_list.sort(key=lambda x: x[-1]), f_list)
print('sort - ', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)

# list & array
# 리스트 : 융통성, 다양한 자료형, 범용적 사용
# array : 고속 연산, 리스트와 거의 호환

# 해시테이블
# key에 value를 저장하는 구조
# 파이썬 dict 해쉬 테이블
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조
# 키 값을 해싱 함수 -> 해쉬 주소 -> 키에 대한 value 참조

# print(__builtins__.__dict__)

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])
print(hash(t1))

# dict setdefault
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)

# Use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)

# 주의
new_dict3 = {k: v for k, v in source}
print(new_dict3)  # 덮어 씌어짐

# immutable Dict
from types import MappingProxyType

d = {'key1': 'value1'}

# read only, 수정 불가능
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))

# 집합 자료형
s1 = {'apple', 'apple', 'orange', 'kiwi', 'orange'}
s2 = set(['apple', 'apple', 'orange', 'kiwi', 'orange'])
s3 = {3}
s4 = set()  # not {} -> dict 자료형임
s5 = frozenset({'apple', 'apple', 'orange', 'kiwi', 'orange'})  # 데이터 변경 불가

s1.add('melon')

# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터 실행
from dis import dis

print('------')
print(dis('{10}'))
print('------')
print(dis('set([10])'))

# set comprehension
print({x for x in range(1, 11) if x % 2 == 0})
