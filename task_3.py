
def zeros(n: int):
    facto: int = 1
    result: int = 0
    for i in range(1, n+1):
        facto *= i
    for i in reversed(tuple(str(facto))):
        if i == '0':
            result += 1
        else:
            return result

def test_zeros(zeros):
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7
