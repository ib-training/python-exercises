"""
Some exercises on python numbers and strings
"""
import math    # basic math functions, see https://docs.python.org/3.7/library/math.html
import random  # module for random numbers, see https://docs.python.org/3.7/library/random.html


def mean(a, b):
    """
    returns the mean of two numbers
    """
    raise NotImplementedError

def concat_digits(a, b):
    """
    returns a number, where the digits of a and b are concatenated

    Example: a = 123 (number)   b =  456 (number)
    Result:  123456 (as a number)
    """
    raise NotImplementedError

def count_digits(n):
    """
    return the number of digits of the number n
    """
    raise NotImplementedError

def calc_three_times_n_plus_one(n):
    """
    calculates 3 times n plus one
    """
    raise NotImplementedError

def my_round(x):
    """
    rounds the number x

    round already exists - but as an exercise,
    implement my_round without using round 

    Also: Try to implement it without 'if'
    """
    raise NotImplementedError

def is_divisible(n, r):
    """
    return True if n is divisible by r 
    return False otherwise
    """
    raise NotImplementedError

def radians(degrees):
    """
    Convert degrees to radians ("Grad in Bodenmaß")
    """
    raise NotImplementedError

def close_enough(a, b, epsilon):
    """
    checks if the distance between the 
    float numbers a and b is smaller than epsilon
    """
    raise NotImplementedError

def hypotenuse(a,b):
    """
    calculates c, with a^2 + b^2 = c^2
    """
    raise NotImplementedError

def binary(n):
    """
    returns the binary representation of n

    binary(3) returns "11"
    binary(16) returns "10000"
    binary(15) returns "1111"

    Hint: use bin function, but remove the first 2 letters from the result
    """
    raise NotImplementedError
    
def line(length=10):
    """
    returns a line composed of dash characters:

    line() returns '----------'
    line(3) returns '---'
    line(20) returns '--------------------'
    """
    raise NotImplementedError

def dice():
    """
    throw a dice (return a random number from 1 to 6)

    hint: look at the module random in the python API
    """
    raise NotImplementedError
