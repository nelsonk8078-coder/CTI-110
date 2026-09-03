# CTI 110
#p1lab2 - selling things
# nelson k
#9/3/26

# product_name = "Brnd Name Jeans"
# product_count = 250
# Product_price = 125.00

print ("store start up")
print ("_" * 10)
product_name = input("Enter product name")
product_count = input("Enter product price")
product_price = input("Enter unit price")

# processing
product_count = int(product_count)
product_price = float(product_price)
total = product_count * product_price


# output
print("Customer interface")
print ("_" * 10)
print(f"welcome to the {product_name} store")
print(f"we have {product_count} {product_name}(s) at $ {product_price:.2f} each")
print(f"total is: $ {total:.2f}")