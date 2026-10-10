#Python Exception with both mutable and immutable datatype
#example 1 with number(Immutable)
n1 = 10
n2 = n1
 #both are refferencing to the same memory object but if we change or give a new value then the n2 is still pointing the 10 object but n1 changed because a new object 15 is created in a memory.
n1 = 15
print(n1)
print(n2)
# in immutable datatype when i give a new value to the variable so it create a new object in a memory and as we know we cannot change the immutable datatype.


# EXAMPLE -2 with mutable datatype which is List
l1 = [1,2,3]
l2 = l1
l2[0] = 55
print(l1)
print(l2)
# now if we either edit one of them then it affect both because they are pointing the same object in a memory.

# EXAMPLE -3
# Now we will provide individual value to both l1 and l2
l1 = [1,2,3]
l2 = [1,2,3]
l2[0] = 55
print(l1)
print(l2)
# now both are independent and doesnt affect each other becuase when we assign the mutable datatype individually then it will point to seperate object in a memory.

# EXAMPLE -4
# now we can copy l1 into l2
# NOTE -when we copy the mutable then it create a seperate object in a memory which means they are independent and if we change either l1 or l2 it doesnt affect each other.
l1 = [1,2,3]
l2 = [1,2,3]
l2[0] = 55
print(l1)
print(l2)
