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