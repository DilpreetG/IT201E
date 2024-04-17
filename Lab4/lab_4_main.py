'''
https://github.com/shmilylty/miller-rabin-primality-test/blob/master/miller_rabin_primality_test.py

OpenAI. (2022). Assistance with Miller-Rabin Primality Test Implementation. GitHub Copilot. https://copilot.github.com
'''

import numpy
import sympy
import math
import random
import time

def display_menu():
    print("Number Theory Operations Menu:")
    print("1. Construct Set Zm")
    print("2. Compute GCD of two integers")
    print("3. Test for primality")
    print("4. Euclidean algorithm")
    print("5. Exit")

def construct_set_zm(m):
    set_zm = []
    for i in range(m):
        set_zm.append(i)

    print(f"Set Zm: {set_zm}")

    # Calculate and display the additive and multiplicative inverses for each element in Zm
    for a in set_zm:
        # Additive inverse
        additive_inverse = (-a) % m
        print(f"Additive inverse of {a} in Zm: {additive_inverse}")

        # Multiplicative inverse
        multiplicative_inverse = None
        for b in set_zm:
            if (a * b) % m == 1:
                multiplicative_inverse = b
                break
        if multiplicative_inverse is not None:
            print(f"Multiplicative inverse of {a} in Zm: {multiplicative_inverse}")
        else:
            print(f"{a} has no multiplicative inverse in Zm")

def compute_gcd(a, b):
    #
    if a.type() == str or b.type() == str:
        return "Inputs must be integers."
    elif a == 0 or b == 0:
        return "GCD of zeros is undefined"
    gcd = gcd(a, b)
    return gcd

def test_primality(n):
    if n == 2:
        return "2 is the only even prime number, no test needed."
    elif n == 1:
        return "1 is composite, no test needed."
    elif n < 0:
        return "Input must be a positive integer"
    # Trial division
    time1 = time.clock()
    if n <= 1:
        result = False
    elif n <= 3:
        result = True
    elif n % 2 == 0 or n % 3 == 0:
        result = False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            result = False
        i += 6
    result = True
    time2 = time.clock
    time_total_1 = time2 - time1
    message1 = (f"Test primality by Trial Division. Primality = {result} and time = {time_total_1}\n")

    # Fermat's test
    time1 = time.clock()
    k = 5  # number of testing rounds
    if n <= 1 or n == 4:
        result = False
    elif n <= 3:
        result = True
    else:
        while k > 0:
            # Pick a random number in [2..n-2]
            a = random.randint(2, n - 2)

            # Fermat's little theorem
            if pow(a, n - 1, n) != 1:
                result = False
                break

            k -= 1
        else:
            result = True
    time2 = time.clock()
    time_total_2 = time2 - time1
    message2 = (f"Test primality by Fermat's Test. Primality = {result} and time = {time_total_2}\n")

    # Miller-Rabin Test
    time1 = time.clock()
    k = 5  # number of testing rounds
    if n <= 1:
        result = False
    elif n <= 3:
        result = True
    else:
        d = n - 1
        while d % 2 == 0:
            d //= 2

        for item in range(k):
            a = random.randint(2, n - 2)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            while d != n - 1:
                x = pow(x, 2, n)
                d *= 2
                if x == n - 1:
                    break
            else:
                result = False
                break
        else:
            result = True

    time2 = time.clock()
    time_total_3 = time2 - time1
    message3 = (f"Test primality by Miller-Rabin Test. Primality = {result} and time = {time_total_3}\n")
    return message1, message2, message3

def euclidean_algorithm(a, b):
    if a != int or b != int:
        return "Inputs must be integers."
    while b != 0:
        a, b = b, a % b
    return_statement = "GCD is: "
    return return_statement + str(a)

# Main program
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        construct_set_zm()
    elif choice == "2":
        compute_gcd()
    elif choice == "3":
        test_primality()
    elif choice == "4":
        euclidean_algorithm()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
