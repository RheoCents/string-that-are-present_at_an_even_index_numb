# Write a program to accept a string from the user and display characters that are present at an even index number.
user_input_name = input(str('What is your name '))
user_input_name_number = len(user_input_name)
print('The original inputed data is ', {user_input_name} )
print('Printing only the even letter of the numbers')
for i in range (0, user_input_name_number, 2):
    print(user_input_name[i])
