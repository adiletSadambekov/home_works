import re

def domain_name(url: str):
    if 'http' in url:
        domain = re.split(r"[//.]", url)
        return domain[2]
    else:
        domain = re.split(r"[//.]", url)
        return domain[1]


def test_domain_name(domain_name):
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"

