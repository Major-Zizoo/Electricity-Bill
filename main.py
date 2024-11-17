units= int(input("Enter units:"))
if units <50:
    amount=2.60*units
    tax=25

elif units<100:
    amount=3.25*units
    tax=35

elif units<200:
    amount=5.25*units
    tax=45

else:
    amount=8.25*units
    tax=55

total=amount+tax
print("Total is:",total)      