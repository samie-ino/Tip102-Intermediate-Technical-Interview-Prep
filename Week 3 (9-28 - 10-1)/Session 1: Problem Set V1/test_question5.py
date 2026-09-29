from problem5_content_cleaner import clean_post

def test_clean_post():
    assert clean_post("pooost") == "pooost"
    assert clean_post("abBACC") == ""
    assert clean_post("s") == "s"