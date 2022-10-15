# Create a function that will take a string as an input and return the 1st unique letter of a string.
# “Google” => “l”
# “Amazon” => “m”
# If there are no unique letters, return an empty string: “xoxoxo” => “”.
# How would you test it? How would you handle edge cases?

def find_unique(string):
    for i in string:
        if string.lower().count(i.lower())==1:
            return i
    return ""

print(find_unique('Google'))
print(find_unique('Amazon'))
print(find_unique('xoxoxo'))
print(find_unique('Festival'))
print(find_unique('xoXOxo'))
print(find_unique('Yahoo'))
print(find_unique('SCISSORS'))
print(find_unique('n'))
print(find_unique('M'))
print(find_unique('ttttttttttt'))
print(find_unique('sssSSSSsSssRRrRRrrrRRRr'))
print(find_unique('asgSDHWQQSDFvGGHdSGDaSasFdKFWBJFDdhlshgSkjfgJUecFFHkIo'))

