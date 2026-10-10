# In this we will discuss the python exceptions with mutable and Immutable datatypes
# EXAMPLE 1
- We will assign the value of both n1 and n2 which is 
- n1 = 10
- n2 = n1
- so either we change one of them then there will be new object created in a memory and then our variable point to that new reference so it means that both of variables pointing different object in a memory.

# EXAMPLE 2
# We are using list 
- we will first assign the l1 and l2
- l1 = [1,2,3]
- l2 = l1
- now as we know that they both are pointing the same object in a memory and these are mutable so if i change either l1 or l2 then both value affect because they are pointing the same object


# EXAMPLE -3
# Now we will provide individual value to both l1 and l2
- l1 = [1,2,3]
- l2 = [1,2,3]
- l2[0] = 55
- now both are independent and doesnt affect each other becuase when we assign the mutable datatype individually then it will point to seperate object in a memory.

# EXAMPLE -4
- now we can copy l1 into l2
- NOTE -when we copy the mutable then it create a seperate object in a memory which means they are independent and if we change either l1 or l2 it doesnt affect each other.
- l1 = [1,2,3]
- l2 = [1,2,3]
- l2[0] = 55
- print(l1)
- print(l2)