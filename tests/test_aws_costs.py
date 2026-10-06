from src.aws_costs import (
    monthly_estimate,
    on_demand_monthly,
    savings_plan_commitment,
    volume_discount_percent,
)


def test_volume_discount_percent():
    assert volume_discount_percent(4) == 0
    assert volume_discount_percent(20) == 5
    assert volume_discount_percent(75) == 10
    assert volume_discount_percent(150) == 15


def test_on_demand_monthly():
    fleet = [{"instance_type": "m5.large", "count": 4}]
    assert round(on_demand_monthly(fleet), 2) == 280.32


def test_monthly_estimate_small_fleet():
    fleet = [{"instance_type": "m5.large", "count": 4}]
    assert monthly_estimate(fleet) == 380.32


def test_monthly_estimate_discounted_fleet():
    fleet = [{"instance_type": "t3.medium", "count": 20}]
    assert monthly_estimate(fleet) == 676.99


def test_monthly_estimate_mixed_fleet():
    fleet = [
        {"instance_type": "c5.2xlarge", "count": 3},
        {"instance_type": "m5.xlarge", "count": 2},
    ]
    assert monthly_estimate(fleet) == 1127.41


def test_savings_plan_commitment():
    assert savings_plan_commitment([1.2, 0.95, 1.4]) == 0.95
