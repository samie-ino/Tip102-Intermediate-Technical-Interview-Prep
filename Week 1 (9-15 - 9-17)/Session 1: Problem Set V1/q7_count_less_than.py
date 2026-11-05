# Problem 7: Poohsticks
# Winnie the Pooh and his friends are playing a game called Poohsticks where they drop sticks in a stream and race them.
# They time how long it takes each player's stick to float under Poohsticks Bridge to score each round.
#
# Write a function count_less_than() to help Pooh and his friends determine how many players should move on to the next round of Poohsticks.
# count_less_than() should accept a list of integers race_times and an integer threshold and return the number of race times less than threshold.
#
# def count_less_than(race_times, threshold):
#     pass
#
# Example Usage:
#
# race_times = [1, 2, 3, 4, 5, 6]
# threshold = 4
# print(count_less_than(race_times, threshold))
#
# race_times = []
# threshold = 4
# print(count_less_than(race_times, threshold))
#
# Example Output:
#
# 3
# 0

'''
Understand:
- Input: Accept a list of integers race_times
- Output: Return an integer lessthan the threshold value

Plan:
1. create an empty list to accpet integers
2. if its less than the threshold return the racetime number
3. if the list is empty return 0

'''

def count_less_than(race_times, threshold):
    race_times = []
    for num in race_times:
        if num < threshold:
            return num 
        else:
            return 0

race_times = [1, 2, 3, 4, 5, 6]
print(count_less_than(race_times, 4))

race_times = []
print(count_less_than(race_times, 4))
