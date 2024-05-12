def mymap(func,*iterables):
    iterators = [iter(iterable) for iterable in iterables]
    while True:
        try:
            curtup = [next(iterator) for iterator in iterators]
            yield func(curtup)
        except StopIteration:
            return

def myzip(*iterables, strict = False):
    iterators = [next(iterator) for iterator in iterables]
    while True:
        try:
            curtup = (next(iterator) for iterator in iterators)
            yield curtup
        except StopIteration:
            return

def myenumerate(iterable,start=0):
    for item in iterable:
        yield start,item
        start += 1

def myfilter(func,iterable):
    if func is None:
        filteredls = [i for i in iterable if bool(i)]
    else:
        filteredls = [i for i in iterable if func(i)]
    for item in filteredls:
        yield item

def myreduce(func,iterable,initial = None):
    iterator = iter(iterable)
    if initial is None:
        try:
            initial = next(iterator)
        except TypeError:
            raise"reduce cant acept argument without initial value"
    result = initial
    for item in iterator:
        result = func(result,item)
    return result


def mymap(func,*iterables):
    iterators = [iter(iterable) for iterable in iterables]
    curtup = [next(iterator) for iterator in iterators]
    yield func(curtup)


def myzip(*iterables):
    iterators = [next(iterator) for iterator in iterables]
    curtup = (next(iterator) for iterator in iterators)
    yield curtup


def myzipmap(function,*iterables):
    iterators = [next(iterator) for iterator in iterables]
    while True:
        try:
            curtup = (next(iterator) for iterator in iterators)
            yield function(curtup)
        except StopIteration:
            return

def outer(foo):
    def inner(*args,**kwargs):
        print(f"calling{foo.name}")
        print(f"with args: {args},and kwargs: {kwargs}")
        res = foo(*args,**kwargs)
        print(f"with the result of: {res}")
        return res
    return inner

def pipeline(*funcs):
    def wrapper(inputs):
        res = inputs
        for func in funcs:
            res = func(res)
        return res
    return wrapper

def adder(x):
    return x+4
def squarer(x):
    return x ** 2
def div(x):
    return x/2
x = pipeline(adder,squarer,div)
print(x(1))