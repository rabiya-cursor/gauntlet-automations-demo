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
