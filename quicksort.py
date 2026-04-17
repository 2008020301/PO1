from random import randint

numbers = [randint(1800, 2200) for _ in range(10)]
print(numbers)

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

sorted_numbers = quick_sort(numbers)
print(sorted_numbers)