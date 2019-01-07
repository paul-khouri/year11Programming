#constants
main_price = 12.5
dessert_price = 6.0
drinks_price = 3.55

#totalling variables (initially declared as 0)
mains_total = 0.0
desserts_total = 0.0
drinks_total = 0.0
ext_gst = 0.0

# input variables
mains = int(input("How many mains would you like to order?: "))
desserts = int(input("How many desserts would you like to order?: "))
drinks = int(input("How many drinks would you like to order?: "))

# Testing
#mains = 6
#desserts = 5
#drinks = 7

mains_total = mains * main_price
desserts_total = desserts * dessert_price
drinks_total = drinks * drinks_price

ext_gst = mains_total + desserts_total + drinks_total
my_gst = ext_gst*0.15
my_to_pay = ext_gst + my_gst

print("-"*40)
print("Bill's Diner")
print("-"*40)
print("-"*40)
print("{:<3}{:10}at ${:<10.2f}= ${:.2f}".format(mains,"mains", main_price, mains_total))
print("{:<3}{:10}at ${:<10.2f}= ${:.2f}".format(desserts,"desserts", dessert_price, desserts_total))
print("{:<3}{:10}at ${:<10.2f}= ${:.2f}".format(drinks,"drinks", drinks_price, drinks_total))
print("-"*40)
print("{:>27}= ${}".format("Total  ", ext_gst))
print("{:>27}= ${:.2f}".format("GST  ", my_gst))
print("{:>27}= ${:.2f}".format("To Pay  ", my_to_pay))
print("-"*40)
print("Thankyou")
print("-"*40)