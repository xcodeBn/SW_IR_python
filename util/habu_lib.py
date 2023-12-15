import re


def remove_special_characters(text):
    """
    Removes special characters at the beginning or end of a word from the given text.

    Args:
    - text (str): The input text containing words with potential special characters.

    Returns:
    - str: The text with special characters removed from the start or end of each word.

    Example:
    >>> remove_special_characters(",stella")
    'stella'
    """
    pattern = r'(^\W+|\W+$)'
    result = re.sub(pattern, '', text)
    return result


if __name__ == "__main__":
    # Test cases remain unchanged
    test_cases = [
        (",stella", "stella"),
        (".`,.,monkey.,.,.", "monkey"),
        (",,2012", "2012"),
        ("$apple$", "apple"),  # Special characters within the word, should remain unchanged
        ("@#%banana", "banana"),  # Special characters at the start, but not end, should remain unchanged
        ("grape!!$", "grape"),  # Special characters at the end, but not start, should remain unchanged
        (",$watermelon$!", "watermelon"),  # Special characters at both start and end
        ("$%^", ""),  # Special characters only, should return an empty string
        ("apple,.", "apple"),  # No special characters at start or end, should remain unchanged
        ("user@example.com", "user@example.com"),  # Email address, should remain unchanged
        ("vb.net", "vb.net")  # Special case: term with a dot
    ]

    # Test the function against the updated test cases
    for input_text, expected_output in test_cases:
        result = remove_special_characters(input_text)
        assert result == expected_output, f"Input: {input_text}, Expected: {expected_output}, Result: {result}"

    print("All test cases passed successfully!")
