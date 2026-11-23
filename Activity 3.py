"""Write a program to create an array with the following elements
 - [1, 3, 5, 3, 7, 9, 3]. Then find the number of occurrences of 
 number 3 in the array. Also, print the reversed array."""

import array as arr

array1 = arr.array('i', [1,3,5,3,7,9,3])
print("The original array is: ", array1)

print("The number 3 appears", array1.count(3), "times")
array1.reverse()
print("The array reversed is: ", array1)

