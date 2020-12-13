#  Create a list with the names of friends and colleagues. Search for the name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

# Searching using linear search
friends = ['Will', 'Jean', 'Sam', 'John', 'Reece', 'Bob']

friend = 'John'
msg = ''

for i in range(len(friends) - 1):
    if friends[i] == friend:
        msg = f'{friend} found in index {i}'
        break
    else:
        msg = 'Not Found'

print(msg)