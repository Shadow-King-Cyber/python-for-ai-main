"""Helper functions for the sales analysis."""


def calculate_total(quantity: float, price: float) -> float:
    """Calculate the total for a single item (quantity * price)."""
    return quantity * price


def format_currency(amount: float) -> str:
    """Format a number as currency, e.g. $1,234.56."""
    return f"${amount:,.2f}"
