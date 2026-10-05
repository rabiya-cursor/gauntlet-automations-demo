import pytest

from src.pricing import bulk_discount_percent


@pytest.mark.parametrize(
    "quantity, expected",
    [
        (0, 0),
        (9, 0),
        (10, 5),
        (49, 5),
        (50, 10),  # tier boundary: 50+ units -> 10%
        (99, 10),
        (100, 15),  # tier boundary: 100+ units -> 15%
        (250, 15),
    ],
)
def test_bulk_discount_tiers(quantity, expected):
    assert bulk_discount_percent(quantity) == expected


def test_bulk_discount_never_decreases_from_0_to_200():
    previous = bulk_discount_percent(0)
    for quantity in range(1, 201):
        current = bulk_discount_percent(quantity)
        assert current >= previous
        previous = current
