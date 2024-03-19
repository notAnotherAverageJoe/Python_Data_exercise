def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    factors = []  # Initialize an empty list to store factors
    for i in range(1, int(num ** 0.5) + 1):  # Iterate up to the square root of num
        if num % i == 0:
            factors.append(i)
            if i != num // i:  # Avoid duplicate factors if num is a perfect square
                factors.append(num // i)
    factors.sort()  # Sort the factors in increasing order
    return factors