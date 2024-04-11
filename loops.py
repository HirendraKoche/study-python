# Write a loop that makes seven calls to print(), so we get on the output the following triangle:

    #
    ##
    ###
    ####
    #####
    ######
    #######

for i in range(1,8):
    print('#'*i)

# Use nested loops to create the following:

    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #

# for i in range(1, 9):
#     for j in range(1, 9):
#         print("#", end=" ")
#     print("")

for x in range(1, 9):
    print("# "*8)

# Print the following pattern:

    # 0 x 0 = 0
    # 1 x 1 = 1
    # 2 x 2 = 4
    # 3 x 3 = 9
    # 4 x 4 = 16
    # 5 x 5 = 25
    # 6 x 6 = 36
    # 7 x 7 = 49
    # 8 x 8 = 64
    # 9 x 9 = 81
    # 10 x 10 = 100

for x in range(11):
    print(f"{x} x {x} = {x * x}")

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

lang_lt = ['Python', 'Numpy','Pandas','Django', 'Flask']

# count = 0
# while count < len(lang_lt):
#     print(lang_lt[count])
#     count += 1

for lang in lang_lt:
    print(lang)

# Use for loop to iterate from 0 to 100 and print only even numbers

# count = 0
# while count <= 100:
#     if count % 2 == 0:
#         print(count, end=" ")
#     count += 1

for x in range(0, 101, 2):
    print(x, end=" ")

# Use for loop to iterate from 0 to 100 and print only odd numbers
print()

for x in range(0, 101):
    if x % 2 !=0:
        print(x, end=" ")

# Use for loop to iterate from 0 to 100 and print the sum of all numbers
print()
result = 0
for x in range(0, 101):
    result += x
print(result)   

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even_sum = 0
odd_sum = 0
for x in range(0, 101):
    if x % 2 == 0:
        even_sum += x
    else:
        odd_sum += x
print(f"Even sum = {even_sum}\nOdd sum = {odd_sum}")

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits_lt = ['banana', 'orange', 'mango', 'lemon']
fruits_rev_lt = []
for fruit in fruits_lt:
    fruits_rev_lt.insert(0, fruit)
print(fruits_rev_lt)
