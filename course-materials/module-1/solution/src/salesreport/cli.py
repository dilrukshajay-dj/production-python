""" CLI for sales report 
This module knows about the CLI, argv, and hardcoded paths. It takes a path in, and gives data back.
"""

from pathlib import Path

import click

from salesreport.report import read_sales_rows, total_revenue_by_store


@click.group()
def cli() -> None:
    """salesreport - daily store revenue reporting."""
    


@cli.command()
@click.option(
    "--input",
    "input_path",
    required=True,
    type=click.Path(exists=True, path_type=Path),
    default=Path("sample_data/sales_sample.csv"),
    help="Path to the sales CSV file.",
)
def generate(input_path: Path) -> None:
    """Generate a sales report from the given CSV file."""
    rows = read_sales_rows(input_path)
    totals = total_revenue_by_store(rows)
    click.echo("Revenue by store:")
    for store, total in sorted(totals.items()):
        click.echo(f"  {store}: ${total:.2f}")

    if __name__ == "__main__":
        cli()
        