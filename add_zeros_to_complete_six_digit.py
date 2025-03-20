# Ask the user to input a number (0-1000)
user_input = input("Input a number (0-1000): ")

# Print the number in 6 digit format
# Add zeros at the beginning to complete the 6 digit
print(user_input.zfill(6))