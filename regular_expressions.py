# the re library contains functions and methods to use
# these allow for use of regular expressions
# re.search(pattern, string, flags=0)
# re.match(pattern, string, flags=0) this function does not require '^' or '$' to specify the start or end of the regular expression
# re.sub(pattern, repl, string, count=0, flags=0)
# re.findall(pattern, string, flags=0)
# re.split(pattern, string, maxsplit=0, flags=0)
"""
    .   = any character except a newline
    *   = 0 or more repetitions
    +   = 1 or more repetitions
    ?   = 0 or 1 repetition(optional)
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
    /   = escape character, to escape dots etc
"""

# FLAGS
"""
    re.IGNORECASE   = Ignores the case of the string
    re.MULTILINE    = handle input that spans multiple lines
    re.DOTALL       = tells the dot to accept all characters plus newline
"""

