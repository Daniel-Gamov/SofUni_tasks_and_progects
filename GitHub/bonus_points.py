BONUS_UP_TO_100 = 5
BONUS_ABOVE_100_PERCENT = 0.20
BONUS_ABOVE_1000_PERCENT = 0.10

BONUS_EVEN_NUMBER = 1
BONUS_ENDS_IN_5 = 2

starting_points = int(input())

bonus_paints = 0
if starting_points <= 100:
   bonus_paints += BONUS_UP_TO_100
elif starting_points > 1000:
   bonus_paints += (starting_points * BONUS_ABOVE_1000_PERCENT)
else:
   bonus_paints += (starting_points * BONUS_ABOVE_100_PERCENT)

if starting_points % 2 == 0:
   bonus_paints += BONUS_EVEN_NUMBER
elif starting_points % 10 == 5:
   bonus_paints += BONUS_ENDS_IN_5

print(bonus_paints)
print(bonus_paints + starting_points)
