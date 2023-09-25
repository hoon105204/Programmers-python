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
print(callable(str), callable(A),  callable(var_func), callable(3.14))

# partial : 인수 고정 -> 콜백 함수 사용
from operator import mul
from functools import partial

print(mul(10, 10))
five = partial(mul, 5)  # 5 * ?

print(five(10))





