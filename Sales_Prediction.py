'''

A company has determined that its annual profit is typically 23% of toal sales
Write a program that asks the suer to enter the projected amount of total sales, then displays
the profit that will be made from that amount

'''
#Creating variables for use later
projected_Amount = 0
annual_Profit = .23
profit = 0

#asking the user what is the projected amount and calculating profit
projected_Amount = int(input("Please enter the projected amount of total sales: "))
profit = projected_Amount * annual_Profit

#showing the profit
print(f"The profit made from {projected_Amount} is {profit}")