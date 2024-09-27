# Program: Basic Multiplication Table
# Author: Connor Shoen

# 1.) Ask user for a number
# 2.) Print out the name of the multiplication table:
    # "multiplication table for [number]"

# 3.) for loop print out all the multiplication facts (1-12) for the user's number


# Create Code

number = int(input("Please enter a number to create a multiplication table: "))
start = 1
end = 12

print("Multiplication Table for", number)
print("----------------------------------")
print("|  ", number, "x 1 =", number * 1, "  |")
print("|  ", number, "x 2 =", number * 2, "  |")
print("|  ", number, "x 3 =", number * 3, "  |")
print("|  ", number, "x 4 =", number * 4, "  |")
print("|  ", number, "x 5 =", number * 5, "  |")
print("|  ", number, "x 6 =", number * 6, "  |")
print("|  ", number, "x 7 =", number * 7, "  |")
print("|  ", number, "x 8 =", number * 8, "  |")
print("|  ", number, "x 9 =", number * 9, "  |")
print("|  ", number, "x 10 =", number * 10, "  |")
print("|  ", number, "x 11 =", number * 11, "  |")
print("|  ", number, "x 12 =", number * 12, "  |")
print("----------------------------------")

# Multiplication Table Generator with custom range and multi-table option

# 1.) Ask the user if they want to generate multiple tables
# 2.) Create a function for to do steps 2 & 3 above (3 variables: number, start = 1, end = 12)
# 3.) Create a control structure to handle the user's answer from step 1
    # What do we do if yes?
    # What do we do if no?