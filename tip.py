print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
percentage = int(input("What percentage would you like to give? 10, 12, or 15? "))
split_count = int(input("How many people to split the bill? "))

amount = (percentage / 100) * bill + bill
each_share = amount / split_count
print(round(each_share, 2))
