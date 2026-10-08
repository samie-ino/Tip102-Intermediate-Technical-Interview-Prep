from q2 import find_smallest_gap

def test_find_smallest_gap():
    # Example 1
    assert find_smallest_gap([(900, 1100), (1300, 1500), (1600, 1800)]) == 60
    # Example 2
    assert find_smallest_gap([(1000, 1130), (1200, 1300), (1400, 1500)]) == 30
    # Example 3
    assert find_smallest_gap([(900, 1100), (1115, 1300), (1315, 1500)]) == 15

    print("All tests for Question 2 passed!")

if __name__ == "__main__":
    test_find_smallest_gap()