import random

def random_interval(start, end):
    if start > end:
        temp = start
        start = end
        end = temp
        
    return int(random.random() * (end - start + 1) + start)


print(random_interval(1, 6))
print(random_interval(1, 6))
print(random_interval(6, 1))
print(random_interval(6, 1))