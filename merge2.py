from random import randint
from timeit import default_timer as timer

    # Random listan luonti
def create_array(size=10, max=50):
    return[randint(0, max) for x in range(size)]


def merge_sort(array):
    # listan palautus mikäli se on pienempi tai yhtäsuuri kuin 1
    if len(array) <= 1:
        return array
    # listan keskipiste ja listan jako osiin 
    midpoint = int(len(array) / 2)
    # merge_sortin kutsu molempiin puoliskoihin
    left, right = merge_sort(array[:midpoint]), merge_sort(array[midpoint:])
    return merge(left, right)

def merge(left, right):
    
    result = []  # Järjestetty lista
    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):

        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])
    return result

def main():
    array = create_array()
    print()
    print("Alkuperäinen lista:", array)
    start = timer()
    result = merge_sort(array)
    stop = timer()
    print("Merge sorted:", result)
    print()
    print("Listan järjestämiseen kului aikaa", stop - start, "sekuntia.")
    print()
if __name__ == "__main__":
    main()