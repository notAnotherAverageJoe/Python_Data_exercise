def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
   
    vowels = 'aeiouAEIOU'  # Define the set of vowels
    frequency_map = {}     # Initialize an empty dictionary to store vowel counts
    for char in phrase:
        if char in vowels:  # Check if the character is a vowel
            char_lower = char.lower()  # Convert the character to lowercase
            frequency_map[char_lower] = frequency_map.get(char_lower, 0) + 1  # Update the count of the vowel
    return frequency_map