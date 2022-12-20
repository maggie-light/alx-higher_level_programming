#!/usr/bin/python3

def safe_print_integer(value):
   """print an integer with "{:d}".format().
   Args:
   value (int): the integer to print.
   Returns:
   If a TypeError or ValueError occurs - False.
   Otherwise - True.
   """
    try:
        print("{:d}".format(value))
        print("\n")
        return (true)
    except (TypeError, ValueError):
        return (false)





