from app.order_processor import calculate_discount, apply_tax, parse_quantity


def test_vip_discount_high():
    assert calculate_discount(200, "VIP") == 40.0


def test_regular_discount_low():
    assert calculate_discount(50, "REGULAR") == 0.0


def test_apply_tax_ontario():
    assert apply_tax(100, "ON") == 113.0


def test_parse_quantity_valid():
    assert parse_quantity("5") == 5