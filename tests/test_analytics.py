from src.analytics import calculate_funnel, generate_synthetic_daily


def test_synthetic_data_is_reproducible():
    assert generate_synthetic_daily(10).equals(generate_synthetic_daily(10))


def test_funnel_rates_are_bounded():
    metrics = calculate_funnel(generate_synthetic_daily(10))
    assert all(0 <= value <= 1 for value in metrics.values())
