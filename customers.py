# ism2411
# --- Exercise 1

customer = {"name": "John Smith", "email": "johnsmith@gmail.com, "tier": "Gold", "ytd_spend": 1500}

print(f"Name: {customer['name']}")
print(f"Email: {customer['email]}")
print(f"Tier: {customer['tier']}")
print(f"YTD Spend: {customer['ytd_spend]}")

print(f"Customer: {customer}")
print()

# --- Exercise 2: Update and add ---
print("---Exercise 2---")
customer["phone"] = "813-555-0142"

print(customer)
del customer["email"]

print(customer)


print("---Exercise 3---")

# New Version 
print(customer.get("email","no email on file"))

try:
    print(customer["email)])
except KeyError:
    print("KeyError: email not found")
print()


print("---Exercise 4---")
for key, value in customer.items():
    print(f"{key} : {value}")

for item in customer:
    print(item)

print("--- Exercise 5 ---")
tier_discounts = {bronze": 0,
                "silver": 0.05,
                "golad": 0.10,
                "platinum": 0.15}
purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount: {discount_rate * 100:.0f}%")
print(f"final price: ${final_price:.2f}")

print("--- Exercise 6 ---")
customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200}
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750}
    {"name": "David", "tier": "bronze", "ytd_spend": 450}
]

for record in customers: 
    rate = tier_discounts.get(record["tier'], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} discount on $300 purchase)

print("--- Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150}
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {prdocut} - Only {details['stock']} left in stock")    

print("--- Exericse 8 ---")

transactions = [
    ("region": "South", "amount": 300)
    ("region": "North", "amount": 150)
    ("region": "South", "amount": 200)
]

summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    summary[region] = summary.get(region, 0) + amount 

for region in sorted(summary):
    print(f"(region): ${summary[region]:.2f}")