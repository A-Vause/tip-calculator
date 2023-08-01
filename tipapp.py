print("Welcome to tip calculator." )
bill = float(input("what was the total bill? $"))
tip_amount = int(input("What percentage would you like to tip? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_int = int(bill)
tip_amount_int = int(tip_amount)
people_int = int(people)

tip_amount_percentage = tip_amount_int / 100
tip_amount_dollars = tip_amount_percentage * bill_int
bill_total = bill_int + tip_amount_dollars
bill_shared = round(bill_total / people_int, 2)


print(f"Each person should pay ${bill_shared}")