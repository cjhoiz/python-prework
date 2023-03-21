# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

# def hello_name(user_name):
#     print("Hello_" + user_name.upper() + "!")

# hello_name('chris')


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

# def first_odds():
#     for num in range(100):
#         if num % 2 != 0:
#             print(num)

# first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.

# def max_num_in_list(a_list):
#     max = a_list[0]
#     for num in a_list:
#         if num >  max:
#             max = num
#     return max

# a_list = [5, 6, 7, 10, 1, 2, 3]
# print(max_num_in_list([5, 6, 7, 10, 1, 2, 3]))
# print("The largest number in the list is:", max_num_in_list(a_list))

# Two ways to print out the information depending on how you want it presented.

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

# def is_leap_year(a_year):
#     if a_year % 100 == 0 and a_year % 400 == 0:
#         print(str(a_year) + " is a century leap year!")
#     elif a_year % 4 == 0 and a_year % 100 != 0:
#         print(str(a_year) + " is a leap year!")
#     else:
#         print(str(a_year) + " is not a leap year!")

# is_leap_year(2000)
# is_leap_year(1987)
# is_leap_year(2004)
# is_leap_year(1900)



# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    sorted_a_list = sorted(a_list)
    test_a_list = list(range(min(a_list), max(a_list) + 1))
    if sorted_a_list == test_a_list:
        return True
    else:
        return False

consecutive_test = is_consecutive([1,2,4,5,3])
non_consecutive_test = is_consecutive([1,2,4,5,7])
print(consecutive_test)
print(non_consecutive_test)