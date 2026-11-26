def delite_even_digits(digits:list[int]) -> int:
    c=[]
    for i in digits:
        if i%2!=0:
            c.append(i)
    return c
while True:
    n=input()
    if n=="":
        break
    digits = list(map(int, n.split()))
    print(delite_even_digits(digits))



