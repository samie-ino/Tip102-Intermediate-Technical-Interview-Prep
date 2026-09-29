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
UNDERSTAND:
- Input: considered valid if a complete () [] {}
- Output: True if correct, False if not correct
- Edge Cases: if there was an invalid input to cause an output that isnt True / False

PLAN: 
- First, we want to intitalize the stack 
- Second, Matching Tags () [] {}
- Third, create a set and use an if statement to append only the valid cases,
return True
- Fourth, if not valid we can return False


IMPLEMENT:
(look below)


'''
def is_valid_post_format(posts):
    stack = []
    matchingTags = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for tags in posts:
        if tags in matchingTags:
            stack.append(tags)
        elif tags in matchingTags.values():
            if not stack or matchingTags[stack[-1]] != tags:
                return False
            stack.pop()

    return not stack


if __name__ == "__main__":
    print(is_valid_post_format("()"))
    print(is_valid_post_format("()[]{}"))
    print(is_valid_post_format("(]"))