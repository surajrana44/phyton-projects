'''
# input for rent calculator 

1. total rent
2. number of people sharing 
3.elecyricity bill
4.kitchem groceries
5. miscellaneous expenses
6.food cost

'''

rent=int(input('Enter total rent: '))
people=int(input('Enter number of people sharing: '))
electricity_bill=int(input('Enter electricity bill: '))
groceries=int(input('Enter kitchen groceries: '))
miscellaneous=int(input('Enter miscellaneous expenses: '))
food_cost=int(input('Enter food cost: '))

total_expense = rent + electricity_bill + groceries + miscellaneous + food_cost
per_person = total_expense / people

print(f'Total expense: {total_expense} \nPer person expense: {per_person}')