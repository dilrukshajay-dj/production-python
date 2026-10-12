""" Core sales-report logic
Tis module module knows nothing about the CLI, argv, or hardcoded paths. IT takes a path in, and gives data back.

"""

import csv
from pathlib import Path
def read_sales_rows(path: Path)-> list[dict[str, str]]:
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def total_revenue_by_store(rows: list[dict[str, str]]) -> dict[str, float]:
    totals = {}
    for row in rows:
        store = row["store_id"]
        qty = int(row["quantity"])
        price = float(row["unit_price"])
        totals[store] = totals.get(store, 0.0) + qty * price
    return totals

