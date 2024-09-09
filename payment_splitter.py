print('Welcome to Tip Calculator / Payment Splitter') 
# User inputs the total amount that needs to be split
Total_amount = int(input('Total amount = '))
# User inputs the percentage of the tip
tip = int(input('Tip percentage = '))
# User inputs the number of people to split the amount
people = int(input('Number of people = '))

# Calculating the remaining amount to be split after tip
tip_amount = (tip / 100) * Total_amount
remaining_amount = Total_amount + tip_amount

# Output the remaining amount to be split
print(f'Remaining amount to be split = {remaining_amount}')

# Calculating the final amount each person needs to pay
final_per_person = remaining_amount / people

# Output the final amount each person needs to pay
print(f'Final amount per person: {final_per_person}')
