# 병행성(Concurrency)
# 이터레이터, 제네레이터

# 반복 가능한 타입
# collections, text file, list, dict, set, tuple, unpacking, *args... : iterable

t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for c in t:
    print(c, end=' ')
print()
# 반복 가능한 이유? -> iter(x) 함수 호출

w = iter(t)
print(w)
while True:
    try:
        print(next(w), end=' ')
    except StopIteration:
        break
print()

# 반복형 확인
from collections import abc

print('__iter__' in dir(t))
print(hasattr(t, '__iter__'))
print(isinstance(t, abc.Iterable))
print()

class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        #print('Callef __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration.')
        self._idx += 1
        return word

    def __repr__(self):
        return 'WordSplit(%s)'%(self._text)

wi = WordSplitter('Do Today What You Could Do Tommorrow')
print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가될 경우 메모리 사용량 증가 -> 제네레이터 사용 권장
# 2. 단위 실행 가능한 코루틴(Corutine) 구현과 연동
# 3. 작은 메모리 조각을 사용

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word # 제네레이터
        return

    def __repr__(self):
        return 'WordSplitGenerator(%s)'%(self._text)

wg = WordSplitGenerator('Do Today What You Could Do Tommorrow')
wt = iter(wg)
print(wt, wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))

# 병행성 : 한 컴퓨터가 여러일을 동시에 수행 -> 단일 프로그램 안에서 여러일을 쉽게 처리
# 병렬성 : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도 증가

# Generator

def generator_ex1():
    print('Start')
    yield 'A Point' # return의 역할을 함
    print('Continue')
    yield 'B Point'
    print('End')

temp = iter(generator_ex1())

for v in generator_ex1():
    print(v)

print([x * 3 for x in generator_ex1()])
for i in (x * 3 for x in generator_ex1()):
    print(i)