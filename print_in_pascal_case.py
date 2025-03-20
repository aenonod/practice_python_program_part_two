# Ask the user to input their fullname in incorrect casing
name = input("Input your full name (in incorrect casing): ")

# Print the input in pascal case
proper_case = name.title()
print("".join(proper_case.split()))