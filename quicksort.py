from random import randint

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    
    pivot = numbers[randint(0, len(numbers)-1)]

    left = []
    middle = []
    right = []

    for n in numbers:
        if n < pivot:
            left.append(n)
        elif n > pivot:
            right.append(n)
        else:
            middle.append(n)

    return quick_sort(left) + middle + quick_sort(right)
