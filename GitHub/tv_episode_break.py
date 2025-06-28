
import math

serial_name = input()
duration_episode_time = int(input())
duration_brake = int(input())

lunch_time = duration_brake / 8
break_time = duration_brake / 4
time_left = duration_brake - (duration_episode_time + lunch_time + break_time)

if time_left >= 0:
   print(f'You have enough time to watch {serial_name} and left with {math.ceil(time_left)} minutes free time.')
else:
   print(f"You don't have enough time to watch {serial_name}, you need {math.ceil(abs(time_left))} more minutes.")
