
product = input()
city = input()
amount = float(input())
prise = 0

#----------------------------sofia
if city == 'Sofia' and product == 'coffee':
   prise = 0.50
elif city == 'Sofia' and product == 'water':
   prise = 0.80
elif city == 'Sofia' and product == 'beer':
   prise = 1.20
elif city == 'Sofia' and product == 'sweets':
   prise = 1.45
elif city == 'Sofia' and product == 'peanuts':
   prise = 1.60
#----------------------------Plovdiv
if city == 'Plovdiv' and product == 'coffee':
   prise = 0.40
elif city == 'Plovdiv' and product == 'water':
   prise = 0.70
elif city == 'Plovdiv' and product == 'beer':
   prise = 1.15
elif city == 'Plovdiv' and product == 'sweets':
  prise = 1.30
elif city == 'Plovdiv' and product == 'peanuts':
   prise = 1.50
#----------------------------Varna
if city == 'Varna' and product == 'coffee':
   prise = 0.45
elif city == 'Varna' and product == 'water':
   prise = 0.70
elif city == 'Varna' and product == 'beer':
   prise = 1.10
elif city == 'Varna' and product == 'sweets':
   prise = 1.35
elif city == 'Varna' and product == 'peanuts':
   prise = 1.55

AP = prise * amount

print(AP)
