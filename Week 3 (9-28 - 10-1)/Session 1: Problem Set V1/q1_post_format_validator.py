# Problem 1: Post Format Validator
# ------------------------------------------------------------------------------
# You are managing a social media platform and need to ensure that posts are
# properly formatted. Each post must have balanced and correctly nested tags,
# such as () for mentions, [] for hashtags, and {} for links. You are given a
# string representing a post's content, and your task is to determine if the
# tags in the post are correctly formatted.
#
# A post is considered valid if:
# 1. Every opening tag has a corresponding closing tag of the same type.
# 2. Tags are closed in the correct order.
#
# Example Usage:
# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}"))
# print(is_valid_post_format("(]"))
#
# Example Output:
# True
# True
# False
# ------------------------------------------------------------------------------

'''
Understand -
Input:
Output:
Edge Cases:

Plan - 


Implement -
(look below)


'''
def is_valid_post_format(posts):
    pass


if __name__ == "__main__":
    print(is_valid_post_format("()"))
    print(is_valid_post_format("()[]{}"))
    print(is_valid_post_format("(]"))