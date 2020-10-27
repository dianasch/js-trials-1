"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """Print each item in the given list."""
    #Loop through each item in items
    for item in items:

        #Print each item
        print(item)


def get_all_evens(nums):
    """Given a list of numbers, return a list of all even numbers."""
    # Create an empty list to store even nums
    even_nums = []

    # Loop through each number in nums
    for num in nums:

        # Determine if number is even
        if num % 2 == 0:

            # If so, append to list
            even_nums.append(num)
    
    # Return list
    return even_nums


def get_odd_indices(items):
    """Returns all odd indices within a list"""
    
    #creates and empty list
    result = []

    #loops through each index
    for i in range(len(items)):

        #checks if the index number is even or odd
        if i % 2 != 0:

            #appends the odd index to results
            result.append(items[i])

    # Return list
    return result



def print_as_numbered_list(items):
    """Given a list, output contents as a numbered list."""

    # Set variable i for list numbers
    i = 1

    # Loop through list of items
    for item in items:

        # Print i and item
        print(f"{i}. {item}")

        # Increment i
        i += 1


def get_range(start, stop):
    """Return an list of numbers in a certain range"""

    #creates an empty list
    nums = []

    #num stores the value of start
    num = start

    #Num will be appended to the empty list while it is less than stop
    while num < stop:
        nums.append(num)
        num += 1

    #Returns the list of nums
    return nums


def censor_vowels(word):
    """Given a string, return a string where vowels are replaced with '*'."""

    # Create empty list to store characters
    chars = []

    # Loop through each letter in word
    for letter in word:

        # Determine if letter is a vowel
        if letter in "aeiou":

            # Append an asterisk to list of characters
            chars.append("*")
        
        # If letter is not a vowel, append letter to list of characters
        chars.append(letter)
    
    # Return a joined string of list of characters
    return " ".join(chars)


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
