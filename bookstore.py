header="""\tWELCOME TO OUR BOOK SHOP
\t\tTVM,KERALA
------------------------------------------\n"""

book1_title= "Python Basics"
book1_price= 450

book2_title= "Data Science Intro"
book2_price= 600

item_format="book:\t{}\t\t₹{}"
line1=item_format.format(book1_title,book1_price)
line2=item_format.format(book2_title,book2_price)
print("-------------------------------------------")

total_price=book1_price+book2_price
total_line="TOTAL PRICE:₹{}\n".format(total_price)

thank_you="------------------------------------------\nTHANK YOU FOR SHOPPING"
finally_receipt = header + line1 + "\n" + line2 + "\n" + total_line + thank_you

print(finally_receipt.upper())