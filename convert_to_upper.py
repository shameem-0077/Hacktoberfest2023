def convert_to_uppercase(input_string):
    """
    Converts all letters in the input string to uppercase.
    
    Args:
        input_string (str): The input string to convert.
        
    Returns:
        str: The input string with all letters converted to uppercase.
    """
    return input_string.upper()

# Example usage:
original_string = "Hello World"
uppercase_string = convert_to_uppercase(original_string)
print(uppercase_string)
