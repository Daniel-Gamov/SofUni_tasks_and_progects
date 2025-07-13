unsatisfactory = int(input())

unsatisfactory_num = 0
num_problem = 0
str_problem = ''
total_grades = 0
while True:

   problem = str(input())
   num_problem += 1

   if problem == 'Enough':


       num_problem -= 1

       print(f'Average score: {total_grades / num_problem:.2f}')
       print(f'Number of problems: {num_problem}')
       print(f"Last problem: {str_problem}")
       break
   else:
       str_problem = problem
   grade = float(input())
   total_grades += grade

   if grade > 4:
       continue
   else:
       unsatisfactory_num += 1

   if unsatisfactory_num == unsatisfactory:
       print(f'You need a break, {unsatisfactory} poor grades.')
       break