# the re library contains functions and methods to use
# these allow for use of regular expressions
# re.search(pattern, string, flags=0)
"""
    .   = any character except a newline
    *   = 0 or more repetitions
    +   = 1 or more repetitions
    ?   = 0 or 1 repetition
    {m} = m repetitions
    {m,n}= m-n repetitions(range)
    ^   = matches the start of a string
    $   = matches the end of string
    []  = set of characters
    [^] = complementing the set(all characters except)
    \w  = any word character
    \W  = now a word character, as well as numbers and the underscore
    \s  = whitespace characters
    \S  = not a whitespace character
    \d  = decimal digit
    \D  = not a decimal digit
    A|B = either A or B
    (...)= a group
    (?:...) = non-capturing version
"""

