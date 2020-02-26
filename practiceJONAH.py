# Partner 1: Jonah Song
# Partner 2: Isabelle Torch
##############################
# Assignment Name: GitHub Practice (2/25/20) - 20 Points
##############################
import random

def getNRandom(n):
    '''takes in an integer and returns a list of n random integers between 1 and 10, inclusive'''
    n = int(input("Input an integer. "))   
    numbers = []
    for i in range(n):
        numbers.append(random.randint(1,10))
    return numbers

def multiplyRandom(numbers):
    '''takes in a list of n numbers and returns the product of the numbers'''
    pass

def main():
	print(multiplyRandom(getNRandom(10))

if __name__ == "__main__":
	main()
