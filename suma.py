
def suma(text):
    numbers = _split(text)
    res = 0
    while numbers:
        a = numbers.pop[0]
        res += a
    res = _suma(numbers)
    return res


def _split(text):
    res = []
    elements = text.split()
    for element in elements:
        if element.isdigit():
            res.append(float(element))
    return res
