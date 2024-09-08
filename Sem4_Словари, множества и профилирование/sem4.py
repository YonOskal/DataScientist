import random as rnd
# from random import randint



def create_rnd_list(size):
    lst = []
    for _ in range(size):
        lst.append(rnd.randint(1,100))
    return lst

def plus_two_values(v1: int, v2: int) -> int:
    '''
    this function add two integer values
    '''
    # if isinstance(v1, int) and isinstance(v2, int):
    #     return v1 + v2
    # else:
    #     print("Error!")
    if not (isinstance(v1, int) and isinstance(v2, int)):
    raise TypeError("Must be int values")
    return v1 + v2



# print(create_rnd_list(8))
# print(plus_two_values.__doc__)
# print(plus_two_values(5,8))
# help(print)
print(plus_two_values("hello "," world"))

# lst = []
# for _ in range(10):
# lst.append(rnd.randint(1,100))
# print(lst)