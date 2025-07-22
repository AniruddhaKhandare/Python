# def add_three(input_var):
#     output_var = input_var + 3
#     return output_var

# new_number = add_three(10)
# print(new_number)

# def get_pay(num_hours):
#     pay_pretax = num_hours * 15
#     pay_aftertax = pay_pretax * (1 - 0.12)
#     return pay_aftertax

# pay_fulltime = get_pay(40)
# print(pay_fulltime)


# pay_parttime = get_pay(32)
# print(pay_parttime)


# def get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket):
#     # pre-tax
#     pay_pretax = num_hours * hourly_wage
#     # after-tax
#     pay_aftertax = pay_pretax * (1 - tax_bracket)
#     return [pay_aftertax]

# higher_pay_aftertax = get_pay_with_more_inputs(40, 24, 0.22)
# print(higher_pay_aftertax)

# same_pay_fulltime = get_pay_with_more_inputs(40, 15, 0.12)
# print(same_pay_fulltime)


# def print_hello():
#     print("Hello, you!")
#     print("Good Morning!")

# print_hello()

# Ex-1
# def get_expected_cost(beds, baths):
#     value = 80000 + 30000 * beds + 10000 * baths
#     return value

# print(get_expected_cost(1,1))
# print(get_expected_cost(2,1))
# print(get_expected_cost(3,2))
# print("setup completed.")

# def get_expected_cost(beds, baths):
#     base_cost = 80000
#     bedroom_cost = beds * 30000
#     baths_cost = baths * 10000
#     expected_cost = base_cost + bedroom_cost + baths_cost
#     return expected_cost

# opt_one_cost = get_expected_cost(2,3)
# opt_two_cost = get_expected_cost(3,2)
# opt_three_cost = get_expected_cost(3,3)
# opt_four_cost = get_expected_cost(3,4)

# print("Opt 1 cost:", opt_one_cost)
# print("Opt 2 cost:", opt_two_cost)
# print("Opt 3 cost:", opt_three_cost)
# print("Opt 4 cost:", opt_four_cost)


# def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
#     total_sqft_to_paint = sqft_walls + sqft_ceiling
#     gallons_needed = total_sqft_to_paint / sqft_per_gallon

#     cost = gallons_needed * cost_per_gallon
#     return cost

# walls_sqft = 800
# ceiling_sqft = 200
# coverage_per_gallon = 400
# paint_cost_per_gallon = 30

# total_cost = get_cost(walls_sqft, ceiling_sqft, coverage_per_gallon, paint_cost_per_gallon)
# print("Total cost of painting:", total_cost)
# print("Setup complete.")

# import math
# def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
#     total_sqft_to_paint = sqft_walls + sqft_ceiling
#     gallons_needed = total_sqft_to_paint / sqft_per_gallon
#     gallons_to_buy = math.ceil(gallons_needed)
#     cost = cost_per_gallon * gallons_to_buy

#     # cost = gallons_needed * cost_per_gallon
#     return cost

# walls_sqft = 594
# ceiling_sqft = 288
# coverage_per_gallon = 400
# paint_cost_per_gallon = 15

# total_cost = get_cost(walls_sqft, ceiling_sqft, coverage_per_gallon, paint_cost_per_gallon)
# print("Total cost of painting:", total_cost)
# print("Setup complete.")