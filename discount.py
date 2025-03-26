#(price, discount_percent)

user_price = float(input("Enter the price of the item: "))
user_discount_percent = float(input("Enter the discount percentage: "))
def calculate_discount(price, discount_percent):
    # for disc >20%
    if discount_percent >= 20:
        discount_amount = price * (discount_percent/100)
        new_price = price - discount_amount
        return f'The payable price is : {new_price}'
    # for disc <20%
    new_price = price 
    return f'The payable price is :{new_price}'

#calculate_discount(user_price, user_discount_percent)
print(calculate_discount(user_price, user_discount_percent))