from q1 import find_task_pair

def test_find_task_pair():
    # Example 1
    assert find_task_pair([30, 45, 60, 90, 120], 105) == True
    # Example 2
    assert find_task_pair([15, 25, 35, 45, 55], 100) == True
    # Example 3
    assert find_task_pair([20, 30, 50, 70], 60) == False
    # Edge Cases
    assert find_task_pair([], 100) == False
    assert find_task_pair([50], 50) == False
    print("q1 tests passed!")

if __name__ == "__main__":
    test_find_task_pair()