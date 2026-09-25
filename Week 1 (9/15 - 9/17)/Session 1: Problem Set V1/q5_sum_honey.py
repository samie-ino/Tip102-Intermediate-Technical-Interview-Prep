# Problem 5: Total Honey
# Winnie the Pooh wants to know how much honey he has. Write a function sum_honey() that accepts
# a list of integers hunny_jars and returns the sum of all elements in the list. Do not use the built-in function sum().
#
# def sum_honey(hunny_jars):
#     pass
#
# Example Usage:
#
# hunny_jars = [12, 7, 31, 5]
# print(sum_honey(hunny_jars))
#
# Example Output:
#
# 55

def sum_honey(hunny_jars):
    honey_sum = 0
    for i in hunny_jars:
        honey_sum += i
    return honey_sum

