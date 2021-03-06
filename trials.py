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
    """Given a string in snake case, return a string in upper camel case"""

    # Creates an empty list
    camel_case = []

    # Loop through the string and spits at _
    for word in string.split("_"):

        #Takes the first letter of the word and sets it to upper case
        camel_case.append(f"{word[0].upper()}{word[1:]}")

    # Return a joined string of camel_case list
    return "".join(camel_case)


def longest_word_length(words):
    """Return the length of the longest word in the given list of words."""

    # Set variable longest to length of first word in words
    longest = len(words[0])

    # Loop through each word in words
    for word in words:

        # Determine if longest is less than length of current word
        if longest < len(word):

            # If so, set longest to length of current word
            longest = len(word)
    
    # Return longest length
    return longest


def truncate(string):
    """Truncate repeating characters into one character"""

    # Creates an empty list
    result = []

    # Loops through each char in the string
    for char in string:

        # Determines if result is empty list or if the last char in result 
        # is equal to the current char in string
        if len(result) == 0 or char != result[-1]:
            
            #If so, the current char is added to the list
            result.append(char)

    # Returns list w/out duplicates 
    return "".join(result)

def has_balanced_parens(string):
    """Return true if all parentheses in a given string are balanced."""

    # Set variable parens to 0 to count open and close parens
    parens = 0

    # Loop through each char in string
    for char in string:

        # Determine if char is an open paren
        if char == "(":

            # If so, increment parens by 1
            parens += 1

        # Determine if char is a close paren
        elif char == ")":

            # If so, decrement parens by 1
            parens -= 1

    # If parens is not equal to 0, return False
    if parens != 0:
        return False
        
    # Otherwise, return True
    return True


def compress(string):
    """Return a compressed version of the given string."""

    #Creates an empty list
    compressed = []

    # Sets curr_char to an empty string
    curr_char = ""

    # Sets char_count to zero
    char_count = 0

    # Loops through each char of the string
    for char in string:

        # Checks if the char is not equal to the current char
        if char != curr_char:

            # Appends the current char
            compressed.append(curr_char)

            # Checks if the char count is greater than 1
            if char_count > 1:

                #appends the char count as a string
                compressed.append(str(char_count))

            # Sets curr char equal to char
            curr_char = char

            # Sets the char count back to 0
            char_count = 0
        
        # Increases the char count by 1
        char_count += 1
    
    # Appends the current char
    compressed.append(curr_char)

    # Checks if char count is greater than 1
    if char_count > 1:
        # If so, appends the char count as a string
        compressed.append(str(char_count))

    # Returns a joined list of each char and the number of times it appears in the string
    return "".join(compressed)


