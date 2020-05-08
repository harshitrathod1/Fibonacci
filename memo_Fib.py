def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func
@memoize
def fibr(n):
    if n==0 or n==1:
        return n
    else:
        return fibr(n-1)+fibr(n-2)
