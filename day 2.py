cost_meal = float(input(' '))
tip = int(input(' ')) * 0.01
tax = int(input(' ')) * 0.01
total_cost = cost_meal + (cost_meal * tip) + (cost_meal * tax)
round(total_cost)
print(total_cost)