from problem3_check_symmetry_in_post_titles import is_symmetrical_title

def test_is_symmetrical_title():
    assert is_symmetrical_title("A Santa at NASA") == True
    assert is_symmetrical_title("Social Media") == False