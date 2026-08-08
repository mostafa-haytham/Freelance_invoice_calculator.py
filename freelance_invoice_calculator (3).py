# Take all information needed .

client_name = input("Client name? ").strip().lower().title()
service_type = input("Enter service type ( web development , Design , Consulting) ").strip().lower()
if not ( service_type in ("web development","design","consulting") ) :
    print("Enter a service type in the choises")
    exit()
hourly_rate = float(input("Developer hourly rate? "))
if hourly_rate < 0 :
    print("Enter a valid hourly rate")
    exit()
worked_hours = float(input("Developer worked hours? "))
if worked_hours < 0 :
    print("Enter a valid worked hours")
    exit()
discount = float(input("Enter a discount(%) if exist "))
if 0> discount or discount >100 :
    print("Enter a valid discount(%) between(0-100)")
    exit()
tax = float(input("Enter a tax(%) if exist "))
if tax <0 :
    print("Enter a valid tax(%) ")
    exit()

# Calculate outputs .

subtotal = worked_hours * hourly_rate
discount_amount =  (discount / 100) * subtotal
subtotal_after_discount = subtotal - discount_amount
tax_amount =  (tax / 100) * subtotal_after_discount
total_price = subtotal_after_discount + tax_amount

# Display invoice .

print()
print()
print()
print("_" * 30)
print()
print("INVOICE".center(30))
print("_" * 30)
print()
print(f"Client: {client_name}")
print(f"Service: {service_type.title()}")
print()
print(f"Hourly rate: {hourly_rate:,.2f}")
print(f"Hours worked: {worked_hours:,.2f}")
print()
print(f"Sub total: ${subtotal:,.2f}")
print(f"Discount: ${discount_amount:,.2f}")
print(f"After discount: ${subtotal_after_discount:,.2f}")
print(f"Tax: ${tax_amount:,.2f}")
print("",end="\n\n")
print("-" * 30)

print(f"Total: ${total_price:,.2f}")
print("=" * 30)
