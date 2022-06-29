import functools

def count_find_num(primeLs, limit):
    result: int = 0
    result = functools.reduce(lambda a, b: a * b, primeLs)
    inter_result: list = list()
    if result < limit:
        inter_result.append(result)
    for i in inter_result:
        for n in primeLs:
            facto = n * i
            if facto <= limit:
                inter_result.append(facto)
    if inter_result:
        set_res = set(inter_result)
        result: list = [len(set_res), max(set_res)]
    else:
        result = []
    return result
        



def test_count_find_num(count_find_num):
    primesL = [2, 3]
    limit = 200
    assert count_find_num(primesL, limit) == [13, 192]

    primesL = [2, 5]
    limit = 200
    assert count_find_num(primesL, limit) == [8, 200]

    primesL = [2, 3, 5]
    limit = 500
    assert count_find_num(primesL, limit) == [12, 480]

    primesL = [2, 3, 5]
    limit = 1000
    assert count_find_num(primesL, limit) == [19, 960]

    primesL = [2, 3, 47]
    limit = 200
    assert count_find_num(primesL, limit) == []