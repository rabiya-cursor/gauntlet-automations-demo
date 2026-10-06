"""AWS compute cost estimates for the demo storefront."""

HOURS_PER_MONTH = 730
SUPPORT_RATE = 0.10
SUPPORT_MINIMUM = 100.0

ON_DEMAND_HOURLY = {
    "t3.medium": 0.0416,
    "m5.large": 0.096,
    "m5.xlarge": 0.192,
    "c5.2xlarge": 0.34,
}

VOLUME_DISCOUNTS = [
    (100, 15),
    (50, 10),
    (10, 5),
]


def volume_discount_percent(instance_count):
    for min_instances, percent in VOLUME_DISCOUNTS:
        if instance_count > min_instances:
            return percent
    return 0


def on_demand_monthly(fleet):
    return sum(
        ON_DEMAND_HOURLY[group["instance_type"]] * group["count"] * HOURS_PER_MONTH
        for group in fleet
    )


def monthly_estimate(fleet):
    compute = on_demand_monthly(fleet)
    instance_count = sum(group["count"] for group in fleet)
    support = max(SUPPORT_MINIMUM, compute * SUPPORT_RATE)
    discounted = compute * (1 - volume_discount_percent(instance_count) / 100)
    return round(discounted + support, 2)


def savings_plan_commitment(hourly_spend):
    return round(min(hourly_spend), 2)
