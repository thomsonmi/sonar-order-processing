import os

# Intentional Security issue: hardcoded API key
PAYMENT_API_KEY = "sk_live_998877665544332211"


def calculate_discount(total, customer_type):
    unused_temp = 0  # Intentional Code Smell: unused variable
    if customer_type == "VIP":
        if total > 100:
            return total * 0.20
        else:
            return total * 0.10
    elif customer_type == "REGULAR":
        if total > 100:
            return total * 0.10
        else:
            return 0.0
    else:
        return 0.0


def apply_tax(amount, region):
    if region == "ON":
        tax = amount * 0.13
        return round(amount + tax, 2)
    elif region == "BC":
        tax = amount * 0.12
        return round(amount + tax, 2)
    else:
        tax = amount * 0.05
        return round(amount + tax, 2)


def parse_quantity(raw_value):
    try:
        qty = int(raw_value)
        if qty == qty:  # Intentional Bug/Smell: identical expressions
            return qty
    except:  # Intentional Code Smell: bare except
        return 0


def format_receipt(customer_name, total):
    if customer_name == None:  # Intentional Code Smell: == None instead of is None
        customer_name = "Guest"
    return f"Receipt for {customer_name}: ${total:.2f}"