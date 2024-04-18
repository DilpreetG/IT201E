'''
https://github.com/shmilylty/miller-rabin-primality-test/blob/master/miller_rabin_primality_test.py

OpenAI. (2022). Assistance with Miller-Rabin Primality Test Implementation. GitHub Copilot. https://copilot.github.com
'''

# import numPy
# import sympy
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

def construct_set_zm():
    """
    Constructs the set Zm, where m is a user-provided modulus, and calculates the additive and multiplicative inverses for each element in Zm.

    Parameters:
    None, but prompts user to input an integer for the modulus.

    Returns:
    str: A string representation of the set Zm, along with the additive and multiplicative inverses for each element in Zm. If the input is not a positive integer, returns an error message.
    """
    m = int(input("Enter an integer for modulus: "))
    if m < 0:
        return "Input must be positive."
    set_zm = []
    additive_inverses = []
    multiplicative_inverses = []
    for i in range(m):
        set_zm.append(i)

    # Calculate the additive and multiplicative inverses for each element in Zm
    for a in set_zm:
        # Additive inverse
        additive_inverse = (-a) % m
        additive_inverses.append(additive_inverse)

        # Multiplicative inverse
        multiplicative_inverse = None
        for b in set_zm:
            if (a * b) % m == 1:
                multiplicative_inverse = b
                break
        multiplicative_inverses.append(multiplicative_inverse)

    return f"Z{m} = {set_zm} \n Additive inverses: {additive_inverses} \n Multiplicative Inverses: {multiplicative_inverses}"

def compute_gcd():
    """
    Computes the greatest common divisor (GCD) of two user-provided integers using the math.gcd function.

    Parameters:
    None, but prompts user to input two integers.

    Returns:
    str: A string representation of the GCD of the two input integers. If the inputs are not integers, returns an error message. If both inputs are zero, returns a message stating that the GCD of zeros is undefined.
    """
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except:
        return "Inputs must be integers"
    #
    if a == 0 and b == 0:
        return "GCD of zeros is undefined"
    gcdResult = math.gcd(a, b)
    return f"GCD = {gcdResult}"

def test_primality():
    """
    Tests the primality of a user-provided integer using trial division.

    Parameters:
    None, but prompts user to input an integer.

    Returns:
    str: A string representation of the result of the primality test. If the input is not an integer, returns an error message. If the input is 1 or 2, returns a message stating that 1 is composite and 2 is the only even prime number, respectively. If the input is less than 0, returns a message stating that the input must be a positive integer.
    """
    n = int(input("Enter a number for primality test: "))
    if n == 2:
        return "2 is the only even prime number, no test needed."
    elif n == 1:
        return "1 is composite, no test needed."
    elif n < 0:
        return "Input must be a positive integer"
    # Trial division
    time1 = time.perf_counter_ns()
    if n <= 1:
        result = False
    elif n <= 3:
        result = True
    elif n % 2 == 0 or n % 3 == 0:
        result = False
    else:
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                result = False
                break
            i += 6
        else:
            result = True
    time2 = time.perf_counter_ns()
    time_total_1 = time2 - time1
    message1 = (f"Test primality by Trial Division: Primality = {result} and time = {time_total_1}")
    # Fermat's test
    time1 = time.perf_counter_ns()
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
    time2 = time.perf_counter_ns()
    time_total_2 = time2 - time1
    message2 = (f"Test primality by Fermat's Test: Primality = {result} and time = {time_total_2}")

    # Miller-Rabin Test
    time1 = time.perf_counter_ns()
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

    time2 = time.perf_counter_ns()
    time_total_3 = time2 - time1
    message3 = (f"Test primality by Miller-Rabin Test: Primality = {result} and time = {time_total_3}")
    return message1, message2, message3

def euclidean_algorithm():
    """
    Computes the greatest common divisor (GCD) of two user-provided integers using the Euclidean algorithm.

    Parameters:
    None, but prompts user to input two integers.

    Returns:
    str: A string representation of the GCD of the two input integers. If the inputs are not integers, returns an error message. If both inputs are even, returns a message stating that the inputs are not coprime.
    """
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except:
        return "Inputs must be integers."
    if a % 2 == 0 and b % 2 == 0:
        return "Error: a and b are not coprime"
    while b != 0:
        a, b = b, a % b
    return_statement = "GCD is: "
    return return_statement + str(a)

# Main program
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print(construct_set_zm())
    elif choice == "2":
        print(compute_gcd())
    elif choice == "3":
        print(test_primality())
    elif choice == "4":
        print(euclidean_algorithm())
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
