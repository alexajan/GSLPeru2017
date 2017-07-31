# SOLUTION Ex. 2
glossary = {'print': 'a function that prints the given object to standard output',
            'list': 'a mutable type of sequence with comma-separated objects',
            'tuple': 'an immutable type of sequence created with parentheses',
            'dictionary': 'a collection of key-value pairs of immutable, unique keys and any type of values',
            'for loops': 'a type of loop that executes a sequence of statements a specified number of times'}
for key, value in glossary.items():
    print(key + ": " + value + "\n")
