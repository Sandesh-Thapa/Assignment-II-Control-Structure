#  Create a tuple with your first name, last name, and age. Create a list, people, and append your tuple to it. Make more tuples with the corresponding information from your friends and append them to the list. Sort the list. When you learn about sort method, you can use the key parameter to sort by any field in the tuple, first name, last name, or age.

list1 = []
tup1 = ('John', 'Doe', 18)
tup2 = ('Jean', 'Doe', 45)
tup3 = ('Sam', 'Kenny', 68)
tup4 = ('Will', 'Smith', 17)
tup5 = ('Brad', 'Traversy', 30)

list1.append(tup1)
list1.append(tup2)
list1.append(tup3)
list1.append(tup4)
list1.append(tup5)

def sortBySecondName(elem):
    return elem[1]

def sortByAge(elem):
    return elem[2]

# sort by first name
list1.sort()
print(list1)

#sort by last name
list1.sort(key=sortBySecondName)
print(list1)

#sort by age
list1.sort(key=sortByAge)
print(list1)

