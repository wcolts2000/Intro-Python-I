# Write a program to determine if a number, given on the command line, is prime.


import math


def isPrime(num):
    for i in range(2, num//2):
        if (num % i == 0):
            print('not prime')
            return
    print('prime')


# isPrime(2)
# isPrime(20)
# isPrime(7)
# isPrime(42)
# isPrime(17)
# isPrime(23)


# Implement The Sieve of Erathosthenes ===================
'''
1. Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
2. Initially, let p equal 2, the smallest prime number.
3. Enumerate the multiples of p by counting in increments of p from 2p to n, and mark them in the list (these will be 2p, 3p, 4p, ...; the p itself should not be marked).
4. Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
5. When the algorithm terminates, the numbers remaining not marked in the list are all the primes below n.
'''

# https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/


def SieveOfEratosthenes(n):

    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            print(p),


SieveOfEratosthenes(30)
