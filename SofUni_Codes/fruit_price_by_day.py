
WORK_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
NOT_WORK_DAY = ['Saturday', 'Sunday']
fruit_list = ['banana', 'apple', 'orange', 'grapefruit', 'kiwi', 'pineapple', 'grapes']

fruit = str(input())
week = str(input())
amount = float(input())
prise = 0

#Work days
if week in WORK_DAYS:
   if fruit == 'banana':
    prise = 2.50
   if fruit == 'apple':
    prise = 1.20
   elif fruit == 'orange':
    prise = 0.85
   elif  fruit == 'grapefruit':
    prise = 1.45
   elif  fruit == 'kiwi':
    prise = 2.70
   elif  fruit == 'pineapple':
    prise = 5.50
   elif  fruit == 'grapes':
    prise = 3.85


#Not work day
if week in NOT_WORK_DAY:
   if fruit == 'banana':
    prise = 2.70
   if fruit == 'apple':
    prise = 1.25
   elif fruit == 'orange':
    prise = 0.90
   elif  fruit == 'grapefruit':
    prise = 1.60
   elif  fruit == 'kiwi':
    prise = 3.00
   elif  fruit == 'pineapple':
    prise = 5.60
   elif  fruit == 'grapes':
    prise = 4.20

if week not in WORK_DAYS and week not in NOT_WORK_DAY:
   print('error')
elif fruit not in fruit_list:
   print('error')

else:
   print(f'{amount * prise:.2f}')