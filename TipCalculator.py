print('Welcome to the tip calculator')
bill = float(input('What was the total bill? '))
tip_percent = float(input('What % tip would you like to give?'))
total_people = float(input('How many people are splitting the bill?'))

total_tip = bill * (tip_percent / 100)
bill_with_tip = '{:.2f}'.format(bill + total_tip)
bill_split = ((bill + total_tip) / total_people)
final_amount = '{:.2f}'.format(bill_split, 2)

print(f'the total of the bill with tip is ${bill_with_tip}')
print(f'each person should pay ${final_amount}')
