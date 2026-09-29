from problem1_post_format_validator import is_valid_post_format

def test_is_valid_post_format():
    assert is_valid_post_format("()") == True
    assert is_valid_post_format("()[]{}") == True
    assert is_valid_post_format("(]") == False