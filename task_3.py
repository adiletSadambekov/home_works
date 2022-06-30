from math import factorial
def zeros(n: int):
    facto: int = factorial(n)
    result: int = 0
    for i in reversed(tuple(str(facto))):
        if i == '0':
            result += 1
        else:
            return result

def test_zeros(zeros):
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7
