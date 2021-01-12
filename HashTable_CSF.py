# @Rexhino_Kovaci
# hash tables we use dictionaries as it is an array whose indexes are obtained using a hash function on the keys
# we use 3 collision handling problems: linear, quadratic, double hashing
# we are obliged to use ASCII values and divide it by the element of our array/dictionary


# declare a dictionary
dict = {'Name': 'Rexhino', 'Age': 19, 'Class': 'CE/IT'}

# Accessing the dictionary with its key
print( "dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])



# modify the dictionary
dict = {'Name': '', 'Age': 99, 'Class': 'None'}
dict['Age'] = 98 # update existing entry
dict['School'] = "Canadian Institute of Technology" # add new entry
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])