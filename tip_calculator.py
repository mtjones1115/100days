# one hundred days of code day two

sub_total = float(input("What was the total bill? \n"))
tip_percentage = int(input("What percentage tip would you like to give? \n"))
bill_split = int(input("How many poeple to split the bill? \n"))

bill_total = sub_total*(1+tip_percentage/100)/bill_split
tidy_total = round(bill_total, 2)
tidy_total = "{:.2f}".format(tidy_total)
message = f"Each person should pay: {tidy_total}"

print(message)

