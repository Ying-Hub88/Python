#!/usr/bin/env python3.10

# given an array A of N integers, returns true if A contains at least two elemets which differ by 1, 
# and flase otherwise. Examples:
# 1. Given A = [7], the function should return false.
# 2. Given A = [4, 3], the function should return true.
# 3. Given A = [11, 1, 8, 12, 14], the function should return true. 
#     Pair of elements which differ by 1 is (11, 12)
# 4. Given A = [4, 10, 8, 5, 9], the function should return true.
#     Pairs of elements which differ by 1 are (4, 5), (10, 9), and (8, 9)
# 5. Given A = [5, 5, 5, 5, 5], the function should return false.
#     There are no two elements in A whose values differ by 1.
# Write an efficient algorithm for the following assumptions:
#     N is an interger within the range [1..100,000]
#     Each element of array A is an interger within the range [1..1,000,000,000]


a = []
entering = True
n_range = 0

while entering:
    user_input = input("Please enter an integer (Enter Q to stop): ")
    if user_input.isdigit() and int(user_input) > 1 and int(user_input) < 1000000000 and n_range < 100000:
        a.append(int(user_input))
        n_range += 1
    elif user_input.lower() == 'q':
        entering = False

print(f"The number(s) you entered: {a}")

a.sort()
pair = []
i, j = 0, 1

while i < len(a):
    while j < len(a):
        if a[i] - a[j] == -1:
            pair.append(f"({a[i]}, {a[j]})")
        j += 1
    i += 1
    j = i + 1

if len(pair) > 1:
    print(f"Pair(s) of elements which differ by 1: {pair}")
else:
    print("There are no two numbers you entered whose values differ by 1.")
