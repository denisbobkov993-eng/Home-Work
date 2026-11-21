def is_polindrome(num):
    if num == num[::-1]:
        return True
    else:
        return False
while True:
    try:
        n=input()
    except EOFError:
        break
    num = list(map(int, n.split()))
    print(is_polindrome(num))