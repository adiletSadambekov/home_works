
def domain_name(url: str):
    domain: str = ''
    if url[4] == 's':
        if url[8] == 'w':
            for i in url[12:]:
                if i == '.':
                    return domain
                else:
                    domain += i
        else:
            for i in url[8:]:
                if i == '.':
                    return domain
                else:
                    domain += i
    if url[7] == 'w':
        for i in url[11:]:
            if i == '.':
                return domain
            else:
                domain += i
    if url[0:3] == 'www':
        for i in url[4:]:
            if i == '.':
                return domain
            else:
                domain += i
    else:
        for i in url[7:]:
            if i == '.':
                return domain
            else:
                domain += i
    return domain


def test_domain_name(domain_name):
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"

