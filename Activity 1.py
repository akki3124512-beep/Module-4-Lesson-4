"""Write a program to create a set and perform the following operations
 on that set- 1. Create a set with integer elements 2. Create a set with
   mixed data type elements 3. Create another set with elements - 1, 2, 3, 4, 3, 2 4.
     Create a set from a list with elements - [1, 2, 3, 2] 5. Print the set after
       removing the first element from this set - [0, 1, 3, 4, 5]"""





set1 = {1,1,2,3,4,1,2,4,2,4,56,1,2}
print(set1)

set2 = {3, "Hello", (1,2,3,2)}
print(set2)

set3 = {1,2,3,4,3,2,4}
print(set3)

list4 = [1,2,3,2]
set = set([1,2,3,2])
print(set)

set = {0,1,3,4,5}
set.pop()
print(set)