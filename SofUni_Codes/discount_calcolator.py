Price = 7.61
Money = int(input())
PM = Price * Money

Discount = 0.18
PMD = PM * (1 - Discount)
D = PM - PMD

print(f"The final price is: {PMD:.2f} lv.")
print(f"The discount is: {D:.2f} lv.")