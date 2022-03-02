from random import randint
from timeit import default_timer as timer

# c = [] #final output array

def create_array(size=10, max=50):
    return[randint(0, max) for x in range(size)]

print(create_array())

def merge(a,b):
    c = [] #final output array
    a_idx, b_idx = 0,0
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1
        if a_idx == len(a): 
            c.extend(b[b_idx:])
            c.extend(a[a_idx:])
        else:               
            return c
a = [1,3,5]
b = [2,4,6]
merge(a,b)
print(a,b)


def merge_sort(a):
    # a list of zero or one elemnts is sorted
    if len(a) <= 1: return a
    # split the list in half and call merge sort recursively on each half
    # left,right = merge_sort(a[:len(a)/2]), merge_sort(a[len(a)/2:])
    midpoint = int(len(a)/2)
    left,right = merge_sort(a[:midpoint]), merge_sort(a[midpoint:])
    # merge the now-sorted sublists
    return merge(left,right)

a = create_array()
print(a)
s = merge_sort(a)
print(s)