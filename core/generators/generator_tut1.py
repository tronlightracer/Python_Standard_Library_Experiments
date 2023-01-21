#! /usr/bin/python3

case1 = ["", "h", "he", "hel", "hell", "world"]
case2 = ("", "h", "he", "hel", "hell", "world")

# generators are functions that act like for loops
# they return a generator object which holds the values in the iterable
# to get the values out of the object do list(generator_func_name)
# or tuple(generator_func_name)

def generate(ls):
    for i in ls:
        yield i

print(list(generate(case1)))
print(tuple(generate(case2)))

# trying to see if it'll convert to similar data structures
print(list(generate(case2))) # it does
print(set(generate(case1))) # even with unordered iterables