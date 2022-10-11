normal_price= 24.95
discount= 0.40 * normal_price
sale_price_per_book= normal_price-discount
total_price= sale_price_per_book*60
first_book_shipping=3
other_book_shipping= 0.75
total_shipping_cost= 3 +(0.75*59)
wholesale_price=(total_price+total_shipping_cost)
print(wholesale_price)

a=5
b=7
c=10
s=(a + b + c) / 2
pre_solution= s * (s-a) * (s-b) * (s-c)
area=pre_solution ** 0.5
print(area)