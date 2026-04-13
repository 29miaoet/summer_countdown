def is_prime(num):
    lastcheck = int(num**0.5)
    for i in range (2,lastcheck+1):
        if num % i == 0:
            return False
            break
    else:
        return True

for i in range(1, 100):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
