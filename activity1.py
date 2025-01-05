#empty turple
my_turple = ()
#Turple having elements and diffrent types of elements
my_turple = (1,2,3,4,5)
my_turple = ("exa",8,9,9.9)
print(my_turple)
#nested turple
my_turple = ("Beta",[8,9,3])
print(my_turple)
#nested index
my_turple = ("beta",[4,0,6])
print(my_turple[0][2])
print(my_turple[1][2])
#slicing
my_turple = ("A","Y","E","S","H","A")
print("Slicied:",my_turple[0:4])
#iterating through turple
for letter in(my_turple):
    print("Hello",letter)