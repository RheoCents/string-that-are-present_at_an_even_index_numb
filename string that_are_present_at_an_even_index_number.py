# Write a program to accept a string from the user and display characters that are present at an even index number.
user_input_name = input(str('What is your name '))
user_input_name_number = len(user_input_name)
#input_user_number_of_letters = input('how many letters is in your name ') 
print('The original string is ', {user_input_name} )
for i in range (0, user_input_name_number, 2):
    print(user_input_name[i])
