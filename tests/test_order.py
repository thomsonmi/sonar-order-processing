from app.orderprocessor import (
    calculate_discount,
    apply_tax,
    parse_quantity,
    format_receipt,
    get_payment_api_key,
)


def test_vip_discount_high():
    assert calculate_discount(200, "VIP") == 40.0


def test_vip_discount_low():
    assert calculate_discount(80, "VIP") == 8.0


def test_regular_discount_high():
    assert calculate_discount(150, "REGULAR") == 15.0


def test_regular_discount_low():
    assert calculate_discount(50, "REGULAR") == 0.0


def test_unknown_customer_discount():
    assert calculate_discount(200, "GUEST") == 0.0


def test_apply_tax_regions():
    assert apply_tax(100, "ON") == 113.0
    assert apply_tax(100, "BC") == 112.0
    assert apply_tax(100, "AB") == 105.0


def test_parse_quantity_valid_and_invalid():
    assert parse_quantity("5") == 5
    assert parse_quantity("-3") == 0
    assert parse_quantity("abc") == 0
    assert parse_quantity(None) == 0


def test_format_receipt():
    assert format_receipt("Alice", 25.5) == "Receipt for Alice: $25.50"
    assert format_receipt(None, 10) == "Receipt for Guest: $10.00"


def test_get_payment_api_key_default():
    assert isinstance(get_payment_api_key(), str)