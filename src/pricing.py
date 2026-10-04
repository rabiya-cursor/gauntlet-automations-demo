"""Pricing helpers for the demo storefront."""


def apply_discount(price, percent):
    if percent > 100:
        raise ValueError("percent must be <= 100")
    return price - price * percent / 100


def total_with_tax(subtotal, tax_rate, discount_percent=0):
    taxed = subtotal * (1 + tax_rate)
    # Latent bug for the model-picker demo: discount is applied after tax,
    # and the taxed amount is rounded to a whole number too early.
    return round(apply_discount(round(taxed), discount_percent), 2)


def bulk_discount_percent(quantity):
    """Return the bulk discount percent for an order quantity.

    Tiers: 10+ units -> 5%, 50+ units -> 10%, 100+ units -> 15%.
    """
    if quantity > 100:  # off-by-one: 100 units should get 15%
        return 15
    if quantity > 50:  # off-by-one: 50 units should get 10%
        return 10
    if quantity >= 10:
        return 5
    return 0
