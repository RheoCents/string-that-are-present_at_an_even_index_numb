# Write a program to accept a string from the user and display characters that are present at an even index number.
user_input_name = input('What is your name ')
input_user_number_of_letters = input('how many letters is in your name ') 
for i in range (0, int(input_user_number_of_letters), 2):
    print(user_input_name[i])