from random import randint

numbers = [randint(0,100) for _ in range(10)]
print(numbers)

def bubble_sort():
    while True:
        order = 0
        for i in range(len(numbers)):
            if i+1 == len(numbers):
                if order == 0:
                    return numbers
                break
            n_l = numbers[i]
            n_r = numbers[i+1]
            
            if n_l > n_r:
                numbers[i], numbers[i+1] = n_r, n_l
                order += 1

print(bubble_sort())