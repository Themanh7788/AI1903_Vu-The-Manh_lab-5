#1. Turn every item of a list into its square
numbers = [1,2,3,4,5,6,7]
new_list = [i**2 for i in numbers]
print(new_list)
#2. Concatenate two lists in the following order
list1 = ["Hello ","take "]
list2 = ["Dear","Sir"]
list3 = [x + y for x in list1 for y in list2]
print(list3)
