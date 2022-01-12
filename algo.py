"""Trying to learn a bit about algorithms"""
import time
import sys
from ipaddress import ip_address
from rich import print
from timer import Timer


DELAY = 0.0001


def bin_search(some_array: list, target: int):
    """Simple binary search function"""
    array = sorted(some_array)
    start = 0
    end = len(array) - 1
    found = False
    while not found and start <= end:
        time.sleep(DELAY)
        middle = int((start + end) / 2)
        if int(array[middle]) == target:
            found = True
            print(f"Found: {ip_address(target)} with binary search")
        elif int(array[middle]) > target:
            end = middle - 1
        else:
            start = middle + 1


def main():
    """Used to run all the things"""

    if len(sys.argv) != 2:
        print("Missing filename parameter, ex python algo.py ordered_ip.txt")
        sys.exit(1)

    # Creating a list of integer values from subnet addresses
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        data = [int(ip_address(line.strip())) for line in file.readlines()]

    # This looks fancy but we are jut asking the user for a subnet and then
    # converting to the integer equivelant.
    my_target = int(
        (ip_address(input("What /24 prefix in 10.0.0.0/8 are you looking for? ")))
    )

    # Testing linear search
    t1 = Timer()
    t1.start()
    for prefix in data:
        time.sleep(DELAY)
        if prefix == my_target:
            print(f"Found: {ip_address(my_target)} with linear search")
            break
    t1.stop()

    # Testing Binary Search
    t2 = Timer()
    t2.start()
    bin_search(data, my_target)
    t2.stop()


if __name__ == "__main__":
    main()
