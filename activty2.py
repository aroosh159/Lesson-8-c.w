#creating a set
my_set = {1,2,2,3,4,4}
print(my_set)
#Adding in a set
my_set.add(8)
print("Updated Set:",my_set)
#Creating new set
set1 = my_set
set2 = {2,4,6,6,0}
#Printing set1 and set2
print("\nSet1:",set1)
print("\nSet2:",set2)
#Difference and Symmetric diffrence
print("Difference:")
print(set1.difference(set2))
print("Symmetric Difference:")
print(set1.symmetric_difference(set2))