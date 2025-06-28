# SofUni_tasks_and_progects
These are many of my SoftUni code tasks 💻📘   I think they might be helpful for beginners and learners! 🚀

# 📘 My SoftUni Python Tasks

Welcome to my collection of beginner-friendly Python exercises from my time at SoftUni! Each task covers a different concept in programming, and I’ve added clear descriptions below to help you understand what each script does. Perfect for learners! 😊

---

## 🧮 1. Calculate Discounted Price

**Filename:** `discount_calculator.py`

* Calculates total price based on quantity.
* Applies an 18% discount.
* Prints the final price and amount saved.

**Concepts used:** input, float, arithmetic, formatted strings



Price = 7.61
Money = int(input())
PM = Price * Money

Discount = 0.18
PMD = PM * (1 - Discount)
D = PM - PMD

print(f"The final price is: {PMD:.2f} lv.")
print(f"The discount is: {D:.2f} lv.")

---

## ✏️ 2. School Supplies Cost with Discount

**Filename:** `school_supplies.py`

* Asks for number of pens, markers, and cleaning solution in liters.
* Calculates total price.
* Applies user-specified discount percentage.
* Prints the discounted total.

**Concepts used:** input, float, percentages, multi-step calculations



PRISE_PACKAGE_PENS = 5.80
PRISE_PACKAGE_MARKERS = 7.20
PRISE_LITER_PREPARATION = 1.20

number_packages_pens =  int(input())
number_packages_markers = int(input())
needed_liter_preparation = int(input())
percent_discount = int(input()) / 100

prise_materials_without_disco = (number_packages_pens * PRISE_PACKAGE_PENS) + \
(number_packages_markers * PRISE_PACKAGE_MARKERS) + (needed_liter_preparation * PRISE_LITER_PREPARATION)
prise_materials_with_disco = prise_materials_without_disco - (prise_materials_without_disco * percent_discount)

print(prise_materials_with_disco)

---

## 🎁 3. Bonus Points Calculator

**Filename:** `bonus_points.py`

* Based on input points:

  * ≤100 → +5 bonus points
  * > 100 and ≤1000 → +20% of points
  * > 1000 → +10% of points
* Adds extra points if number is even or ends in 5.
* Prints bonus points and total score.

**Concepts used:** if-else, modulus, percentage logic, math operations



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

---

## 🎬 4. Can You Watch the Episode?

**Filename:** `tv_episode_break.py`

* Asks for TV show name, episode duration, and total break time.
* Calculates time spent eating and relaxing.
* Determines if you have enough time left to watch the episode.
* Gives a nice message depending on the result.

**Concepts used:** division, conditional logic, `math.ceil()`




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

---

Thanks for checking out my early Python projects! 🚀 Feel free to explore the code, leave feedback, or suggest improvements. 😄
