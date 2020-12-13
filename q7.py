# Create a list of tuples of first name, last name, and age for your friends and colleagues. If you don't know the age, put in None. Calculate the average age, skipping over any None values. Print out each name, followed by old or young if they are above or below the average age.

listFriend = []
tup1 = ('John', 'Doe', 18)
tup2 = ('Jean', 'Doe', None)
tup3 = ('Sam', 'Kenny', None)
tup4 = ('Will', 'Smith', 17)
tup5 = ('Brad', 'Traversy', 30)

listFriend.append(tup1)
listFriend.append(tup2)
listFriend.append(tup3)
listFriend.append(tup4)
listFriend.append(tup5)

sum = 0
count = 0

for friend in listFriend:
    if friend[2] == None:
        continue
    else:
        sum += friend[2]
        count += 1

avgAge = sum//count

for friend in listFriend:
    if friend[2] == None:
        continue
    else:
        if friend[2] <= avgAge:
            print(f'{friend[0]} {friend[1]} young')
        else:
            print(f'{friend[0]} {friend[1]} old')

