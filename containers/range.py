

def range(a, b=None, c=None):
    if b is None and c is None:
        result = 0
        while result < a:
            yield result
            result += 1
    elif c is None:
        result = a
        while result < b:
            yield result
            result += 1
    else:
        result = a
        if c > 0:
            while result < b:
                yield result
                result += c
        else:
            while result > b:
                yield result
                result += c
