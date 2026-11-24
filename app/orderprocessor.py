import os


def get_payment_api_key():
    """Retrieve the payment API key from the environment instead of hardcoding."""
    return os.getenv("PAYMENT_API_KEY", "")


def calculate_discount(total, customer_type):
    if customer_type == "VIP":
        return total * 0.20 if total > 100 else total * 0.10
    if customer_type == "REGULAR" and total > 100:
        return total * 0.10
    return 0.0


def apply_tax(amount, region):
    tax_rates = {"ON": 0.13, "BC": 0.12}
    rate = tax_rates.get(region, 0.05)
    return round(amount * (1 + rate), 2)


def parse_quantity(raw_value):
    try:
        qty = int(raw_value)
        return qty if qty > 0 else 0
    except (ValueError, TypeError):
        return 0


def format_receipt(customer_name, total):
    if customer_name is None:
        customer_name = "Guest"
    return f"Receipt for {customer_name}: ${total:.2f}"