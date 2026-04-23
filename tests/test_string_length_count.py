def test_count_strings_length_over_8():
    data = ["short", "abcdefgh", "12345678", "tiny", "longstring", "abc"]

    count = sum(1 for s in data if len(s) >= 8)

    assert count == 3