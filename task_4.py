def bananas(s: str) -> set:
    result = set()
    first_count: int = 0
    last_count: int = 0
    first_len: str = ''
    last_len: str = ''
    banana: str = ''
    banan: str = ''
    trigger: bool = True
    trigger3: bool = False
    trigger2: bool = False
    two_step: int = 0
    two_step2: int = 0
    two_step3: int = 0
    
    for i in s:
        if len(banana) == 7:
            banana = banana[1:]
            first_len += banana[0]
        if banana == 'banana':
            last_len = s[len(first_len)+6:]
            result.add(len((first_len)) * '-' + banana + len(last_len) * '-')
            last_count = len(last_len)
            first_count = len(first_len)
            banan = s[first_count:]
        else:
            banana += i


    if banana == 'banana':
        if len(s) > 6:
            trigger2 = True
            trigger3 = True
            if banan[0] in first_len:
                if first_count == 1 and first_len == 'b':
                    result.add(first_len + (first_count * '-') + banana[first_count:] + (last_count * '-'))
        else:
            result.add(banana)
    

    while trigger:
        two_step += 1
        check_banana_last = banan[0:-(last_count + two_step)] + banan[-two_step:]
        if check_banana_last == 'banana':
            result.add(first_count * '-' + banan[0:-(last_count + two_step)] +\
                 (last_count * '-' ) + banana[-two_step:])
        else:
            trigger = False
    

    while trigger2:
        two_step2 += 1
        check_banana_first = banan[0:-(last_count + two_step2)] + banan[-two_step2:]
        if check_banana_first == 'banana':
            result.add(first_len + (first_count * '-') +\
                 banan[first_count:-(last_count + two_step2)] +\
                      (last_count * '-') + banan[-two_step2:])
        else:
            trigger2 = False

    while trigger3:
        two_step3 += 1
        check_trough = banan[0:5] + banan[-two_step3]
        if check_trough == 'banana':
            add_check = banan[0:5] + banan[-two_step]
            if add_check == 'banana':
                result.add(banan[0:5] + len(banan[5:-2]) * '-' +\
                 banan[-two_step] + '-')
        else:
            trigger3 = False

    return result


def test_bananas(bananas):
    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}


        
        
 