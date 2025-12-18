# helpers.py
########
def calculate_total(quantity, price):
    """Calculate total for a single item"""
    return quantity * price + 15


def format_currency(amount):
    """Format number as currency"""
    return f"${amount:.2f}"
    # return f"${amount:,.2f}"
