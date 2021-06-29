from functools import reduce

source = [1,2,3,4,5]

# 1*2,3,4,5
# 2*3,4,5


def mult(x, y):
    return x * y

def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def concatenate(x, y):
    return str(x) + str(y)



def custom_reduce(func, source):
    result = source[0]
    if len(source) < 2:
        result = source[0]
    for i in range(1, len(source)):
        result = func(result, source[i])
    return result


def recursion_reduce(func, source, default=None):
    if default is None:
        default = source[0]
        source = source[1:]
    if len(source) == 0:
        return default
    return recursion_reduce(func, source[1:], func(default, source[0]))


functions = [
    mult, 
    plus,
    minus,
    concatenate
]

str_func = [
    'mult', 
    'plus',
    'minus',
    'concatenate'
]


for i in range(len(functions)):
    print("func: {0} in custom_reduce: {1}".format(str_func[i], custom_reduce(functions[i],source)))
    print("func: {0} in recursion_reduce: {1}".format(str_func[i], recursion_reduce(functions[i],source)))
    print("func: {0} in reduce: {1}".format(str_func[i], reduce(functions[i],source)))
    print('-' * 20)

"""
Пример вывода
source = [1, 2]

func: mult in custom_reduce: 2
func: mult in recursion_reduce: 2
func: mult in reduce: 2
--------------------
func: plus in custom_reduce: 3
func: plus in recursion_reduce: 3
func: plus in reduce: 3
--------------------
func: minus in custom_reduce: -1
func: minus in recursion_reduce: -1
func: minus in reduce: -1
--------------------
func: concatenate in custom_reduce: 12
func: concatenate in recursion_reduce: 12
func: concatenate in reduce: 12
--------------------


source = [1, 2, 3, 4, 5]

func: mult in custom_reduce: 120
func: mult in recursion_reduce: 120
func: mult in reduce: 120
--------------------
func: plus in custom_reduce: 15
func: plus in recursion_reduce: 15
func: plus in reduce: 15
--------------------
func: minus in custom_reduce: -13
func: minus in recursion_reduce: -13
func: minus in reduce: -13
--------------------
func: concatenate in custom_reduce: 12345
func: concatenate in recursion_reduce: 12345
func: concatenate in reduce: 12345
--------------------
"""
