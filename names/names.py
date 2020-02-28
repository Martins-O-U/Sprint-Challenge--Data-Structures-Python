import time
from Binary_Search import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()
f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
BST = BinarySearchTree("names")
for name_1 in names_1:
    BST.insert(name_1)

for name_2 in names_2:
    if BST.contains(name_2):
        duplicates.append(name_2)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# original run time was a polynomial "0(n ** 2)"" due to the use of double for loop:
# runtime now is 0(n) is it only does a constant action of append and insert


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
