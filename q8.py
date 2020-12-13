# Write a function, is_prime, that takes an integer and returns True if the number is prime and False if the number is not prime.

def is_prime(num):
    for i in range(2, num//2):
        if num % i == 0:
            return True
        else:
            return False

n = int(input('Enter number to check prime: '))
result = is_prime(n)
print(result)
