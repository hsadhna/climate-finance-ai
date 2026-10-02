"""
carbon_engine.py — Phase 1 (carbon accounting) + first piece of Phase 2 (carbon cost)

Method: GHG Protocol Corporate Standard, activity-based approach
    Emissions (tCO2e) = Activity data x Emission factor

IMPORTANT: The emission factors and company data below are ILLUSTRATIVE PLACEHOLDERS
so the code runs. Replace them with real factors from an authoritative source
(e.g., ECCC National Inventory Report, BC Methodological Guidance for Quantifying GHG
Emissions) and real company activity data before using any output.
"""

from dataclasses import dataclass
import pandas as pd


@dataclass
class EmissionFactor:
    value: float          # tCO2e per unit of activity
    unit: str             # e.g., "tCO2e/GJ"
    source: str           # publication name
    year: int             # factor year


@dataclass
class ActivityRecord:
    source_name: str      # e.g., "Natural gas - boilers"
    scope: str            # "Scope 1", "Scope 2", "Scope 3 Cat 6", ...
    quantity: float       # activity data
    unit: str             # e.g., "GJ", "kWh"
    factor: EmissionFactor
    data_status: str      # "Reported", "Estimated", or "Assumed"
    note: str = ""


def calculate_inventory(records: list[ActivityRecord]) -> pd.DataFrame:
    """Return one row per source, showing every input so results can be checked."""
    rows = []
    for r in records:
        rows.append({
            "Source": r.source_name,
            "Scope": r.scope,
            "Activity": r.quantity,
            "Activity unit": r.unit,
            "EF": r.factor.value,
            "EF unit": r.factor.unit,
            "EF source": f"{r.factor.source} ({r.factor.year})",
            "tCO2e": r.quantity * r.factor.value,
            "Data status": r.data_status,
            "Note": r.note,
        })
    return pd.DataFrame(rows)


def carbon_cost(total_tco2e: float, price_per_t: float) -> float:
    """Carbon cost = tCO2e x carbon price per tCO2e."""
    return total_tco2e * price_per_t


def ebitda_impact(cost: float, ebitda: float) -> float:
    """Carbon cost as a % of EBITDA."""
    return cost / ebitda * 100


if __name__ == "__main__":
    # --- PLACEHOLDER INPUTS: replace with real, sourced values ---
    placeholder_ef_gas = EmissionFactor(0.05, "tCO2e/GJ", "PLACEHOLDER - replace", 2026)
    placeholder_ef_elec = EmissionFactor(0.00001, "tCO2e/kWh", "PLACEHOLDER - replace", 2026)

    records = [
        ActivityRecord("Natural gas - boilers", "Scope 1", 120_000, "GJ",
                       placeholder_ef_gas, "Assumed", "Demo value"),
        ActivityRecord("Purchased electricity", "Scope 2", 40_000_000, "kWh",
                       placeholder_ef_elec, "Assumed", "Location-based; demo value"),
    ]

    inventory = calculate_inventory(records)
    print(inventory.to_string(index=False))
    print("\nTotal by scope (tCO2e):")
    print(inventory.groupby("Scope")["tCO2e"].sum())

    total = inventory["tCO2e"].sum()
    assumed_ebitda = 50_000_000   # PLACEHOLDER company EBITDA ($)
    for label, price in [("Low", 50), ("Base", 110), ("High", 170)]:  # assumed $/tCO2e
        cost = carbon_cost(total, price)
        print(f"{label:5} ${price}/t -> carbon cost ${cost:,.0f} "
              f"= {ebitda_impact(cost, assumed_ebitda):.2f}% of EBITDA")
        