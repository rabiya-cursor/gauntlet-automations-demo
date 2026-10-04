from src.pricing import apply_discount, total_with_tax


def test_apply_discount_basic():
    assert apply_discount(100, 10) == 90


def test_total_no_discount():
    assert total_with_tax(100, 0.1) == 110
