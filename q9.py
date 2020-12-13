# Write a binary search function. It should take a sorted sequence and the item it is looking for. It should return the index of the item if found. It should return -1 if the item is not found.

import random

def binary_search(lst, left, right, key):
    if left > right:
        return -1
    else:
        mid = (left + right) // 2
        
        if lst[mid] == key:
            return mid
        elif lst[mid] < key:
            return binary_search(lst, mid+1, right, key)
        else:
            return binary_search(lst, left, mid-1, key)


# generate list of random unique integers of length 30
listRandom = random.sample(range(1,100), 30)
listRandom.sort()
print(listRandom)

n = int(input('Enter number to search: '))
result = binary_search(listRandom, 0, len(listRandom)-1, n)
print(result)


