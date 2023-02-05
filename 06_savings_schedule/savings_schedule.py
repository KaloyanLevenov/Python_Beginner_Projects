import random


def input_validation():
    while True:
        try:
            money = int(input("ENTER how much MONEY do you want to save: "))
            break
        except ValueError:
            print("Please enter an integer number !")

    while True:
        try:
            days = int(input("ENTER for how many DAYS you want to save the money: "))
            break
        except ValueError:
            print("Please enter an integer number !")

    while True:
        try:
            biggest_bill = int(input("ENTER the biggest amount you can save for a day: "))
            break
        except ValueError:
            print("Please enter an integer number !")

    return money, days, biggest_bill


def schedule(days):
    matrix = []
    while days > 0:
        row = []
        while len(row) < 7:
            row.append(0)
            days -= 1
            if days == 0:
                break
        matrix.append(row)
    return matrix


money, period_of_time, payment = input_validation()
print(schedule(period_of_time))

#Given two integers M and N, the task is to create a list of M non-negative integers whose sum is N. In case when more
#than one list is possible, find any one.
#Examples:
 #Input: M = 4, N = 8
#Output: 1 3 3 1
#1 + 3 + 3 + 1 = 8
#Input: M = 5, N = 3
#Output: 0 1 1 0 1


# Utility function to print the
# elements of an array
def printArr(arr, n):
    for i in range(n):
        print(arr[i], end=" ")


# Function to generate a list of
# m random non-negative integers
# whose sum is n
def randomList(m, n):
    # Create an array of size m where
    # every element is initialized to 0
    arr = [0] * m

    # To make the sum of the final list as n
    for i in range(n):
        # Increment any random element
        # from the array by 1
        arr[randint(0, n) % m] += 1;

    # Print the generated list
    printArr(arr, m);


# Driver code
if __name__ == "__main__":
    m = 4;
    n = 8;

    randomList(m, n);

# This code is contributed by AnkitRai01

