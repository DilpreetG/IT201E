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

def construct_set_zm():
    # TODO: Implement the logic for constructing Set Zm
    print("Constructing Set Zm")

def compute_gcd():
    # TODO: Implement the logic for computing GCD of two integers
    print("Computing GCD")

def test_primality():
    # TODO: Implement the logic for testing primality
    print("Testing primality")

def euclidean_algorithm():
    # TODO: Implement the logic for Euclidean algorithm
    print("Euclidean algorithm")

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
