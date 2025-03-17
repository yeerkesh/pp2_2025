import re

pattern = r"ab*" # "*" means that b 0 or more
test_strings = ["a", "ab", "abb", "ac", "abc"]

for i in test_strings:
    if re.fullmatch(pattern, i):
        print(f"Matched: {i}")

# metacharacters
# . ^ $ * + ? { } [ ] \ | ( )
# . - any symbol 
# ^ - matches at the beginning of the string
# $ - matches at the end of the string
# * - quantifier, 0 or more repetitions
# + - quantifier, 1 or more repetitions
# ? - quantifier, 0 or 1 repetitions
# {} - quantifier, allows to specify the exact amount of repetitions
# [] - set of characters
# \ - backslash, used for special sequences or escaping character
# | - or, allows to check for 2 or more patterns
# () - grouping