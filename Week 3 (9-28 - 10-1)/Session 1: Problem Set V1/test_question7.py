from problem7_post_compare import post_compare

def test_post_compare():
    assert post_compare("abc", "ad#c") == True
    assert post_compare("ab##", "c#d#") == True
    assert post_compare("a#c", "b") == False