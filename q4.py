# Create a list. Append the names of your colleagues and friends to it. Has the id of the list changed? Sort the list. What is the first item on the list? What is the second item on the list?

n = int(input('Enter number of friends: '))

friendList = []
print(id(friendList))

for i in range(n):
    friend = input(f'Enter {i+1}th friend name: ')
    friendList.append(friend)

print(id(friendList))

friendList.sort()
print(friendList[0])
print(friendList[1])
