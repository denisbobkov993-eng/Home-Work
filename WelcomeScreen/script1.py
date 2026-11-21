from itertools import count


def count_of_local_minimum(numbers):
    result = 0
    for i in range(1, len(numbers)-1):
        if numbers[i]<numbers[i-1] and numbers[i]<numbers[i+1]:
            result += 1
    return result
while True:
    try:
        n=input()
    except EOFError:
        break
    numbers = list(map(int, n.split()))
    print(count_of_local_minimum(numbers))



