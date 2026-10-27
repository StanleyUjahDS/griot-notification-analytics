"""Synthetic notification-funnel analytics with explicit privacy boundaries."""
from __future__ import annotations

import numpy as np
import pandas as pd


def generate_synthetic_daily(days: int = 90, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    dates = pd.date_range(end=pd.Timestamp.today().normalize(), periods=days, freq="D")
    sends = rng.poisson(1000, days)
    received = rng.binomial(sends, 0.91)
    displayed = rng.binomial(received, 0.84)
    opened = rng.binomial(displayed, 0.28)
    return pd.DataFrame({"date": dates, "sends": sends, "received": received, "displayed": displayed, "opened": opened})


def calculate_funnel(frame: pd.DataFrame) -> dict[str, float]:
    totals = frame[["sends", "received", "displayed", "opened"]].sum()
    return {
        "delivery_rate": float(totals.received / totals.sends),
        "display_rate": float(totals.displayed / totals.received),
        "open_rate": float(totals.opened / totals.displayed),
        "end_to_end_rate": float(totals.opened / totals.sends),
    }


def main() -> None:
    frame = generate_synthetic_daily()
    print(frame.head())
    print(calculate_funnel(frame))


if __name__ == "__main__":
    main()
