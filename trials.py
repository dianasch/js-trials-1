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
    pass  # TODO: replace this line with your code


def censor_vowels(word):
    pass  # TODO: replace this line with your code


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
