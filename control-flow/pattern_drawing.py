# pattern_drawing.py

# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to draw each row
while row < size:
    # Use a for loop to draw each column in the current row
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Move to the next line after each row
    row += 1
