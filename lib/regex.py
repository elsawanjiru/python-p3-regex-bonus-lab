import re

# Define the regular expression pattern
my_pattern = r"(It's such a lovely day today\.|Some weather we're having today, huh?|Maybe today's just not my day\.)"

# Compile the regular expression
my_regex = re.compile(my_pattern)

# Test the regular expression against a list of strings
test_strings = [
    "It's such a lovely day today.",
    "Some weather we're having today, huh?",
    "Maybe today's just not my day.",
]

# Use the findall() method to check if the regular expression matches all strings
found_strings = my_regex.findall('\n'.join(test_strings))

if found_strings == test_strings:
    print("Regular expression matches all three strings.")
else:
    print("Regular expression does not match all three strings.")
