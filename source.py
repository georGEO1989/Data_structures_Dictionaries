# 1. Creating a dictionary
a = {}
print (a)

# 2. Setting up a new dictionary for our computer list and adding key:value pairs
computer_list = {}

computer_list["Comp1"] = "Station1"
computer_list["Comp2"] = "Station2"
computer_list["Comp3"] = "Station3"
computer_list["Comp4"] = "Station4"
computer_list["Comp5"] = "Station5"

print (computer_list)

# 3. Get length of dictionary
print (len(computer_list))

# 4. Delete entry dictionary
del computer_list['Comp5']

print (computer_list)

# 5. basic looping through your new list
for k, v in computer_list.items():
    print(k,v)

# 6. Enumerating our dictionary
for a, b in enumerate(computer_list):
    print (a, b)

# 7. Look into the list to find a specific key
# use this in place of getting the computer name
node_name = input("Enter computer name:\n")
node_name = node_name[0].upper() + node_name[1:]

if node_name in computer_list:
    print (computer_list.get(node_name))
else:
    print("Please use a designated computer for this program")
