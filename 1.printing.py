
# 1. Using the print method, print "Hello World"
new_variable = "Hello World"
# print(new_variable)

# 2. Create variables for the data type below. 
# Data Types:
# Int
new_int = 1
# print(new_int)

# Float
new_float = 1.0
# print(new_float)

# String
new_string = "1, 2, 3, 4"
# print(new_string)

# Boolean 
new_boo = True
# print(new_boo)

# Boolean (The other boolean value)
false_boo = False
# print(false_boo)

# Lists ( 4 items in list min.)
new_list = [1, 2, 3, 4, 5]
# print([new_list])

# Dictionaries  ( 4 key/value pairs min.)
new_dictionary = {
    "name": "Adrian",
    "age": 100,
    "married": True,
    "number_of_kids": 2
}
# print(new_dictionary)

# 3. For each of the variables, use the print method for each variable. To print each varible

# 4. Backtick ` in JS are used for Template literals. In a JS file a variable called intVariable and stringVariable exist.
# They are equal to the int and string variables on step 2.
# What is the python equvalent for: console.log(`int: ${intVariable}, string ${stringVariable}`)
# print("5" + str(6))
# print(f'int: {int_v}, string{string_v} ')


# 5. Comment out all print statements up to this point

# 6. Write a FOR LOOP in python that prints "David Rocks" 5 times
# Hint: type this into google "loop range python"
# for x in range(5):
#     print("David Rocks")

# 7. Declare a function what print "Alex Rocks". Invoke that function 5 times. 

# def alex_teacher():
#     print("Alex Rocks")
# for x in range(5):
#     print("Alex Rocks")

# 8. Declare a function that takes in 2 parameters. 
# It will print "P1(your parameter1) and P2(your parameter2) Rocks"
# Now call that function using "Kyle" and "Winston" as the arguments 
# invoke that function 4 more times

# def two_params(param1, param2):
#     # print(param1 + " " + "and " + param2  + " rocks")
#     print(f'{param1} and {param2} Rocks')
# # two_params(param1="Kyle", param2="Winston")
#     two_params("Kyle", "Winston")

# for x in range(4):
#     two_params('kyle', 'Winston')


# Definitions:  
# P is for Placeholder. P is for Parameters.
# These 2 start w/ the letter P 
# A parameter is variable in the declaration of the function - The place holder

# A is for actual value. A is for aguement.
# These 2 start w/ the letter A
# Arguement is are the values when calling the function - The actual value

# 9. Remember the list variable in step 2. 
# a. Print the index at 3. Then comment it out
# new_list = [1, 2, 3, 4, 5]
# print(new_list[3])

# b. Now print the index at 100. Does this error? comment it out
# print([new_list[100]])
# It errors and says it is out of range.

# e. Now print the index at -1 index. Observe what it prints. Then comment it out
# print(new_list[-1])

# f. Now print the index at -100.  Does this error? comment it out
# print(new_list[-100])
# error. list index out of range

# 10. Write a FOR LOOP in python that prints each item in the list variable in step 2.  
# The staring number MUST be a negative number. The ending number MUST be postive number
# Looking to get each item printed once in order and then a second time in order
# new_list.insert(0,0)
# new_list.insert(0, -1)
# # print([new_list])

# for item in new_list:
#     print(item)
# for x in range(-5, 5):
#     print(new_list[x])


# 11. Write a WHILE LOOP in python that does the same thing as 10.
# counter = 0
# while (counter <1):
#     print(new_list)
#     counter += 1 

ind = -4
while(ind < 4):
    print(new_list[ind])
    ind +=1

# 12. For loops.
# Write a FOR LOOP in python that prints each item in list variable in step 2.  
# Hint: type this into google "loop python"
# for item in new_list:
#     print(item)

# 13. Repeat step 12 but instead of the list variable, use the dictionary variable. 
# Print each key
for key in new_dictionary.keys():
    print(key)

# 14. Repeat step 13. Instead of printing each key, print each value
# Hint: google "dictionary values python"
# new_dictionary = {
#     "name": "Adrian",
#     "age": 100,
#     "married": True,
#     "number_of_kids": 2
# }
for value in new_dictionary.values():
    print(value)

    print(new_dictionary.keys())
    print(new_dictionary.values())