import pytest

@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("hello", "HELLO"),
        ("hyeonwoo", "HYEONWOO"),
        ("Hello123", "HELLO123"),
        ("", ""),
    ]
)
def test_uppercase_conversion_various_cases(input_text, expected):
    assert input_text.upper() == expected