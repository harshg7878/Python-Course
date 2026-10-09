# example of mutable datatype
list = [1,2,3]
list.append(10)
print(list)

# example of immutable datatype
string = "harsh"
string = string +" gupta"
print(string)

# now we thought that string is immutable but how it will changed right?
# so it doesnt change the same object it create a new object in a memory and then point the variable to that new object.
# simply means it create a copy of existing value and then reassign to the variable.

# but if we try to change the same object then see what will happen
str = "harsh"
str[0]="H"
print(str)

# now it will throw an error
