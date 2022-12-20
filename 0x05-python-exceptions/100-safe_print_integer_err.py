#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().
    if a ValueError message is caught, a corresponding message is printed to standard error.
     Args:
     value (int): the integer to print.
     Return:
     if a TypeError or ValueError occurs - false.
     otherwise - True.
     """
     try:
         print("{:d}".format(value))
         return (True)
     except (TypeError, ValueError):
         print("Exception: {}".format(sys.esc_info()[i]), file=sys.stderr)
         return (False)

