#1.creating a list
list1 = [1,2,3]
print(list1)
list2 = [1.0,'Jessa',3]
print(list2)
list3 = []
print(list3)
#2Concatenate two lists index-wise
list1 = ["M","na","i","Ke"]
list2 = ["y","me","s","lly"]
list3 = [i+j for i,j in zip(list1,list2)]
print(list3)

