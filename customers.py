# Tony Wiley - ISM2411 Lab 11
#
# Reflection 1:
# I use .get() when a field might be missing so the program doesn't crash,
# and I use brackets when the field always has to be there.
# My rule is: if missing data is normal, use .get(); if it means something
# is wrong, use brackets.
#
# Reflection 2:
# Building a summary dictionary reminds me of a pivot table or SUMIF in Excel,
# where you total sales by region. The Python version is better for big
# datasets because it can handle millions of rows without slowing down, and
# you can run the same code again on new data with no extra work.

# --- Exercise 1 ---
print("--- Exercise 1 ---")
customer = {"name": "John Smith", "email": "johnsmith@gmail.com",
            "tier": "gold", "ytd_spend": 1500}

print(f"Name: {customer['name']}")
print(f"Email: {customer['email']}")
print(f"Tier: {customer['tier']}")
print(f"YTD Spend: {customer['ytd_spend']}")
print(f"Customer: {customer}")
print()

# --- Exercise 2 ---
print("--- Exercise 2 ---")
customer["phone"] = "813-555-0142"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)
print()

# --- Exercise 3 ---
print("--- Exercise 3 ---")
print(customer.get("email", "no email on file"))
try:
    print(customer["email"])
except KeyError:
    print("KeyError: email not found")
print()

# --- Exercise 4 ---
print("--- Exercise 4 ---")
for key, value in customer.items():
    print(f"{key}: {value}")

# Looping without .items() only gives the keys, not the values
for item in customer:
    print(item)
print()

# --- Exercise 5 ---
print("--- Exercise 5 ---")
tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.10, "platinum": 0.15}
purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount: {discount_rate * 100:.0f}%")
print(f"Final price: ${final_price:.2f}")
print()

# --- Exercise 6 ---
print("--- Exercise 6 ---")
customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} discount on $300 purchase")
print()

# --- Exercise 7 ---
print("--- Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - Only {details['stock']} left in stock")
print()

# --- Exercise 8 ---
print("--- Exercise 8 ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

summary = {}
for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    summary[region] = summary.get(region, 0) + amount

for region in sorted(summary):
    print(f"{region}: ${summary[region]:.2f}")