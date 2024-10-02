def prime_checker(number):
    list = []
    for i in range(1, n+1):
        if n % i == 0:
            list.append(i)
    count = len(list)
    if count > 2:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")   
n = int(input()) # Check this number
prime_checker(number=n)
