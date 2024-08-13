# 함수형 프로그래밍 : 컴퓨터 프로그래밍을 함수와 함수간의 연산으로 간주하여 접근하는 방법
# 일급함수(First-Class Functions) : 함수를 변수에 할당하거나 함수의 인자로 다른 함수에 전달하고,
#                                 함수를 다른 함수의 반환 값으로 사용
# 불변성 : 함수형 프로그래밍에서 데이터는 불변해야 함, 한번 생성된 데이터는 변경되지 않으며,


# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달
# 4. 함수 결과 반환 (return)

def factorial(n):
    """Factorial Function -> n : int"""
    if n == 1:
        return 1
    return n * factorial(n - 1)


class A:
    pass


print(factorial(5))
print(factorial.__doc__)
print(type(factorial), type(A))
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))  # 함수만 가진 성질
print(factorial.__name__)
print(factorial.__code__)

print()
print()

# 변수 할당 가능?
var_func = factorial
print(var_func)
print(var_func(10))
print(list(map(var_func, range(1, 11))))

print()
print()

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order function)
# map, filter, reduce
print(list(map(var_func, filter(lambda x: x % 2, range(1, 6)))))
print([var_func(i) for i in range(1, 6) if i % 2])

from functools import reduce
from operator import add

print(reduce(add, range(1, 11)))
print(sum(range(1, 11)))

# 익명함수(lambda)
# 가급적 주석 작성, 가급적 함수 작성
# 일반 함수 형태로 리팩토링 권장
print(reduce(lambda x, t: x + t, range(1, 11)))

# callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
print(callable(str), callable(A), callable(var_func), callable(3.14))

# partial : 인수 고정 -> 콜백 함수 사용
from operator import mul
from functools import partial

print(mul(10, 10))
five = partial(mul, 5)  # 5 * ?
six = partial(five, 6)

print(five(10))
print(six())
# print(six(2)) # 에러, 이미 2개의 인자가 고정되었기 때문

print([five(i) for i in range(1, 11)])

print()
print()

# 파이썬 변수 범위(scope)
# global
g = 30
def func_v1(a):
    # local
    global g
    print(a)
    print(g)
    g = 40

print('g >>', g)
func_v1(10)
print('g >>', g)

# 클로저(Clouser) 사용 이유
# 서버 프로그래밍 -> 동시성(Concurrency)제어 -> 메모리 공간에 여러 자원이 접근 -> 교착상태(Dead Lock)
# 메모리를 공유하지 않고 메시지 전달로 처리하기 위한 언어 등장 -> 클로저는 종료시에 값을 기억함(상태를 기억)
# 클로저는 공유하되 변경되지 않는(Immutable, Read Only) -> 함수형 프로그래밍과 연결됨
# 클로저는 불변자료구조 및 atom, stm -> 멀티스레스(Coroutine) 프로그래밍에 강점이 되는 병행성 처리


class Averager():
    # 클래스로 함수는 종료되었지만 값을 기억하도록 구현
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)


averager_cls = Averager()

print(averager_cls(10))
print(averager_cls(20))
print(averager_cls(30))


def closure_ex1():
    # 자유 변수
    # 클로저 영역
    series = []
    def averager(v):
        series.append(v)
        print('inner >> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    # 함수 자체를 리턴해서 함수의 바깥 영역을 계속 기억
    return averager


avg_closure1 = closure_ex1()

print(avg_closure1(20))
print(avg_closure1(40))
print(avg_closure1(60))

# function inspection
print(dir(avg_closure1))
print(dir(avg_closure1.__code__))
print(avg_closure1.__code__.co_freevars)    # 자유변수 출력
print(avg_closure1.__closure__[0].cell_contents)    # [20, 40, 60] 값을 가지고 있음

# 잘못된 클로저 사용 -> 사용 가능하게 변경(비추)
def closure_ex2():
    # free variable
    cnt = 0
    total = 0
    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt
    return averager


avg_closure2 = closure_ex2()
print(avg_closure2(10))
print(avg_closure2(20))
print(avg_closure2(30))

# 데코레이터(정말 중요!) -> 클로저 이해해야 함
# 1. 중복제거, 코드 간결, 공통 함수(로깅, 프레임워크, 유효성 체크 등) 작성
# 2. 특정 기능에 한정된 함수는 단일 함수로 작성하는것이 유리, 디버깅 불편

import time

def perf_clock(func):
    def perf_clocked(*args):
        # 함수 시작 시간
        st = time.perf_counter()
        # 함수 실행
        result = func(*args)
        # 함수 종료 시간
        et = time.perf_counter() - st
        # 실행 함수명
        name = func.__name__
        # 함수 매개변수
        arg_str = ', '.join(repr(arg) for arg in args)
        # 결과 출력
        print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))
        return result
    return perf_clocked


def time_func(seconds):
    time.sleep(seconds)

def sum_func(*numbers):
    return sum(numbers)

# 데코레이터 미사용
none_deco1 = perf_clock(time_func)
none_deco2 = perf_clock(sum_func)

print('-'*40, 'Called None Decorator -> time_func')
none_deco1(1.5)

print('-'*40, 'Called None Decorator -> sum_func')
none_deco2(100, 200, 300, 400, 500)

# 데코레이터 사용
@perf_clock
def time_func(seconds):
    time.sleep(seconds)

@perf_clock
def sum_func(*numbers):
    return sum(numbers)

print('-'*40, 'Called Decorator -> time_func')
time_func(1.5)

print('-'*40, 'Called Decorator -> sum_func')
sum_func(100, 200, 300, 400, 500)