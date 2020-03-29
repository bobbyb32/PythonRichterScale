#PYTHON RICHTER SCALE CALCULATION
#Your first and last name: Robert Betlesky
#Your ID: s1114185

#REQUIREMENTS:
# ask the user to "Enter the Richter scale value or -99 to end: "
# the program must end when the user enters -99
# the richter scale value entered must be greater than 0
# if the richter scale value is less than 0, the program must print  "Value must be greater than 0"
#   and the user must re-enter the richter scale value
# program must print the correct warning message for the richter scale value entered as per the accompanying diagram
# program must print only 1 warning message for each richter scale value entered
# the program must be tested so that it repeats until user enters -99
# the program must be tested so that if user enters a richter scale value less than 0,
#   "Value must be greater than 0" prints and the user must re-enter it
# the program must be tested with each of the following values to make sure the correct warning message is printed
#    8.1, 8.0, 7.1, 7.0, 6.1, 6.0, 4.6, 4.5, 4,4, -4.6
#-------------------------------------------------------------------------

# HINT: Use the base number conversion program for guidance
#--------------------------------------------------------------------------------------------
# 1. Develop the ALGORITHM for Richter Scale program from the requirements and enter it below
#--------------------------------------------------------------------------------------------
# Input Richter Scale Value, Decimal Format
# while (the value is greater than 0)
    # Evaluate the value at the appropriate richter scale
    # Output appropriate warning message
# If value is less than 0
    # Output message "Value must be greater than 0"
# Have the program rerun the while loop until the requirement is met
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# 2. Convert the ALGORITHM to PSEUDOCODE and enter it below
#-------------------------------------------------------------------------
# Write "Enter the Richer scale value or -99 to end: "
# Read userValue
# Set doMore equal to true
# while (true)
#  if(uservalue == -99, set doMore to false)
# elseIf(userValue < 0, ask for userValue again and output "Value must be greater than 0"
# elseIf(user value less than 4.5, output "Damage to poorly constructed buildings"
# elseIf(user value greater than equal to 4.5 but less than 6.0, output "Damage to poorly constructed buildings")
# elseIf(user value greater than equal to 6.0 but less than 7.0, output "Many buildings considerably damaged, some collapse")
# elseIf(user value greater than equal to 7.0 but less than 8.0, output "Many buildings destroyed")
# elseIf(user value greater than or equal to 8.0, output "Most structures fall")
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# 3. Convert the PSEUDOCODE into PYTHON CODE and enter it below
#-------------------------------------------------------------------------
print("Enter the Richter scale value or -99 to end: ")
userValue = float(input())
doMore = True
while doMore == True:
    if userValue == -99:
        doMore = False
        continue
    elif userValue < 0:
        print("Value must be greater than 0")
        userValue = float(input())
    elif userValue >= 0 and userValue < 4.5:
        print("No destruction of buildings")
        doMore = False
    elif userValue >= 4.5 and userValue < 6.0:
        print("Damage to poorly constructed buildings")
        doMore = False
    elif userValue >= 6.0 and userValue < 7.0:
        print("Many buildings considerably damaged, some collapse")
        doMore = False
    elif userValue >=7.0 and userValue < 8.0:
        print("Many buildings destroyed")
        doMore = False
    elif userValue >= 8.0:
        print("Most structures fall")
        doMore = False
