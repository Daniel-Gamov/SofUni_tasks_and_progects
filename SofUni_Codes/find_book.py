books_num = 0
book_of_Ani = str(input())

while True:
   gess_book = str(input())
   books_num += 1
   if gess_book == "No More Books":
       if gess_book == book_of_Ani:
           books_num -= 1
           print(f"You checked {books_num} books and found it.")
           break
       else:
           books_num -= 1
           print('The book you search is not here!')
           print(f'You checked {books_num} books.')
           break
   if gess_book == book_of_Ani:
       books_num -= 1
       print(f"You checked {books_num} books and found it.")
       break
   else:
       continue
