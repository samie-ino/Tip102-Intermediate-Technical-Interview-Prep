from q3 import calculate_expenses

def test_calculate_expenses():
    # Example 1
    e1 = [("Food", 12.5), ("Transport", 15.0), ("Accommodation", 50.0), 
          ("Food", 7.5), ("Transport", 10.0), ("Food", 10.0)]
    res_dict1, highest1 = calculate_expenses(e1)
    assert res_dict1 == {'Food': 30.0, 'Transport': 25.0, 'Accommodation': 50.0}
    assert highest1 == 'Accommodation'

    # Example 2
    e2 = [("Entertainment", 20.0), ("Food", 15.0), ("Transport", 10.0), 
          ("Entertainment", 5.0), ("Food", 25.0), ("Accommodation", 40.0)]
    res_dict2, highest2 = calculate_expenses(e2)
    assert res_dict2 == {'Entertainment': 25.0, 'Food': 40.0, 'Transport': 10.0, 'Accommodation': 40.0}
    assert highest2 == 'Food'

    # Example 3
    e3 = [("Utilities", 100.0), ("Food", 50.0), ("Transport", 75.0), 
          ("Utilities", 50.0), ("Food", 25.0)]
    res_dict3, highest3 = calculate_expenses(e3)
    assert res_dict3 == {'Utilities': 150.0, 'Food': 75.0, 'Transport': 75.0}
    assert highest3 == 'Utilities'

    print("All tests for Question 3 passed!")

if __name__ == "__main__":
    test_calculate_expenses()
    