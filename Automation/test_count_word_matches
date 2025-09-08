import pytest
from count_word_matches import count_word_matches

# -----------------
# Exercise 1: Basic Parameterized Tests
# -----------------
@pytest.mark.parametrize("text, target, expected", [
    ("The cat sat on the mat", "cat", 1),
    ("Dog dog DOG dOg", "dog", 4),
    ("Hello world", "world", 1),
    ("hello hello HELLO", "hello", 3),
    ("No matches here", "yes", 0),
    ("catcat cat catdog", "cat", 1),
    ("a a a", "a", 3)
])
def test_basic(text, target, expected):
    assert count_word_matches(text, target) == expected


# -----------------
# Exercise 2: Edge Case Testing
# -----------------
@pytest.mark.parametrize("text, target, expected", [
    ("", "word", 0),                # Empty text
    ("hello world", "", 0),         # Empty target
    ("", "", 0),                    # Both empty
    ("hello  world", "world", 1),   # Multiple spaces
    (" cat ", "cat", 1),            # Leading/trailing spaces
    ("cat,dog cat", "cat", 2),      # Punctuation not handled
    ("x y z", "x", 1)               # Single character
])
def test_edge_cases(text, target, expected):
    assert count_word_matches(text, target) == expected


# -----------------
# Exercise 3: Negative Testing
# -----------------
@pytest.mark.parametrize("text, target", [
    (None, "word"),
    ("hello world", None),
    (123, "word"),
    ("hello world", 456),
    (["hello", "world"], "world"),
    ("hello world", ["world"])
])
def test_invalid_inputs(text, target):
    with pytest.raises(TypeError):
        count_word_matches(text, target)
