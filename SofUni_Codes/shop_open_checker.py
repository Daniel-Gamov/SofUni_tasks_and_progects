
HOURS = [10, 13, 14, 15, 16, 17, 18]
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

hour_time = int(input())
day_in_week = str(input())

if hour_time in range(10, 18) and day_in_week in week:        
   print("open")
else:
   print('closed')
