import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# original solution
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# binary search tree ~0.05s
# bst = BinarySearchTree(names_1[0])
# for i in range(1, len(names_1) - 1):
#     bst.insert(names_1[i])
#
# for name in names_2:
#     if bst.contains(name):
#         duplicates.append(name)

# dictionary ~0.005s
# dictionary_1 = {}
# for name in names_1:
#     dictionary_1[name] = name
#
# for name in names_2:
#     if name in dictionary_1:
#         duplicates.append(name)

# Stretch Solution ~0.06s
# sort the array first
names_1.sort()

# binary search it
for name in names_2:
    low = 0
    high = len(names_1) - 1
    # binary search
    while high - low > -1:
        mid = low + (high - low) // 2
        if names_1[mid] == name:
            duplicates.append(name)
            break

        if high - low == 1 or high == low:
          # we were down to the last element, if it's not here
          # break
          if names_1[high] != name:
            break
          else:
              duplicates.append(name)
              break
        elif name > names_1[mid]:
          low = mid
        else:
          high = mid



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

